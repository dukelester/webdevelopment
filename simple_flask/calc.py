''' Build a simple calculator with Flask, which uses URL query parameters 
to get the numbers to calculate with.
'''
from flask import Flask, request
import operator

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

@app.route('/math/<oper>')
def do_calculation(oper):
    """ Do the calculation """
    result = 0
    number_1 = request.args.get('num1')
    number_2 = request.args.get('num2')
    print(number_2, number_1)
    if oper == 'add':
        result = operator.add(int(number_1), int(number_2))
        print(result)
    elif oper == 'sub':
        result = operator.sub(int(number_1), int(number_2))
        print(result)
    elif oper == 'mul':
        result = operator.mul(int(number_1), int(number_2))
        print(result)
    elif oper == 'div':
        result = operator.floordiv(int(number_1), int(number_2))
        print(result)
    elif oper == 'mod':
        result = operator.mod(int(number_1), int(number_2))
        print(result)
    else:
        return 'invalid operation'
    return str(result)
    