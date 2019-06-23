import os
from flask import Flask, render_template, request, url_for, redirect, session

# create an instance of Flask
app = Flask(__name__)

# before deploying convert to enviroment variable
app.secret_key = "randomString123"


# landing page for the website for new users. 
@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session["username"] = request.form["username"]

    # if the cookie for the user already exist the login page is skipped
    if "username" in session:
        return redirect(url_for('get_recipies'))
    
    return render_template('login.html')

def getusername():
    username = session['username']
    return username

@app.route('/get_recipies')
def get_recipies():
    username = getusername()
    return render_template('get_recipies.html', username=username)

# https://www.tutorialspoint.com/flask/flask_sessions.htm
@app.route('/logout')
def logout():
 # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')))
