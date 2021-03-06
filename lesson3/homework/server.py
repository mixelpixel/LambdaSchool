# https://github.com/SunJieMing/python-minicamp-homework-3

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        name           = request.form['name']
        calories       = request.form['calories']
        cuisine        = request.form['cuisine']
        is_vegetarian  = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']
        cursor.execute('INSERT INTO foods (name,calories,cuisine,\
                                           is_vegetarian,is_gluten_free) \
                        VALUES (?,?,?,?,?)',(name,calories,cuisine,\
                                             is_vegetarian,is_gluten_free))
        connection.commit()
        message = "Yum! Food successfuly added"
    except:
        connection.rollback()
        message = "Barf! Error w/food insertion operation"
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
    	cursor.execute('SELECT * FROM foods Where name="mango"')
    	connection.commit()
    	fav = cursor.fetchone()
    except:
    	fav = ('Did you forget to add mango?')
    finally:
    	return jsonify(fav)
    	connection.close()

@app.route('/search', methods = ['GET'])
def search():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM foods Where name=?', name)
        connection.commit()
        search_result = cursor.fetchone()
    except:
        search_result = ('what the effing eff?')
    finally:
        return jsonify(search_result)
        connection.close()


@app.route('/drop')
def drop():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        cursor.execute('DROP TABLE foods')
        connection.commit()
        drop_result = ('You dropped the table!')
    except:
        connection.rollback()
        drop_result = ('Did you DROP the ball?')
    finally:
        return render_template('result.html', message = drop_result)
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
