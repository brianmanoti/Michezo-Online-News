from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['sqlalchemy database uri'] = 'ourdatabase'
db = SQLAlchemy(app)
Login_manager = LoginManager(app)