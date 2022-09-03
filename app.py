from flask import Flask, render_template
from game_of_live import GameOfLife


app = Flask(__name__)
width = 50
height = 20
@app.route("/")
def home():
    GameOfLife(width, height)
    return render_template('index.html')

@app.route("/live/")
def live():
    _game = GameOfLife()
    _game.form_new_generation()
    return render_template('live.html', game=_game, width=width, height=height)
