__author__ = 'Peter_000'


class Space(object):

    def __init__(self, value=0):
        self.value = value

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

    def __str__(self):
        if self.value == 0:
            value = ""
        else:
            value = self.value
        return " {0:5s} |".format(str(value))


class Board(object):

    def __init__(self, nrows=4, ncols=4):
        self.rows = [[Space(x) for x in range(0, ncols)] for y in range(0, nrows)]
        self.cols = [[self.rows[n][m] for n in range(0, ncols)] for m in range(0, ncols)]

    def up(self):
        '''
        Shift up
        '''
        pass

    def down(self):
        '''
        Shift down
        '''
        pass

    def right(self):
        '''
        Shift right
        '''
        # iterate through each row
        for row in self.rows:
            # starting from right look pairwise for potential to combine
            for (left, right) in zip(row[0:-2], row[1:-1]):

        # only combine one pair per row
        pass

    def left(self):
        '''
        Shift left
        '''
        pass

    def print_using_rows(self):
        for row in self.rows:
            print "|" + "".join([str(e) for e in row])

    def print_using_cols(self):
        for n in range(0, len(self.rows)):
            print "|" + "".join([str(self.cols[m][n]) for m in range(0, len(self.cols))])


if __name__ == '__main__':
    b = Board(4, 4)
    b.print_using_rows()
    print ""
    b.print_using_cols()



