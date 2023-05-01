import os
import services
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

BASE_DIR = os.path.dirname(__file__)
app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=f'sqlite:///{BASE_DIR}/db.sqlite3',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)
metadata = MetaData(naming_convention=services.CONVENTION)
db = SQLAlchemy(app, metadata=metadata)
Migrate(app, db, render_as_batch=True)
CORS(app, resources={r'*': {'origins': 'http://localhost:5173'}})


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(30), index=True, nullable=False)


@app.get('/')
def home():
    return 'Hello'


@app.post('/test')
def test():
    return jsonify({'test': 'test'})
