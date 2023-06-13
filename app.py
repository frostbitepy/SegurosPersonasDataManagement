from flask import Flask
from flask import  render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greetings/')
@app.route('/greetings/<name>')
def greetings(name=None):
    return render_template('greetings.html', name=name)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/loadfile')
def loadfile():
    return render_template('loadfile.html')