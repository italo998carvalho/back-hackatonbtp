from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'string de conexão'
db = SQLAlchemy(app)
app.secret_key = '123456789'

@app.route('/')
def index():
    return 'HACKATON BTP'