from flask import request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User  # Import your User model from the correct location
from app import app, db, bcrypt
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
            'player_count': len(team.players)
        }
        team_info.append(team_data)
    return team_info

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))  # Replace 'index' with your desired route after login
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))  # Replace 'index' with your desired route after logout

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')
@app.route('/players')
def display_players():
    team_name = request.args.get('team_name')  # Get the team_name from the URL parameter
    players = get_players_by_team(team_name)
    return render_template('players_template.html', players=players)

@app.route('/teams')
def display_teams():
    team_info = get_team_info()
    return render_template('teams_template.html', teams=team_info)

if __name__ == '__main__':
    app.run(debug=True)