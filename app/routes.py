from app import app
from flask import render_template, redirect

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/pagina2")
def cadastrar():
    return render_template("pag2.html")

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

