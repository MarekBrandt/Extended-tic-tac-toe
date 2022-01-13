import random

from player import Player
from constants import field_markings
from random import choice


class Computer(Player):
    def __init__(self, team, name):
        super().__init__(team, name)

    def make_move(self, board):
        empty_fields = [x for x, field in enumerate(board.board) if field == field_markings.index("empty")]
        board.change_field(random.choice(empty_fields), self.team)
