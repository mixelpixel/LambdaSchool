# https://github.com/SunJieMing/python-minicamp-homework-3

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')




@app.route('/search', methods = ['GET'])
def search():
    # connection = sqlite3.connect('database.db')
    # # cursor lets us write in the database
    # cursor = connection.cursor()
    #
    # try:
    #     title = request.form['title']
    #     post = request.form['post']
    #     cursor.execute('INSERT INTO posts (title,post) VALUES (?,?)', (title,post))
    #     connection.commit()
    #     message = "Record successfuly added"
    # except:
    #     connection.rollback()
    #     message = "error in insert operation"
    # finally:
    #     return render_template('result.html', message = message)
    #     connection.close()
    return

if __name__ == '__main__':
    app.run(debug = True)
