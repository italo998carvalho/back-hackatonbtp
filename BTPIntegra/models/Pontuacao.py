from BTPIntegra.app import db

class Pontuacao(db.Model):
    __tablename__: 'pontuacoes'

    id = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    valor = db.Column(db.Float)

    def __init__(self, idUsuario, valor):
        self.idUsuario = idUsuario
        self.valor = valor