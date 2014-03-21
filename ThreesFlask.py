__author__ = 'Peter_000'
from Threes import Board
from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def board_state():
    return json.dumps(board.to_json())

@app.route('/move/right')
def move_right():
    board.right()
    return json.dumps(board.to_json())

@app.route('/move/left')
def move_left():
    board.left()
    return json.dumps(board.to_json())

@app.route('/move/up')
def move_up():
    board.up()
    return json.dumps(board.to_json())

@app.route('/move/down')
def move_down():
    board.down()
    return json.dump(board.to_json())

@app.route('/new')
def new_board():
    # TODO: this does not actually change the board beyond json returned
    board = get_new_board()
    return json.dumps(board.to_json())

def get_new_board(nrows=4, ncols=4):
    b = Board(nrows, ncols)
    b.add_random_tile()
    b.add_random_tile()
    b.add_random_tile()
    return b

if __name__ == '__main__':
    board = get_new_board()
    app.run()