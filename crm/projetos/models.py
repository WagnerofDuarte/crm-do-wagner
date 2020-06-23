from crm import app, db

class Projeto(db.Model):
    __tablename__ = "projeto"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30),nullable = False)
    comentarios = db.Column(db.String, nullable = True)
    nota = db.Column(db.Integer, nullable = True)