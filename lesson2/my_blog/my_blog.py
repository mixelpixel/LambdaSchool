from flask import Flask

app = Flask(__name__)

# routes are the responses to http requests

@app.route('/')
def index():
    # return 'Hello world!'
    return app.send_static_file('home.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

# Writing html into the python file is quickly cumbersome
# Much easier to put .html files in the "status" folder!
@app.route('/something')
def something():
    return '<h1>This is a big h1</h1><p>This is a paragraph</p><h2>This is an h2!</h2>'

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

# using parameter <postnum> instead of a number per post:
@app.route('/post/<postnum>')
# @app.route('/post/<int:postnum>')
def posts(postnum):
    return 'This is post {}'.format(postnum)
