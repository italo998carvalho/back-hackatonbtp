from flask import Blueprint, request, jsonify
from BTPIntegra.models.Conteudo import Conteudo
from BTPIntegra.models.ConteudoConsumido import ConteudoConsumido
from BTPIntegra.models.Arquivo import Arquivo
from BTPIntegra.models.Avaliacao import Avaliacao
from BTPIntegra.models.Usuario import Usuario
from BTPIntegra.app import app, db
from BTPIntegra.views.login import token_required
from BTPIntegra.config import pontuacaoPorConteudoGerado, pontuacaoPorConteudoConsumido, categoriasAceitas

@token_required
def atribuirPontos(self, valor):
    self.pontuacao += valor
        
    try:
        db.session.add(self)
        db.session.commit()
    except:
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

content = Blueprint('content', __name__)

@content.route('/conteudo', methods=['POST', 'GET'])
@token_required
def conteudo(usuarioAtual):
    data = request.get_json()

    if request.method == 'POST':
        idUsuario = usuarioAtual.id
        titulo = data['titulo']
        descricao = data['descricao']
        categoria = data['categoria']

        if categoria not in categoriasAceitas:
            return jsonify({'code': 400, 'body':{'mensagem': 'Categoria inexistente!'}})
        
        conteudo = Conteudo(idUsuario, titulo, descricao, categoria)

        try:
            db.session.add(conteudo)
            db.session.commit()
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

        dados = data['arquivos']
        for info in dados:

            arquivo = Arquivo(conteudo.id, info)

            try:
                db.session.add(arquivo)
                db.session.commit()
            except:
                return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

        atribuirPontos(pontuacaoPorConteudoGerado)
        
        return jsonify({'code': 200, 'body': {'mensagem': 'Conteúdo cadastrado com sucesso!'}})
    
    elif request.method == 'GET':
        conteudos = Conteudo.query.all()

        listaConteudo = []
        for conteudo in conteudos:
            try:
                arquivos = Arquivo.query.filter_by(idConteudo = conteudo.id).all()
            except:
                return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

            conteudoAtual = {}
            conteudoAtual['id'] = conteudo.id
            conteudoAtual['idUsuario'] = conteudo.idUsuario
            conteudoAtual['titulo'] = conteudo.titulo
            conteudoAtual['descricao'] = conteudo.descricao

            listaArquivos = []
            for arquivo in arquivos:
                arquivoAtual = {}
                arquivoAtual['midia'] = arquivo.midia

                listaArquivos.append(arquivoAtual)
            
            conteudoAtual['arquivos'] = listaArquivos

            avaliacoes = Avaliacao.query.filter_by(idConteudo = conteudo.id).all()

            somaAvaliacoes = 0
            contadorDeAvaliacoes = 0

            for avaliacao in avaliacoes:
                somaAvaliacoes += avaliacao.valor
                contadorDeAvaliacoes += 1
                
            if contadorDeAvaliacoes > 0:
                media = somaAvaliacoes / contadorDeAvaliacoes
                conteudoAtual['avaliacaoMedia'] = media
            else:
                conteudoAtual['avaliacaoMedia'] = None

            conteudoAtual['numeroDeAvaliacoes'] = contadorDeAvaliacoes

            listaConteudo.append(conteudoAtual)
        
        return jsonify({'code': 200, 'body': listaConteudo})

    else:
        return jsonify({'code': 403, 'body': {'mensagem': 'Método inválido!'}}), 403

@content.route('/conteudo/<int:id>', methods=['GET'])
@token_required
def oneConteudo(usuarioAtual, id):
    conteudo = Conteudo.query.filter_by(id = id).first()

    conteudoAtual = {}
    conteudoAtual['idUsuario'] = conteudo.idUsuario
    conteudoAtual['titulo'] = conteudo.titulo
    conteudoAtual['descricao'] = conteudo.descricao

    arquivos = Arquivo.query.filter_by(idConteudo = conteudo.id).all()

    listaArquivos = []
    for arquivo in arquivos:
        arquivoAtual = {}
        arquivoAtual['midia'] = arquivo.midia

        listaArquivos.append(arquivoAtual)
            
    conteudoAtual['arquivos'] = listaArquivos

    avaliacoes = Avaliacao.query.filter_by(idConteudo = conteudo.id).all()

    somaAvaliacoes = 0
    contadorDeAvaliacoes = 0

    for avaliacao in avaliacoes:
        somaAvaliacoes += avaliacao.valor
        contadorDeAvaliacoes += 1
                
    if contadorDeAvaliacoes > 0:
        media = somaAvaliacoes / contadorDeAvaliacoes
        conteudoAtual['avaliacaoMedia'] = media
    else:
        conteudoAtual['avaliacaoMedia'] = None

    conteudoAtual['numeroDeAvaliacoes'] = contadorDeAvaliacoes

    return jsonify({'code': 200, 'body': conteudoAtual})

