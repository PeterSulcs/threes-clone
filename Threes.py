__author__ = 'Peter_000'


class Space(object):

    def __init__(self):
        self.value = 0

    def is_empty(self):
        return self.value == 0

    def get_value(self):
        return self.value

    def can_be_combined_with(self, b):
        """
        Can be combined if one of the values is blank
        The sum of the value is 5
        The values are the same.
        """
        if b.is_empty() or b.get_value() + self.get_value() == 5 or b.get_value() == self.get_value():
            return True
        else:
            return False


class Board(object):

    board = List()

    def __init__(self, size=4):

        for row in range(0, size):
            for col in range(0, size):
                newSpace = Space()
                self.rows.append


