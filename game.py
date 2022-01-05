from board import Board
from player import Player
from constants import field_markings
import random


class Game:
    def __init__(self, size):
        self.board = Board(size)
        team1 = random.randrange(1, 3)
        if team1 == 1:
            team2 = 2
        else:
            team2 = 1
        self.player1 = Player(field_markings[team1])
        self.player2 = Player(field_markings[team2])

        if self.player1.team == "x":
            self.first = self.player1
            self.second = self.player2
        else:
            self.first = self.player2
            self.second = self.player1

    def start(self):
        run = True
        while run:
            self.board.show()
            self.first.make_move(self.board)
            if self.board.is_not_full():
                self.board.show()
                self.second.make_move(self.board)
                """ To consideration
                Is it possible that second player will make board full?
                run = self.board.is_not_full()"""
            else:
                self.board.show()
                print("It's a tie. Well played!")
                run = False
