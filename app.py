#placeholder Flask application for demonstration purposes
# Routes for index.signup0,login,dashboard, and alogout
#actual logic for each route is not implemented

from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3, hashlib

app = Flask(__name__)
app.secret_key = '24' #change this to a random secret key
db_locate = 'users.db'

@app.route('/')
def index():
    return render_template('Menu.html')

@app.route('/signup', methods= ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        connection = sqlite3.connect (db_locate)
        cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        flash('Signup successful! Please log in.')
        return redirect(url_for('login'))
    except sqlite3.IntegrityError:
        flash('Signup successful! Please log in.')
        return redirect(url_for('signup'))
    finally:
        connection.close()
        return render_template('signup.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        connection = sqlite3.connect(db_locate)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        connection.close()

        if user:
            session['username'] = username 
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route ('/dashboard')
def  dashboard():
    if 'username' not in session:
        flash('Please login first.')
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
