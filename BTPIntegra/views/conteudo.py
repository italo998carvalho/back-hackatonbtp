from flask import Blueprint, request, jsonify
from BTPIntegra.models.Conteudo import Conteudo
from BTPIntegra.models.Arquivo import Arquivo
from BTPIntegra.models.Pontuacao import Pontuacao
from BTPIntegra.app import app, db
from BTPIntegra.views.login import token_required
from BTPIntegra.config import pontuacaoPorConteudoGerado

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

            arquivo = Arquivo(usuarioAtual.id, info)

            try:
                db.session.add(arquivo)
                db.session.commit()
            except:
                return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

        pontuacao = Pontuacao.query.filter_by(idUsuario = usuarioAtual.id).first()
        if not pontuacao:
            pontuacao = Pontuacao(usuarioAtual.id, pontuacaoPorConteudoGerado)
        else:
            pontuacao.valor += pontuacaoPorConteudoGerado
        
        try:
            db.session.add(pontuacao)
            db.session.commit()
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
        
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
