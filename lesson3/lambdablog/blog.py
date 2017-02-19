from flask import Flask, render_template, request
# 'render_template' renders templates and 'request' handles http requests

import sqlite3

app = Flask(__name__)

#connecting application to the database
connection = sqlite3.connect('database.db')
print('Database opened successfully')

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('Table created successfully')
connection.close()

@app.route('/')
def hello_world():
    return "Hello World!"

# Rendering a template:
@app.route('/new')
def new_post():
    return render_template('new.hmtl')

if __name__ == '__main__':
    app.run(debug = True)
