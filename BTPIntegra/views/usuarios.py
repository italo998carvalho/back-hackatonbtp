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
            
            return jsonify({'code': 200, 'data': {'mensagem': 'Usuário cadastrado com sucesso!'}})
        except:
            return jsonify({'code': 500, 'data': {'mensagem': 'Erro interno!'}})
        
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

            return jsonify({'code': 200, 'data': usuarios})
        except:
            return jsonify({'code': 500, 'data': {'mensagem': 'Erro interno!'}})

    else:
        return jsonify({'code': 403, 'data': {'mensagem': 'Método inválido!'}})

@user.route('/usuario/<int:id>', methods=['GET'])
def oneUsuario(id):
    if request.method == 'GET':
        try:
            info = Usuario.query.filter_by(id = id).first()

            usuario = {}
            usuario['id'] = info.id
            usuario['nome'] = info.nome
            usuario['registro'] = info.registro

            return jsonify({'code': 200, 'data': usuario})
        except:
            return jsonify({'code': 500, 'data': {'mensagem': 'Erro interno!'}})
    
    else:
        return jsonify({'code': 500, 'data': {'mensagem': 'Método inválido!'}})