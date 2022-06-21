from flask import Flask
from game import demo_game

app = Flask(__name__)


@app.route('/')
def hello_world():
    Game = demo_game(3)
    print(Game.show_player())
    return str(Game.show_player())