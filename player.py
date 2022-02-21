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
        while run:
            pos = pg.mouse.get_pos()
            if click:
                for i, rect in enumerate(board.rectangles):
                    if rect.collidepoint(pos):
                        if board.board_list[i] != constants.field_markings.index("empty"):
                            interface.board_message = "This field is occupied"
                            board.show()
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

        return ret_value

    # make_move2 is different only for AI
    def make_move2(self, board):
        return self.make_move(board)
