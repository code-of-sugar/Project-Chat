from flask import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import MeCab

import argparse
import pyaudio
import wave
from pykakasi import kakasi
import re
import csv
import time


parser = argparse.ArgumentParser(description="convert csv")
parser.add_argument("input", type=str, help="faq tsv file")
parser.add_argument("--dictionary", "-d", type=str, help="mecab dictionary")
parser.add_argument("--stop_words", "-s", type=str, help="stop words list")
args = parser.parse_args()

app = Flask(__name__)

def save_questions(line):
    with open('conversation_new.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow({line})
        
def conversation(username,questions,vecs,mecab,vectorizer):
    line = username
    line1=line
    line2=line
    line3=line
    with open('conversation_.csv', 'a', newline='') as f: #a+ #w
        writer = csv.writer(f)
        writer.writerow({line})
        sims = cosine_similarity(vectorizer.transform([mecab.parse(line)]), vecs)
        index = np.argsort(sims[0])
        line3=line2
        line2=line1
        line1=line
        while True:
            index_= index[-np.random.randint(1,10)]
            line = questions[index_]
            if line1==line or line2==line or line3==line:
                continue
            else:
                break
            conv_new=read_conv(mecab)
            s=1
            ss=1
            for j in range(0,len(conv_new),1):
                if line==conv_new[j]: 
                    s=0
                else:
                    s=1
                ss *= s
                #print(ss,s)
            if ss == 0:
                continue
            else:
                break
        save_questions(line)
        return questions[index_]

def train_conv(mecab):
    questions = []
    with open('conversation_.csv') as f:
        cols = f.read().strip().split('\n')
        for i in range(len(cols)):
            questions.append(mecab.parse(cols[i]).strip())
    return questions        

def read_conv(mecab):
    conv_new = []
    with open('conversation_new.csv') as f:
        cols = f.read().strip().split('\n')
        for i in range(len(cols)):
            conv_new.append(mecab.parse(cols[i]).strip())
    return conv_new

@app.route("/", methods=["GET"])
def top_render():
    return render_template("top.html")

@app.route("/", methods=["POST"])
def getBotMessage():
    username = request.json
    mecab = MeCab.Tagger("-Owakati" + ("" if not args.dictionary else " -d " + args.dictionary))
    stop_words = []
    if args.stop_words:
        for line in open(args.stop_words, "r", encoding="utf-8"):
            stop_words.append(line.strip())

    questions = train_conv(mecab)
    vectorizer = TfidfVectorizer(token_pattern="(?u)\\b\\w+\\b", stop_words=stop_words)
    vecs = vectorizer.fit_transform(questions)
    chatmessage = conversation(username,questions,vecs,mecab,vectorizer)
    return Response(chatmessage)




#おまじない
if __name__ == "__main__":
    app.run(debug=True)