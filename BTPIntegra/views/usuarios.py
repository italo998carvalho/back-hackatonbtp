from flask import Blueprint, request, jsonify
from BTPIntegra.models.Usuario import Usuario
from BTPIntegra.views.login import token_required
from BTPIntegra.app import db
from BTPIntegra.config import categoriasAceitas

user = Blueprint('user', __name__)

@user.route('/usuario', methods=['POST', 'GET'])
def usuario():
    data = request.get_json()
    
    if request.method == 'POST':
        nome = data['nome']
        registro = data['registro']
        senha = data['senha']
        funcao = data['funcao']
        categoria = data['categoria']
        dataNascimento = data['dataNascimento']
        sexo = data['sexo']
        fotoPerfil = data['fotoPerfil']

        if categoria not in categoriasAceitas:
            return jsonify({'code': 400, 'body':{'mensagem': 'Categoria inexistente!'}})

        usuario = Usuario(nome, registro, senha, funcao, categoria, dataNascimento, sexo, fotoPerfil)

        try:
            db.session.add(usuario)
            db.session.commit()
            
            return jsonify({'code': 200, 'body': {'mensagem': 'Usuário cadastrado com sucesso!'}})
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
        
    elif request.method == 'GET':
        try:
            dados = Usuario.query.all()

            usuarios = []
            for info in dados:
                usuario = {}
                usuario['id'] = info.id
                usuario['nome'] = info.nome
                usuario['registro'] = info.registro
                usuario['funcao'] = info.funcao
                usuario['categoria'] = info.categoria
                usuario['dataNascimento'] = info.dataNascimento
                usuario['sexo'] = info.sexo
                usuario['fotoPerfil'] = info.fotoPerfil

                usuarios.append(usuario)

            return jsonify({'code': 200, 'body': usuarios})
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

    else:
        return jsonify({'code': 403, 'body': {'mensagem': 'Método inválido!'}}), 403

@user.route('/usuario/<int:id>', methods=['GET'])
@token_required
def oneUsuario(usuarioAtual, id):
    if request.method == 'GET':
        try:
            info = Usuario.query.filter_by(id = id).first()

            usuario = {}
            usuario['id'] = info.id
            usuario['nome'] = info.nome
            usuario['registro'] = info.registro
            usuario['funcao'] = info.funcao
            usuario['categoria'] = info.categoria
            usuario['dataNascimento'] = info.dataNascimento
            usuario['sexo'] = info.sexo
            usuario['fotoPerfil'] = info.fotoPerfil

            return jsonify({'code': 200, 'body': usuario})
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
    
    else:
        return jsonify({'code': 500, 'body': {'mensagem': 'Método inválido!'}}), 500