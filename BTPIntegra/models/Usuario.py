from BTPIntegra.app import db
from werkzeug.security import generate_password_hash

class Usuario(db.Model):
    __tablename__: 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    registro = db.Column(db.Integer)
    senha = db.Column(db.String(255))

    def __init__(self, nome, registro, senha):
        self.nome = nome
        self.registro = registro
        self.senha = generate_password_hash(senha)