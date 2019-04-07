from BTPIntegra.app import db

class Avaliacao(db.Model):
    __tablename__: 'avaliacoes'

    id = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    idConteudo = db.Column(db.Integer, db.ForeignKey('conteudo.id'))
    valor = db.Column(db.Float)

    def __init__(self, idUsuario, idConteudo, valor):
        self.idUsuario = idUsuario
        self.idConteudo = idConteudo
        self.valor = valor