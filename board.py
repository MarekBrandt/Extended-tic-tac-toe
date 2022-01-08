from constants import field_markings


class Board:
    """Represent a game board"""

    def __init__(self, size):
        """Initialize board which width is size"""
        self.size = size
        self.board = []
        for _ in range(size * size):
            self.board.append(field_markings.index('empty'))

    def show(self):
        """
        line = ""
        line2 = ""
        for i in range(self.size):
            line += "___"
            line2 += "---"
        print(line)
        attempt to add frame to board"""
        for row in range(self.size):
            row_elements = []
            for column in range(self.size):
                index = row * self.size + column
                row_elements.append(self.board[index])
            row_to_print = ""
            i = 0
            for element in row_elements:
                if element == field_markings.index('empty'):
                    row_to_print += ' '
                elif element == field_markings.index('x'):
                    row_to_print += 'X'
                elif element == field_markings.index('o'):
                    row_to_print += 'O'

                # adding | after every element except the last one
                if i != len(row_elements)-1:
                    row_to_print += ' | '
                i += 1
            print(row_to_print)
        row_to_print = ''
        print(row_to_print)
        for _ in range(self.size + (self.size-1)*3):
            row_to_print += '='
        print(row_to_print)
        row_to_print = ''
        print(row_to_print)

    def change_field(self, index, marking):
        self.board[index] = field_markings.index(marking)

    def is_not_full(self):
        if field_markings.index("empty") not in self.board:
            return False
        else:
            return True

    def is_victory(self, symbol, win_cond):
        numb_of_marking = field_markings.index(symbol)

        if self.horizontal_win(numb_of_marking, win_cond) \
                or self.vertical_win(numb_of_marking, win_cond) \
                or self.l_diagonal_win(numb_of_marking, win_cond):
            win = True
        else:
            win = False

        return win

    def horizontal_win(self, numb_of_marking, win_cond):
        # checking for the horizontal victory,
        # numb_of_marking is index of symbol in constants.py
        win = False
        for row in range(self.size):
            counter = 0
            for column in range(self.size):
                if counter == win_cond:  # victory
                    break
                index = row * self.size + column
                if self.board[index] == numb_of_marking:
                    counter += 1
                else:
                    counter = 0
            if counter == win_cond:
                win = True
                break
        return win

    def vertical_win(self, numb_of_marking, win_cond):
        # checking for the vertical victory,
        # numb_of_marking is index of symbol in constants.py
        win = False
        for column in range(self.size):
            counter = 0
            for row in range(self.size):
                if counter == win_cond:  # victory
                    break
                index = row * self.size + column
                if self.board[index] == numb_of_marking:
                    counter += 1
                else:
                    counter = 0
            if counter == win_cond:
                win = True
                break
        return win

    def l_diagonal_win(self, numb_of_marking, win_cond):
        # checking for the diagonal tilted to left (\) victory,
        # numb_of_marking is index of symbol in constants.py
        # i divide problem on two smaller.
        # first: under main diagonal, including it
        # second: above main diagonal, not including it
        win = False

        # first problem solution
        row = self.size-1
        while row >= 0:
            counter = 0
            for column in range(self.size - row):
                if counter == win_cond:  # victory
                    break
                index = (row + column) * self.size + column
                if self.board[index] == numb_of_marking:
                    counter += 1
                else:
                    counter = 0
            if counter == win_cond:
                win = True
                break
            row -= 1

        # second problem solution
        # to check, not working
        if not win:
            first_row = 0
            first_column = 1
            for i in range(self.size-1):
                counter = 0
                for column in range(self.size-1 - i):
                    if counter == win_cond:  # victory
                        break
                    index = (first_row + column) * self.size + first_column + i + column
                    if self.board[index] == numb_of_marking:
                        counter += 1
                    else:
                        counter = 0
                if counter == win_cond:
                    win = True
                    break
        return win
