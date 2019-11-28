from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def top_route():
    return render_template("top.html")


#おまじない
if __name__ == "__main__":
    app.run(debug=True)