# https://github.com/SunJieMing/python-minicamp-homework-3

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods = {'POST'})
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        is_vegetarian = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']
        cursor.execute('INSERT INTO foods (name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?,?,?,?,?)',(name,calories,cuisine,is_vegetarian,is_gluten_free))
        connection.commit()
        message = "Yum! Food successfuly added"
    except:
        connection.rollback()
        message = "Barf! Error with food insertion operation"
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/search', methods = ['GET'])
def search():
    return

if __name__ == '__main__':
    app.run(debug=True)
