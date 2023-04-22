''' Build a simple calculator with Flask, which uses URL query parameters 
to get the numbers to calculate with.
'''
from flask import Flask, request

app = Flask(__name__)

@app.get('/')
def home():
    return { 'success': 'Weclcome to do_calc application. The home of basic mathematical calculations' }

@app.route('/add', methods=['POST', 'GET'])
def addition():
    """Add a and b."""
    if request.method == 'POST':
        number_a = request.form['first_number']
        number_b = request.form['second_number']
        result =  int(number_a) + int(number_b)
        return { 'result': result }
    return '''
        <h3> Add two numbers </h3>
        <form method='POST'>
            <input type="number" required name="first_number"/>
            <input type="number" required name="second_number"/>
            <button> Calculate Now! </button>
    '''

@app.route('/sub', methods=['POST', 'GET'])
def subtraction():
    """Subtract a and b."""
    if request.method == 'POST':
        number_a = request.form['first_number']
        number_b = request.form['second_number']
        result =  int(number_a) - int(number_b)
        return { 'result': result }
    return '''
        <h3> Subtract two numbers </h3>
        <form method='POST'>
            <input type="number" required name="first_number"/>
            <input type="number" required name="second_number"/>
            <button> Calculate Now! </button>
    '''

@app.route('/multiply', methods=['POST', 'GET'])
def multiply():
    """Multiply a and b."""
    if request.method == 'POST':
        number_a = request.form['first_number']
        number_b = request.form['second_number']
        result =  int(number_a) * int(number_b)
        return { 'result': result }
    return '''
        <h3> Multiply two numbers </h3>
        <form method='POST'>
            <input type="number" required name="first_number"/>
            <input type="number" required name="second_number"/>
            <button> Calculate Now! </button>
    '''

@app.route('/devide', methods=['POST', 'GET'])
def division():
    """Devide a and b."""
    if request.method == 'POST':
        number_a = request.form['first_number']
        number_b = request.form['second_number']
        result =  int(number_a) / int(number_b)
        return { 'result': result }
    return '''
        <h3> Devide two numbers </h3>
        <form method='POST'>
            <input type="number" required name="first_number"/>
            <input type="number" required name="second_number"/>
            <button> Calculate Now! </button>
    '''