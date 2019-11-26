from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


@app.route("/top")
def index():
    return render_template(".html")


#おまじない
if __name__ == "__main__":
    app.run(debug=True)