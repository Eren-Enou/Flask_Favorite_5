from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    test = ['1', '2', '3', '4', '5']
    return render_template('favorites.html', test = test)