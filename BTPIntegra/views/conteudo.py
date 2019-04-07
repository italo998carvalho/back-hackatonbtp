from flask import Blueprint, request, jsonify
from BTPIntegra.models.Conteudo import Conteudo
from BTPIntegra.models.ConteudoConsumido import ConteudoConsumido
from BTPIntegra.models.Arquivo import Arquivo
from BTPIntegra.models.Pontuacao import Pontuacao
from BTPIntegra.app import app, db
from BTPIntegra.views.login import token_required
from BTPIntegra.config import pontuacaoPorConteudoGerado, pontuacaoPorConteudoConsumido

@token_required
def atribuirPontos(idUsuario, valor):
    pontuacao = Pontuacao.query.filter_by(idUsuario = idUsuario).first()
    if not pontuacao:
        pontuacao = Pontuacao(usuarioAtual.id, valor)
    else:
        pontuacao.valor += valor
        
    try:
        db.session.add(pontuacao)
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
        
        conteudo = Conteudo(idUsuario, titulo, descricao)

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

        atribuirPontos(usuarioAtual.id, pontuacaoPorConteudoGerado)
        
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

    return jsonify({'code': 200, 'body': conteudoAtual})

@content.route('/conteudo/<int:id>/visto', methods=['POST'])
@token_required
def visualizarConteudo(usuarioAtual, id):
    if request.method == 'POST':
        conteudo = Conteudo.query.filter_by(id = id).first()

        if not conteudo:
            return jsonify({'code': 200, 'body':{'mensagem': 'Conteúdo inexistente!'}})

        conteudoChecado = ConteudoConsumido.query.filter_by(idConteudo = conteudo.id).first()
        if conteudoChecado:
            return jsonify({'code': 200, 'body':{'mensagem': 'Você já visualizou este conteúdo!'}})
        
        conteudoConsumido = ConteudoConsumido(usuarioAtual.id, conteudo.id)

        try:
            db.session.add(conteudoConsumido)
            db.session.commit()
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

        atribuirPontos(usuarioAtual.id, pontuacaoPorConteudoGerado)

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