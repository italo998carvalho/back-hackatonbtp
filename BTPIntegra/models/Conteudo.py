from BTPIntegra.app import db

class Conteudo(db.Model):
    __tablename__: 'conteudos'

    id = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    titulo = db.Column(db.String)
    descricao = db.Column(db.String)
    arquivos = db.relationship('Arquivo', backref='conteudo')
    categoria = db.Column(db.String)

    def __init__(self, idUsuario, titulo, descricao, categoria):
        self.idUsuario = idUsuario
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria