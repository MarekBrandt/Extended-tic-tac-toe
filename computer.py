import math
import random
from board import Board
from player import Player
from constants import field_markings


class Computer(Player):
    def __init__(self, team):
        super().__init__(team, "Computer")

    def minimax(self, board, depth, alpha, beta, is_maximising, max_depth):

        if self.team == 'o':
            comp_team = 'o'
            player_team = 'x'
        else:
            comp_team = 'x'
            player_team = 'o'
        result = board.is_victory()
        # check if one of the players is winning
        if result == field_markings.index(comp_team):
            score = 1 / depth
            return [score, 0]
        elif result == field_markings.index(player_team):
            score = -1 / depth
            return [score, 0]
        # check if tie
        if result == 0 or depth == max_depth:
            return [0, 0]

        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]

        if is_maximising:
            best_score = -math.inf
            index = None
            for field in empty_fields:
                board.change_field(field, comp_team)
                score_index_list = self.minimax(board, depth + 1, alpha, beta, False, max_depth)
                board.change_field(field, 'empty')
                if score_index_list[0] > best_score:
                    best_score = score_index_list[0]
                    index = field
                alpha = max(best_score, alpha)
                if alpha >= beta:
                    break
            return [best_score, index]

        else:
            best_score = math.inf
            index = None
            for field in empty_fields:
                board.change_field(field, player_team)
                score_index_list = self.minimax(board, depth + 1, alpha, beta, True, max_depth)
                board.change_field(field, 'empty')
                if score_index_list[0] < best_score:
                    best_score = score_index_list[0]
                    index = field

                beta = min(beta, best_score)
                if alpha >= beta:
                    break
            return [best_score, index]

    def make_move(self, board):
        score_index_list = self.minimax(board, 1, -2, 2, True, 10)
        board.change_field(score_index_list[1], self.team)
        return True

    def make_move2(self, board):
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
            winning_fields = []
            for field in empty_fields:
                board_copy = Board(board.size, board.win_cond, board.WINDOW)
                board_copy.board_list = board.board_list[:]

                board_copy.change_field(field, symbol)
                if board_copy.is_victory() == field_markings.index(symbol):
                    winning_fields.append(field)

                del board_copy
            if winning_fields:
                # print("winning fields for "+symbol)
                # print(winning_fields)
                board.change_field(random.choice(winning_fields), self.team)
                return True

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
                        board_copy = Board(board.size, board.win_cond, board.WINDOW)
                        board_copy.board_list = board.board_list[:]

                        board_copy.change_field(first_field, symbol)
                        board_copy.change_field(second_field, symbol)
                        if board_copy.is_victory() == field_markings.index(symbol):
                            good_fields.append(first_field)
                            good_fields.append(second_field)

                        del board_copy
                del empty_fields2[0]
            if good_fields:
                board.change_field(random.choice(good_fields), self.team)
                return True

        board.change_field(random.choice(empty_fields), self.team)
        return True
