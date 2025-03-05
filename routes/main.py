from app import app
from flask import render_template


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/lol")
def lol():
    return "This is LOL page!"

@app.route("/hello/<string:name>/<string:last_name>")
def hello_user(name, last_name):
    return  render_template("index.html", name=name, last_name=last_name)
