import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

db_config = {
    'host': 'your_mysql_host',
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'database': 'your_mysql_database'
}

@app.route('/')
def method_name():
    return render_template('index.html')

@app.route('/News')
def show_news():
    return render_template('news.html')


@app.route('/players')
def display_players():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT jersey, name, age, height, nationality, strong_foot FROM players")
    info = cursor.fetchall()

    conn.close()

    return render_template('Team.html', info=info)

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


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run