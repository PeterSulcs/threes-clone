__author__ = 'Peter_000'
from random import randint


class Tile(object):
    def __init__(self, value=0, position=(0, 0)):
        self.value = value
        self.row = position[0]
        self.col = position[1]

    def set_position(self, position):
        self.row = position[0]
        self.col = position[1]

    def get_position(self):
        return self.row, self.col

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_value(self):
        return self.value

    def move_right(self):
        self.col += 1

    def move_left(self):
        self.col -= 1

    def move_up(self):
        self.row -= 1

    def move_down(self):
        self.row += 1

    def can_be_combined_with(self, tile):
        """
        Can be combined if one of the values is blank
        The sum of the value is 3
        The values are the same and greater than or equal to 3.
        """
        that_value = tile.get_value()
        this_value = self.get_value()
        if (this_value + that_value == 3) or (this_value == that_value and (this_value >= 3 and that_value >= 3)):
            return True
        else:
            return False
        # else:
        #     return False

    def combine_into(self, tile):
        """
        if can be combined then combine
        """
        if self.can_be_combined_with(tile):
            self.value += tile.get_value()
            self.set_position(tile.get_position())

    def __str__(self):
        if self.value == 0:
            value = ""
        else:
            value = self.value
        return " {0:5s} |".format(str(value))


class Board(object):

    def __init__(self, nrows=4, ncols=4):
        self.nrows = nrows
        self.ncols = ncols
        self.tiles = list()

    def is_full(self):
        if len(self.tiles) >= self.nrows * self.ncols:
            return True
        else:
            return False

    def get_random_col(self):
        return randint(0, self.ncols - 1)

    def get_random_row(self):
        return randint(0, self.nrows - 1)

    def get_tiles_in_row(self, row):
        """
        Return the tiles in the given row from left to right
        """
        tiles = [tile for tile in self.tiles if tile.get_row() == row]
        tiles.sort(key=lambda x: x.get_col())
        return tiles

    def get_tiles_in_col(self, col):
        """
        Return the tiles in the given col from top to bottom
        """
        tiles = [tile for tile in self.tiles if tile.get_col() == col]
        tiles.sort(key=lambda x: x.get_row())
        return tiles

    def get_tile_at(self, row, col):
        tiles_in_row = self.get_tiles_in_row(row)
        match = [tile for tile in tiles_in_row if tile.get_col() == col]
        if match == list():
            return None
        else:
            return match[0]

    def is_space_filled(self, row, col):
        if self.get_tile_at(row, col):
            return True
        else:
            return False

    def add_random_tile(self):
        """
        :type self: Board
        """
        if not self.is_full():
            placed = False
            while not placed:
                row = self.get_random_row()
                col = self.get_random_col()
                if not self.is_space_filled(row, col):
                    self.tiles.append(Tile(value=randint(1, 2), position=(row, col)))
                    placed = True
        pass

    def up(self):
        """
        Shift up
        """
        # iterate through each col
        for n in range(0, self.ncols):
            col = self.get_tiles_in_col(n)
            combine_limit_reached = False
            if col:  # only do something if the row isn't empty
                for tile in col:
                    # start at top most tile
                    # can it move up? if yes, move
                    new_row = tile.get_row() - 1
                    if new_row >= 0:  # is it within the edges of the board
                        tile_at_destination = self.get_tile_at(new_row, n)
                        if not tile_at_destination:  # is the destination empty?
                            tile.move_up()
                        elif tile.can_be_combined_with(
                                tile_at_destination) and not combine_limit_reached:  # if not empty and can be combined, then combine
                            tile.combine_into(tile_at_destination)
                            combine_limit_reached = True
                            assert isinstance(tile, Tile)
                            self.tiles.remove(tile_at_destination)  # trust that tile will be garbage collected.

    def down(self):
        """
        Shift down
        """
        # iterate through each col
        for n in range(0, self.ncols):
            col = self.get_tiles_in_col(n)
            combine_limit_reached = False
            if col:  # only do something if the row isn't empty
                for tile in reversed(col):
                    # start at bottom most tile
                    # can it move down? if yes, move
                    new_row = tile.get_row() + 1
                    if new_row < self.nrows:  # is it within the edges of the board
                        tile_at_destination = self.get_tile_at(new_row, n)
                        if not tile_at_destination:  # is the destination empty?
                            tile.move_down()
                        elif tile.can_be_combined_with(
                                tile_at_destination) and not combine_limit_reached:  # if not empty and can be combined, then combine
                            tile.combine_into(tile_at_destination)
                            combine_limit_reached = True
                            assert isinstance(tile, Tile)
                            self.tiles.remove(tile_at_destination)  # trust that tile will be garbage collected.

    def right(self):
        """
        Shift right
        """
        # iterate through each row
        for n in range(0, self.nrows):
            row = self.get_tiles_in_row(n)
            combine_limit_reached = False
            if row:  # only do something if the row isn't empty
                for tile in reversed(row):
                    # start at right most tile
                    # can it move right? if yes, move
                    new_col = tile.get_col() + 1
                    if new_col < self.ncols:  # is it within the edges of the board
                        tile_at_destination = self.get_tile_at(n, new_col)
                        if not tile_at_destination:  # is the destination empty?
                            tile.move_right()
                        elif tile.can_be_combined_with(
                                tile_at_destination) and not combine_limit_reached:  # if not empty and can be combined, then combine
                            tile.combine_into(tile_at_destination)
                            combine_limit_reached = True
                            assert isinstance(tile, Tile)
                            self.tiles.remove(tile_at_destination)  # trust that tile will be garbage collected.
        pass

    def left(self):
        """
        Shift left
        """
        # iterate through each row
        for n in range(0, self.nrows):
            row = self.get_tiles_in_row(n)
            combine_limit_reached = False
            if row:  # only do something if the row isn't empty
                for tile in row:
                    # start at left most tile
                    # can it move left? if yes, move
                    new_col = tile.get_col() - 1
                    if new_col >= 0:  # is it within the edges of the board
                        tile_at_destination = self.get_tile_at(n, new_col)
                        if not tile_at_destination:  # is the destination empty?
                            tile.move_left()
                        elif tile.can_be_combined_with(
                                tile_at_destination) and not combine_limit_reached:  # if not empty and can be combined, then combine
                            tile.combine_into(tile_at_destination)
                            combine_limit_reached = True
                            self.tiles.remove(tile_at_destination)  # trust that tile will be garbage collected.
        pass

    def print_board(self):
        for n in range(0, self.nrows):
            row = '|'
            for m in range(0, self.ncols):
                match = self.get_tile_at(n, m)
                if match:
                    row += " {0:5s} |".format(str(match.get_value()))
                else:
                    row += " {0:5s} |".format('')
            print row
        print ""


if __name__ == '__main__':
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
        b.print_board()
        a = raw_input("wasd to move, q to quit:")
        if a == 'w':
            b.up()
        elif a == 's':
            b.down()
        elif a == 'a':
            b.left()
        elif a == 'd':
            b.right()



