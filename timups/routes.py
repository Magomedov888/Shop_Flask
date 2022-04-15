from os import rename
from timups import app
from flask import before_render_template, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/watches')
def watches():
    return render_template('watches.html')