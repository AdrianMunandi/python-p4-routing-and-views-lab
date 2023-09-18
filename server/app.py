#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    # Print the string to the console
    print(param)
    # Display the string in the web browser
    return param

@app.route('/count/<int:param>')
def count(param):
    # Generate a list of numbers in the range of the parameter
    numbers = '\n'.join(str(i) for i in range(param + 1))
    # Display the numbers on separate lines
    return numbers

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    # Perform the appropriate operation based on the operator
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return 'Error: Modulo by zero'
    else:
        return 'Error: Invalid operation'

    # Display the result
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
