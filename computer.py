import random
import copy
from board import Board

from player import Player
from constants import field_markings
from random import choice


class Computer(Player):
    def __init__(self, team, name):
        super().__init__(team, name)

    def make_move(self, board):
        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]

        if self.team == 'o':
            comp_team = 'o'
            player_team = 'x'
        else:
            comp_team = 'x'
            player_team = 'o'
        # checking if there is a chance to win with one move
        # if not, checking if opponent can win with one move, and blocks it
        for symbol in [comp_team, player_team]:
            for field in empty_fields:
                board_copy = Board(board.size, board.win_cond)
                board_copy.board_list = board.board_list[:]

                board_copy.change_field(field, symbol)
                # todo change win_condition to load from game somehow
                if board_copy.is_victory(symbol):
                    board.change_field(field, self.team)
                    return

                del board_copy

        board.change_field(random.choice(empty_fields), self.team)
