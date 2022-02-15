import sys

import constants
import pygame as pg
import interface


class Player:
    """Represents a player"""

    def __init__(self, team, name):
        self.team = team
        self.name = name

    def make_move(self, board):
        clock = pg.time.Clock()
        run = True
        click = False
        ret_value = True
        interface.act_on_message("your turn", board, self)
        while run:
            pos = pg.mouse.get_pos()
            if click:
                for i, rect in enumerate(board.rectangles):
                    if rect.collidepoint(pos):
                        if board.board_list[i] != constants.field_markings.index("empty"):
                            interface.act_on_message("non-existing field", board, self)
                        else:
                            board.change_field(i, self.team)
                            run = False
            click = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        ret_value = False
                        run = False
            clock.tick(constants.FPS)


            """index = interface.act_on_message("choose field", board, self)
            try:
                index = int(index)

                if index < 1 or index > board.size ** 2:
                    interface.act_on_message("non-existing field", board, self)
                else:
                    index = index - 1  # now index is starting from 0
                    if board.board_list[index] != field_markings.index("empty"):
                        interface.act_on_message("occupied field", board, self)
                    else:
                        board.change_field(index, self.team)
                        run = False
            except ValueError:
                interface.act_on_message("value error", board, self)
"""
        return ret_value

    def make_move2(self, board):
        return self.make_move(board)
