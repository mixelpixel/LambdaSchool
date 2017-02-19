from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('Database opened successfully')

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('Table created successfully')
connection.close()

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/new')
def new_post():
    return render_template('new.hmtl')
