__author__ = 'Peter_000'

import requests
import json

board = requests.get('http://127.0.0.1:5000/new')
print board.json()

next_turn = requests.post('http://127.0.0.1:5000/move/down', data=json.dumps(json.loads(board.content)))
print next_turn.json()

next_turn = requests.post('http://127.0.0.1:5000/move/up',
                          data=json.dumps(json.loads(next_turn.content)))
print next_turn.json()

next_turn = requests.post('http://127.0.0.1:5000/move/right',
                          data=json.dumps(json.loads(next_turn.content)))
print next_turn.json()

next_turn = requests.post('http://127.0.0.1:5000/move/left',
                          data=json.dumps(json.loads(next_turn.content)))
print next_turn.json()