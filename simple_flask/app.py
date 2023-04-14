from flask import Flask

app = Flask(__name__)
print('Welcome to the simple flask application...')

@app.get('/')
def index_page():
    return ' Welcome to the index page !'