from flask import Blueprint, request, jsonify
from BTPIntegra.models.Usuario import Usuario
from BTPIntegra.app import db

user = Blueprint('user', __name__)

@user.route('/usuario', methods=['POST', 'GET'])
def usuario():
    data = request.get_json()
    
    if request.method == 'POST':
        nome = data['nome']
        registro = data['registro']
        senha = data['senha']

        usuario = Usuario(nome, registro, senha)

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

                usuarios.append(usuario)

            return jsonify({'code': 200, 'body': usuarios})
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

    else:
        return jsonify({'code': 403, 'body': {'mensagem': 'Método inválido!'}}), 403

@user.route('/usuario/<int:id>', methods=['GET'])
def oneUsuario(id):
    if request.method == 'GET':
        try:
            info = Usuario.query.filter_by(id = id).first()

            usuario = {}
            usuario['id'] = info.id
            usuario['nome'] = info.nome
            usuario['registro'] = info.registro

            return jsonify({'code': 200, 'body': usuario})
        except:
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
    
    else:
        return jsonify({'code': 500, 'body': {'mensagem': 'Método inválido!'}}), 500