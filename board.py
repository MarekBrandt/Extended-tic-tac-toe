import random

import interface
from constants import field_markings, COLORS
from constants import WIDTH
from constants import HEIGHT
from interface import board_message
import pygame as pg


class Board:
    """Represent a game board"""

    def __init__(self, size, in_line):
        """Initialize board which width is size"""
        self.size = size
        self.win_cond = in_line
        self.board_list = []
        for _ in range(size * size):
            self.board_list.append(field_markings.index('empty'))



        # only fraction of height, cause top of the screen is place to show messages
        HEIGHT2 = 0.9 * HEIGHT
        board_width = 0.8 * min(WIDTH, HEIGHT2)
        tile_gap_size = board_width / self.size  # how big can be tile with gap alongside
        tile_size = 4 / 5 * tile_gap_size
        gap_size = tile_gap_size - tile_size
        self.rectangles = []

        x_offset = WIDTH / 2 - board_width / 2
        y_offset = -HEIGHT2 / 2 - board_width / 2 + HEIGHT

        for i in range(self.size):
            for j in range(self.size):
                self.rectangles.append(pg.Rect(x_offset + j * tile_gap_size + gap_size / 2,
                                               y_offset + i * tile_gap_size + gap_size / 2,
                                               tile_size, tile_size))
        message_width = 0.9 * WIDTH
        message_height = HEIGHT - HEIGHT2
        message_x = WIDTH/2 - message_width/2
        message_y = 0
        self.message_box = pg.Rect(message_x, message_y, message_width, message_height)

    def show(self, WIN):
        WIN.fill(COLORS['black'])
        font = pg.font.Font(None, int(400 / self.size))
        font2 = pg.font.Font(None, 50)
        color = pg.Color(COLORS['white'])

        message = font2.render(interface.board_message, True, COLORS['yellow'])
        text_width = message.get_width()
        text_height = message.get_height()
        text_x = self.message_box.width / 2 - text_width / 2 + self.message_box.x
        text_y = self.message_box.height / 2 + self.message_box.y

        # pg.draw.rect(WIN, color, (text_x, text_y, text_width, text_height))
        WIN.blit(message, (text_x, text_y, text_width, text_height))

        for row in range(self.size):
            for column in range(self.size):
                text = font.render("", True, (0, 0, 0))
                index = row * self.size + column
                pg.draw.rect(WIN, color, self.rectangles[index])
                if self.board_list[index] == field_markings.index('x'):
                    text = font.render("X", True, (0, 0, 0))
                elif self.board_list[index] == field_markings.index('o'):
                    text = font.render("O", True, (0, 0, 0))

                text_width = text.get_width()
                text_height = text.get_height()
                text_x = self.rectangles[index].width / 2 - text_width / 2
                text_y = self.rectangles[index].height / 2 - text_height / 2

                WIN.blit(text, (self.rectangles[index].x + text_x, self.rectangles[index].y + text_y))
        pg.display.update()

        """for row in range(self.size):
            row_elements = []
            for column in range(self.size):
                index = row * self.size + column
                row_elements.append(self.board_list[index])
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
                if i != len(row_elements) - 1:
                    row_to_print += ' | '
                i += 1
            print(row_to_print)
        row_to_print = ''
        print(row_to_print)
        for _ in range(self.size + (self.size - 1) * 3):
            row_to_print += '='
        print(row_to_print)
        row_to_print = ''
        print(row_to_print)"""

    def change_field(self, index, marking):
        self.board_list[index] = field_markings.index(marking)

    def is_not_full(self):
        if field_markings.index("empty") not in self.board_list:
            return False
        else:
            return True

    # symbol is "x" or "o"
    # returns 0 for tie, 1 for x victory and 2 for o victory
    def is_victory(self):
        for k, symbol in enumerate(['x', 'o']):
            numb_of_marking = field_markings.index(symbol)

            if self.horizontal_win(numb_of_marking) \
                    or self.vertical_win(numb_of_marking) \
                    or self.l_diagonal_win(numb_of_marking) \
                    or self.r_diagonal_win(numb_of_marking):
                win = True
            else:
                win = False

            if win:
                return k + 1
        # is full == tie
        if not self.is_not_full():
            return 0

    def is_victory2(self, symbol):
        numb_of_marking = field_markings.index(symbol)

        if self.horizontal_win(numb_of_marking) \
                or self.vertical_win(numb_of_marking) \
                or self.l_diagonal_win(numb_of_marking) \
                or self.r_diagonal_win(numb_of_marking):
            win = True
        else:
            win = False

        return win

    def horizontal_win(self, numb_of_marking):
        # checking for the horizontal victory,
        # numb_of_marking is index of symbol in constants.py
        win = False
        for row in range(self.size):
            counter = 0
            for column in range(self.size):
                if counter == self.win_cond:  # victory
                    break
                index = row * self.size + column
                if self.board_list[index] == numb_of_marking:
                    counter += 1
                else:
                    counter = 0
            if counter == self.win_cond:
                win = True
                break
        return win

    def vertical_win(self, numb_of_marking):
        # checking for the vertical victory,
        # numb_of_marking is index of symbol in constants.py
        win = False
        for column in range(self.size):
            counter = 0
            for row in range(self.size):
                if counter == self.win_cond:  # victory
                    break
                index = row * self.size + column
                if self.board_list[index] == numb_of_marking:
                    counter += 1
                else:
                    counter = 0
            if counter == self.win_cond:
                win = True
                break
        return win

    def l_diagonal_win(self, numb_of_marking):
        # checking for the diagonal tilted to left (\) victory,
        # numb_of_marking is index of symbol in constants.py
        # i divide problem on two smaller.
        # first: under main diagonal, including it
        # second: above main diagonal, not including it
        win = False

        # first problem solution
        row = self.size - 1
        while row >= 0:
            counter = 0
            for column in range(self.size - row):
                if counter == self.win_cond:  # victory
                    break
                index = (row + column) * self.size + column
                if self.board_list[index] == numb_of_marking:
                    counter += 1
                else:
                    counter = 0
            if counter == self.win_cond:
                win = True
                break
            row -= 1

        # second problem solution
        # to check, not working
        if not win:
            first_row = 0
            first_column = 1
            for i in range(self.size - 1):
                counter = 0
                for column in range(self.size - 1 - i):
                    if counter == self.win_cond:  # victory
                        break
                    index = (first_row + column) * self.size + first_column + i + column
                    if self.board_list[index] == numb_of_marking:
                        counter += 1
                    else:
                        counter = 0
                if counter == self.win_cond:
                    win = True
                    break
        return win

    def r_diagonal_win(self, numb_of_marking):
        # checking for the diagonal tilted to right (/) victory,
        # numb_of_marking is index of symbol in constants.py
        # i divide problem on two smaller.
        # first: under main diagonal, including it
        # second: above main diagonal, not including it
        win = False

        # for upper from main diagonal, including it
        for diagonal in range(self.size):
            counter = 0
            for field in range(diagonal + 1):
                if counter == self.win_cond:  # victory
                    break
                index = (diagonal - field) * self.size + field
                if self.board_list[index] == numb_of_marking:
                    counter += 1
                else:
                    counter = 0
            if counter == self.win_cond:
                win = True
                break

        # for below main diagonal
        if not win:
            starting_row = self.size - 1
            for diagonal in range(self.size - 1):
                counter = 0
                for field in range(starting_row - diagonal):
                    if counter == self.win_cond:  # victory
                        break
                    index = (starting_row - field) * self.size + diagonal + 1 + field
                    if self.board_list[index] == numb_of_marking:
                        counter += 1
                    else:
                        counter = 0
                if counter == self.win_cond:
                    win = True
                    break

        return win
