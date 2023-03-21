from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    manga = ['Shingeki no Kyojin', 'Chainsaw man', 'Goodbye Eri', 'Berserk', 'Horimiya']
    return render_template('favorites.html', manga = manga)