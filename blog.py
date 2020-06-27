from flask import Flask,render_template, request, session,flash, redirect, url_for,g
import sqlite3

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'

SECRET_KEY = 'hard_to_guess'
#creates instance of Flask object and points to app variable
app = Flask(__name__)

#pulls in app configuration by looking for UPERCASE variables
app.config.from_object(__name__)


#function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    status_code =200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Username or Password. Please Try again'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html',error=error) , status_code
@app.route('/main')
def main():
    return render_template('main.html')
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were looged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug =True)
