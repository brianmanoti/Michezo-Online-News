from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(index.html)


if __name__ == '__main__':
    app.run