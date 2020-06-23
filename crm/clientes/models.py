from crm import app, db

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30))
    historico_status = db.Column(db.String(100))
    observacoes = db.Column(db.String)
    email = db.Column(db.String)
    telefone = db.Column(db.Integer)
    endereco = db.Column(db.String)
    status = db.Column(db.String)
    datainsercao = db.Column(db.String)
    prospeccao = db.Column(db.String)