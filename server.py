from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def Welcome():
    return "Welcome to Playground!"

@app.route("/play/<number>/<color>")
def play(number, color):
    return render_template("index.html", num=int(number), change=color)

if __name__ == "__main__":
    app.run(debug=True)