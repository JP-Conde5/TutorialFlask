from app import app, db
from flask import render_template, redirect, request
from app.models.site import Site

@app.route("/")
def index():
   sites_ = Site.query.all()
   return render_template("index.html", sites = sites_)

@app.route("/pagina2", methods=["POST", "GET"])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        dominio = request.form.get('dominio')
        novo_site = Site(nome=nome, dominio=dominio)
        db.session.add(novo_site)
        db.session.commit()
        return redirect('/')
    return render_template("pag2.html")

@app.route("/editar/<int:id>", methods=["POST", "GET"])
def editar(id):
    site_ = Site.query.get_or_404(id)
    if request.method == 'POST':
        site_.nome = request.form.get('nome')
        site_.dominio = request.form.get('dominio')
        db.session.commit()
        return redirect('/')
    return render_template("editar.html", site = site_)

@app.route("/deletar/<int:id>")
def deletar(id):
    site = Site.query.get_or_404(id)
    db.session.delete(site)
    db.session.commit()
    return redirect('/')

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

