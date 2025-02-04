from app import db

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    dominio = db.Column(db.String(100), nullable=True)
    #feedback = db.Column(db.Boolean, nullable=True)