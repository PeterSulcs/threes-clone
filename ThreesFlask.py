__author__ = 'Peter_000'
from Threes import Board, create_board_from_json
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/move/right', methods=['POST'])
def move_right():
    board = create_board_from_json(request.data)
    board.right()
    return jsonify(board.to_json())

@app.route('/move/left', methods=['POST'])
def move_left():
    board = create_board_from_json(request.data)
    board.left()
    return jsonify(board.to_json())

@app.route('/move/up', methods=['POST'])
def move_up():
    board = create_board_from_json(request.data)
    board.up()
    return jsonify(board.to_json())

@app.route('/move/down', methods=['POST'])
def move_down():
    '''
    Each movement must post the board state to be mutated such that
    web service is stateless.
    '''
    # need to grab board state from POST request
    board = create_board_from_json(request.data)
    board.down()
    return jsonify(board.to_json())

@app.route('/new')
def new_board():
    board = get_new_board()
    return jsonify(board.to_json())

def get_new_board(nrows=4, ncols=4):
    b = Board(nrows, ncols)
    b.add_random_tile()
    b.add_random_tile()
    b.add_random_tile()
    return b

if __name__ == '__main__':
    app.run()