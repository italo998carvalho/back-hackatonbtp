from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://italo:1234@localhost:5432/hackatonbtp'
db = SQLAlchemy(app)
app.secret_key = '123456789'

@app.route('/')
def index():
    return 'HACKATON BTP'

from BTPIntegra.views.login import auth
app.register_blueprint(auth)

from BTPIntegra.views.usuarios import user
app.register_blueprint(user)