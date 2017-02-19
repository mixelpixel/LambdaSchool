# https://github.com/SunJieMing/python-minicamp-homework-2

from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug = True)