@content.route('/conteudo/<string:categoria>', methods=['GET'])
@token_required
def filtrarConteudo(usuarioAtual,categoria):
    if request.method == 'GET':
        try:
            conteudos = Conteudo.query.filter_by(categoria = categoria).all()

            listaConteudo = []
            for conteudo in conteudos:
                try:
                    arquivos = Arquivo.query.filter_by(idConteudo = conteudo.id).all()
                except:
                    return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

                conteudoAtual = {}
                conteudoAtual['id'] = conteudo.id
                conteudoAtual['idUsuario'] = conteudo.idUsuario
                conteudoAtual['titulo'] = conteudo.titulo
                conteudoAtual['descricao'] = conteudo.descricao

                listaArquivos = []
                for arquivo in arquivos:
                    arquivoAtual = {}
                    arquivoAtual['midia'] = arquivo.midia

                    listaArquivos.append(arquivoAtual)
                
                conteudoAtual['arquivos'] = listaArquivos

                avaliacoes = Avaliacao.query.filter_by(idConteudo = conteudo.id).all()

                somaAvaliacoes = 0
                contadorDeAvaliacoes = 0

                for avaliacao in avaliacoes:
                    somaAvaliacoes += avaliacao.valor
                    contadorDeAvaliacoes += 1
                    
                if contadorDeAvaliacoes > 0:
                    media = somaAvaliacoes / contadorDeAvaliacoes
                    conteudoAtual['avaliacaoMedia'] = media
                else:
                    conteudoAtual['avaliacaoMedia'] = None

                conteudoAtual['numeroDeAvaliacoes'] = contadorDeAvaliacoes

                listaConteudo.append(conteudoAtual)
            
            return jsonify({'code': 200, 'body': listaConteudo})

        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
    else:
        return jsonify({'code': 403, 'body': {'mensagem': 'Método inválido!'}}), 403

@content.route('/conteudo/<int:id>/visto', methods=['POST'])
@token_required
def visualizarConteudo(usuarioAtual, id):
    if request.method == 'POST':
        conteudo = Conteudo.query.filter_by(id = id).first()

        if not conteudo:
            return jsonify({'code': 200, 'body':{'mensagem': 'Conteúdo inexistente!'}})

        conteudoChecado = ConteudoConsumido.query.filter_by(idUsuario = usuarioAtual.id, idConteudo = conteudo.id).first()
        if conteudoChecado:
            return jsonify({'code': 200, 'body':{'mensagem': 'Você já visualizou este conteúdo!'}})
        
        conteudoConsumido = ConteudoConsumido(usuarioAtual.id, conteudo.id)

        try:
            db.session.add(conteudoConsumido)
            db.session.commit()
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

        atribuirPontos(pontuacaoPorConteudoConsumido)

        data = request.get_json()
        nota = data['nota']
        avaliacao = Avaliacao(usuarioAtual.id, conteudo.id, nota)
        try:
            db.session.add(avaliacao)
            db.session.commit()
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

        return jsonify({'code': 200, 'body': {'mensagem': 'Sucesso!!'}})

    else:
        return jsonify({'code': 403, 'body': {'mensagem': 'Método inválido!'}}), 403

@content.route('/conteudosConsumidos', methods=['GET'])
@token_required
def visualizarEventosConsumidos(usuarioAtual):
    if request.method == 'GET':
        try:
            conteudos = ConteudoConsumido.query.filter_by(idUsuario = usuarioAtual.id).all()

            conteudosConsumidos = []
            for conteudo in conteudos:
                conteudo = Conteudo.query.filter_by(id = conteudo.idConteudo).first()
                
                conteudoAtual = {}
                conteudoAtual['id'] = conteudo.id
                conteudoAtual['titulo'] = conteudo.titulo
                conteudoAtual['descricao'] = conteudo.descricao

                arquivos = Arquivo.query.filter_by(idConteudo = conteudo.id).all()
                arquivosAtuais = []
                for arquivo in arquivos:
                    arquivoAtual = {}
                    arquivoAtual['midia'] = arquivo.midia

                    arquivosAtuais.append(arquivoAtual)

                conteudoAtual['arquivos'] = arquivosAtuais

                conteudosConsumidos.append(conteudoAtual)
            
            return jsonify({'code': 200, 'body': conteudosConsumidos})
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
    
    else:
        return jsonify({'code': 403, 'body': {'mensagem': 'Método inválido!'}}), 403