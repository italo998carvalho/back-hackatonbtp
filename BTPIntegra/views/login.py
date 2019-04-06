from flask import request, jsonify, Blueprint
from werkzeug.security import check_password_hash
import jwt, datetime
from BTPIntegra.models.Usuario import Usuario
from BTPIntegra.app import app

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print("ajhsdkahkjsdha: " + str(data))

    if not data or not data['registro'] or not data['senha']:
        return jsonify({'code': 400, 'data':{'mensagem': 'Formato da informação inválido!'}})

    registro = Usuario.query.filter_by(registro = data['registro']).first()

    if not registro:
        return jsonify({'code': 201, 'data':{'mensagem': 'Usuário inválido!'}})

    if check_password_hash(registro.senha, data['senha']):
        token = jwt.encode({'id': registro.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 40)}, app.secret_key)
        return jsonify({'code': 200, 'data': {'token': token.decode('UTF-8')}})
    else:
        return jsonify({'code': 201, 'data':{'mensagem': 'Senha inválida!'}})