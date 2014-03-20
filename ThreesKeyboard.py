__author__ = 'Peter_000'

import msvcrt
import os

from Threes import Board


b = Board(4, 4)
b.add_random_tile()
#b.print_board()
b.add_random_tile()
b.add_random_tile()
b.add_random_tile()
b.add_random_tile()
b.add_random_tile()
#b.print_board()
b.add_random_tile()

a = ''
while not a == 'q':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" --- Threes Clone --- ")
    b.print_board()
    print("wasd to move, q to quit:")
    a = msvcrt.getch()
    if a == 'w':
        b.up()
    elif a == 's':
        b.down()
    elif a == 'a':
        b.left()
    elif a == 'd':
        b.right()



