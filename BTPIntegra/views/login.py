from flask import request, jsonify, Blueprint
from werkzeug.security import check_password_hash
import jwt, datetime
from BTPIntegra.models.Usuario import Usuario
from BTPIntegra.app import app
from functools import wraps

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data['registro'] or not data['senha']:
        return jsonify({'code': 400, 'body':{'mensagem': 'Formato da informação inválido!'}})

    registro = Usuario.query.filter_by(registro = data['registro']).first()

    if not registro:
        return jsonify({'code': 201, 'body':{'mensagem': 'Usuário inválido!'}})

    if check_password_hash(registro.senha, data['senha']):
        token = jwt.encode({'id': registro.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 40)}, app.secret_key)
        return jsonify({'code': 200, 'body': {'token': token.decode('UTF-8')}})
    else:
        return jsonify({'code': 201, 'body':{'mensagem': 'Senha inválida!'}})

def token_required(f):
    @wraps(f)
    def decoreted(*args, **kwargs):
        token = None

        if 'token' in request.headers:
            token = request.headers['token']
        
        if not token:
            return jsonify({'code': 401, 'body':{'mensagem': 'Voce precisa de uma Token para ter acesso!!'}}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            usuarioAtual = Usuario.query.filter_by(id = data['id']).first()
        except:
            return jsonify({'code': 401, 'body':{'mensagem': 'Token invalida!'}}), 401
        
        return f(usuarioAtual, *args, **kwargs)
    
    return decoreted