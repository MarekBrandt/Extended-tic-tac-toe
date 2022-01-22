import math
import random
from board import Board

from player import Player
from constants import field_markings


class Computer(Player):
    def __init__(self, team):
        super().__init__(team, "Computer")

    scores = {
        "x": 1,
        "o": -1,
        "tie": 0
    }

    def minimax(self, board, depth, is_maximising):
        if self.team == 'o':
            comp_team = 'o'
            player_team = 'x'
        else:
            comp_team = 'x'
            player_team = 'o'
        # check if one of the players is winning
        if is_maximising and board.is_victory(comp_team):
            score = 1
        elif not is_maximising and board.is_victory(player_team):
            score = -1
        return score

    def make_move2(self, board):
        best_score = -math.inf
        best_move = 0
        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]
        for field in empty_fields:
            board.change_field(field, self.team)
            score = self.minimax(board,self.team, 0, False)
            board.change_field(field, 'empty')
            if score > best_score:
                best_score = score
                best_move = field
        board.change_field(best_move, self.team)

    def make_move(self, board):
        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]
        # print("fields that are empty")
        # print(empty_fields)
        if self.team == 'o':
            comp_team = 'o'
            player_team = 'x'
        else:
            comp_team = 'x'
            player_team = 'o'
        # checking if there is a chance to win with one move
        # if not, checking if opponent can win with one move, and blocks it
        for symbol in [comp_team, player_team]:
            winning_fields = []
            for field in empty_fields:
                board_copy = Board(board.size, board.win_cond)
                board_copy.board_list = board.board_list[:]

                board_copy.change_field(field, symbol)
                if board_copy.is_victory() == field_markings.index(symbol):
                    winning_fields.append(field)

                del board_copy
            if winning_fields:
                # print("winning fields for "+symbol)
                # print(winning_fields)
                board.change_field(random.choice(winning_fields), self.team)
                return

        # checking if there is a chance to win with two moves
        # if not, checking if opponent can win with two moves, and blocks it
        # it takes all possibilities, and randomly choose one
        for symbol in [comp_team, player_team]:
            good_fields = []
            # to optimize it uses empty fields without first
            empty_fields2 = empty_fields[1:]
            # and that one empty fields without last
            empty_fields3 = empty_fields[:-1]
            for first_field in empty_fields3:
                for second_field in empty_fields2:
                    if second_field != first_field:
                        board_copy = Board(board.size, board.win_cond)
                        board_copy.board_list = board.board_list[:]

                        board_copy.change_field(first_field, symbol)
                        board_copy.change_field(second_field, symbol)
                        if board_copy.is_victory() == field_markings.index(symbol):
                            good_fields.append(first_field)
                            good_fields.append(second_field)

                        del board_copy
                del empty_fields2[0]
            if good_fields:
                # print("fields that can make a line for "+symbol)
                # print(good_fields)
                board.change_field(random.choice(good_fields), self.team)
                return

        board.change_field(random.choice(empty_fields), self.team)
