from BTPIntegra.app import db

class Arquivo(db.Model):
    __tablename__: 'arquivos'

    id = db.Column(db.Integer, primary_key=True)
    idConteudo = db.Column(db.Integer, db.ForeignKey('conteudo.id'))
    midia = db.Column(db.Text)

    def __init__(self, idConteudo, midia):
        self.idConteudo = idConteudo
        self.midia = midia