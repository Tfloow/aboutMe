from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<path:secret>")
def secret(secret):
    return render_template("404.html")