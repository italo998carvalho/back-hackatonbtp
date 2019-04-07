from BTPIntegra.app import db
from werkzeug.security import generate_password_hash

class Usuario(db.Model):
    __tablename__: 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    registro = db.Column(db.Integer)
    senha = db.Column(db.String(255))
    funcao = db.Column(db.String(100))
    dataNascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(1))
    fotoPerfil = db.Column(db.String)

    def __init__(self, nome, registro, senha, funcao, dataNascimento, sexo, fotoPerfil):
        self.nome = nome
        self.registro = registro
        self.senha = generate_password_hash(senha)
        self.funcao = funcao
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.fotoPerfil = fotoPerfil