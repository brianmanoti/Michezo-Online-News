from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 
db = SQLAlchemy(app)

class users(db.model):
    id = db.column(db.Integer, primary_key=True)
    
@app.@app.route('/')
def Hello_world():
    return "hello _ there"

if __name__ == '__main__':
    app.run