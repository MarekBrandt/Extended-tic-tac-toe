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

    def minimax_alpha_beta(self, board, maximizing_player, alpha, beta):
        index = None
        if self.team == 'o':
            comp_team = 'o'
            player_team = 'x'
        else:
            comp_team = 'x'
            player_team = 'o'
        result = board.is_victory()
        # check if one of the players is winning
        if result == field_markings.index(comp_team):
            return 1, 0
        elif result == field_markings.index(player_team):
            return -1, 0
        # check if tie
        elif result == 0:  # or depth == max_depth:
            return 0, 0

        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]

        if maximizing_player:
            best = -2
            for field in empty_fields:
                board.change_field(field, comp_team)
                val, index = self.minimax_alpha_beta(board, False, alpha, beta)
                if val > best:
                    best = val
                    index = field
                board.change_field(field, 'empty')
                alpha = max(best, alpha)
                if alpha >= beta:
                    break
            return best, index
        else:
            best = 2
            for field in empty_fields:
                board.change_field(field, player_team)
                val, index = self.minimax_alpha_beta(board, True, alpha, beta)
                if val < best:
                    best = val
                    index = field
                board.change_field(field, 'empty')
                beta = min(beta, best)
                if alpha >= beta:
                    break
            return best, index

    def max_alpha_beta(self, board, alpha, beta):
        best_score = -10
        index = 0

        if self.team == 'o':
            comp_team = 'o'
            player_team = 'x'
        else:
            comp_team = 'x'
            player_team = 'o'
        result = board.is_victory()
        # check if one of the players is winning
        if result == field_markings.index(comp_team):
            # score = 1# / depth
            return 1, 0
        elif result == field_markings.index(player_team):
            # score = -1# / depth
            return -1, 0
        # check if tie
        elif result == 0:  # or depth == max_depth:
            return 0, 0

        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]
        for field in empty_fields:
            board.change_field(field, comp_team)
            score, index = self.min_alpha_beta(board, alpha, beta)
            if score > best_score:
                best_score = score
                index = field
            board.change_field(field, 'empty')
            if best_score >= beta:
                return best_score, index
            if best_score > alpha:
                alpha = best_score
        print("MAX AND MY TEAM IS " + comp_team)

        return best_score, index

    def min_alpha_beta(self, board, alpha, beta):

        best_score = 10

        index = 0

        if self.team == 'o':
            comp_team = 'o'
            player_team = 'x'
        else:
            comp_team = 'x'
            player_team = 'o'
        result = board.is_victory()
        # check if one of the players is winning
        if result == field_markings.index(comp_team):
            # score = 1  # / depth
            return 1, 0
        elif result == field_markings.index(player_team):
            # score = -1  # / depth
            return -1, 0
            # check if tie
        if result == 0:  # or depth == max_depth:
            return 0, 0

        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]
        for field in empty_fields:
            board.change_field(field, player_team)
            score, index = self.max_alpha_beta(board, alpha, beta)
            if score < best_score:
                best_score = score
                index = field
            board.change_field(field, 'empty')
            if best_score <= alpha:
                return best_score, index

            if best_score < beta:
                beta = best_score

        print("MIN AND MY TEAM IS " + player_team)
        return best_score, index

    def make_move3(self, board):
        score, index = self.minimax_alpha_beta(board, True, -10, 10)
        board.change_field(index, self.team)
        """best_score = -2
        best_move = 0
        best_fields = []
        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]
        for field in empty_fields:
            board.change_field(field, self.team)
            score = self.minimax(board, 1, 2, -2, False, 10)
            board.change_field(field, 'empty')
            if score > best_score:
                best_fields = [field]
                best_score = score
                best_move = field
            elif score == best_score:
                best_fields.append(field)"""
        # if best_score == 0:
        #    board.change_field(random.choice(empty_fields), self.team)
        # else:
        # board.change_field(random.choice(best_fields), self.team)
        # board.change_field(index, self.team)
        # board.change_field(best_move, self.team)
        return True

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
            return score
        elif result == field_markings.index(player_team):
            score = -1 / depth
            return score
        # check if tie
        if result == 0:  # or depth == max_depth:
            return 0

        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]

        if is_maximising:
            best_score = -math.inf
            for field in empty_fields:
                board.change_field(field, comp_team)
                score = self.minimax(board, depth + 1, alpha, beta, False, max_depth)
                board.change_field(field, 'empty')
                best_score = max(best_score, score)
                alpha = max(best_score, alpha)
                if alpha >= beta:
                    break

            return best_score

        else:
            best_score = math.inf
            for field in empty_fields:
                board.change_field(field, player_team)
                score = self.minimax(board, depth + 1, alpha, beta, True, max_depth)
                board.change_field(field, 'empty')
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if alpha >= beta:
                    break

            return best_score

    def make_move(self, board):
        best_score = -math.inf
        best_move = 0
        best_fields = []
        empty_fields = [x for x, field in enumerate(board.board_list) if field == field_markings.index("empty")]
        for field in empty_fields:
            board.change_field(field, self.team)
            score = self.minimax(board, 1, -2, 2, False, 10)
            board.change_field(field, 'empty')
            if score > best_score:
                best_fields = [field]
                best_score = score
                best_move = field
            elif score == best_score:
                best_fields.append(field)
        # if best_score == 0:
        #    board.change_field(random.choice(empty_fields), self.team)
        # else:
        # board.change_field(random.choice(best_fields), self.team)
        board.change_field(best_move, self.team)
        # board.change_field(best_move, self.team)
        return True

    def make_move2(self, board):
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
        return True
