from BTPIntegra.app import db

class ConteudoConsumido(db.Model):
    __tablename__: 'conteudos_consumidos'

    id = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    idConteudo = db.Column(db.Integer, db.ForeignKey('conteudo.id'))

    def __init__(self, idUsuario, idConteudo):
        self.idUsuario = idUsuario
        self.idConteudo = idConteudo