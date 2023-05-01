from flask import Flask, render_template, request
from random import randint
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sdfghjklsjhgfdsdfghjkllkjrghjssxxx356-098765'
toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lucky')
def get_lucky_number():
    number = randint(10, 50)
    return render_template('lucky.html', lucky_number=number)

@app.route('/register', methods=['GET', 'POST'])
def user_registration():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        return {
            'full name': full_name,
            'username': username,
            'email': email,
            'phone': phone,
        }
    return render_template('register.html')
