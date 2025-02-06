from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'  # Set the secret key

db = SQLAlchemy(app)

from . import routes, models

with app.app_context():
    db.create_all()
