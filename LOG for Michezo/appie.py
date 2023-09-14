from flask import request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import User 
from app import app, db, bcrypt
import mysql.connector
from app.models.player import Player
from app.models.team import Team
from app.models.user import User


# Sample function to retrieve all players or players from a specific team
def get_players_by_team(team_name=None):
    if team_name:
        players = Player.query.filter_by(team_name=team_name).all()
    else:
        players = Player.query.all()
    return players

# Sample function to retrieve team information and player count
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))  # Replace 'index' with your desired route after logout
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        result = cursor.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            user_data = cursor.fetchone()
            user = User(user_data[0], user_data[1], user_data[2])

            if bcrypt.check_password_hash(user.password, password):
                session['user_id'] = user.id
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password!', 'danger')
        else:
            flash('Invalid username or password!', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                       (username, hashed_password))
        mysql.connection.commit()
        cursor.close()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/')
def show_news():
    return render_template('home.html')

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

if __name__ == '__main__':
    app.run(debug=True)