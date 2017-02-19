# https://github.com/SunJieMing/python-minicamp-homework-2

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello World'
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'June 6, 1973'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello {}'.format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return str(num1 * num2)

# Flask jsonify: http://flask.pocoo.org/docs/0.12/api/#flask.json.jsonify
@app.route('/fav_foods')
def fav_foods():
    list_of_foods = ['bi bim kook soo',
                     'pizza',
                     'CHAWKLAT!!!!']
    return jsonify(list_of_foods)

# The following allows flask to automatically update changes
if __name__ == '__main__':
    app.run(debug = True)

# Without it, automatic updating can be invoked:
# $ export FLASK_APP=<filename>.py
# $ export FLASK_DEBUG=1
# $ flask run
