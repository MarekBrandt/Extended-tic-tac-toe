from dictionaries import field_markings


class Board:
    """Represent a game board"""

    def __init__(self, size):
        """Initialize board which width is size"""
        self.size = size
        self.board = []
        for _ in range(size * size):
            self.board.append(field_markings['empty'])

    def show(self):
        for row in range(self.size):
            row_elements = []
            for column in range(self.size):
                index = row * self.size + column
                row_elements.append(self.board[index])
            row_to_print = ""
            i = 0
            for element in row_elements:
                if element == field_markings.get('empty'):
                    row_to_print += ' '
                elif element == field_markings.get('x'):
                    row_to_print += 'X'
                elif element == field_markings.get('o'):
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


