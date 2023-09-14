import db as db
import flask as flask
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_bcrypt import Bcrypt

# Initialize Flask app
app = Flask(__name__)

flask db init  
flask db migrate -m "Initial migration"  
flask db upgrade

# Configure app
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'  # Replace with your MySQL connection details
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

# Define your other database models (Player, Team) here

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def show_news():
    return render_template('home.html')

# Define login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Replace 'dashboard' with your desired route after login
        else:
            flash('Invalid username or password!', 'danger')

    return render_template('login.html')

# Define registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, password=hashed_password)
            db.session.add(user)
            db.session.commit()

            login_user(user)
            flash('Registration successful. You are now logged in.', 'success')
            return redirect(url_for('dashboard'))  # Replace 'dashboard' with your desired route after registration

    return render_template('register.html')

# Define other routes and functions (get_players_by_team, get_team_info, etc.) as needed
@app.route('/news')
def show_news():
    return render_template('news.html')

@app.route('/players')
def display_players():
    team_name = request.args.get('team_name')  # Get the team_name from the URL parameter
    players = get_players_by_team(team_name)
    return render_template('players_template.html', players=players)

@app.route('/teams')
def display_teams():
    team_info = get_team_info()
    return render_template('teams.html', teams=team_info)


# Functions to retrive specific data from the database
def get_players_by_team(team_name=None):
    if team_name:
        players = Player.query.filter_by(team_name=team_name).all()
    else:
        players = Player.query.all()
    return players

def get_team_info():
    teams = Team.query.all()
    team_info = []
    for team in teams:
        team_data = {
            'team_name': team.team_name,
            'nick_name': team.nick_name,
            'stadium': team.stadium,
            'city': team.city,
            'coach': team.coach,
            'player_count': len(team.players)
        }
        team_info.append(team_data)
    return team_info


if __name__ == '__main__':
    app.run(debug=True)
