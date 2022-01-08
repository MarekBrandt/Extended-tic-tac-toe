from board import Board
from player import Player
from constants import field_markings
import random


class Game:
    # __init__ sets variables and starts a game
    def __init__(self, size):
        self.board = Board(size)
        # every game draw player1 team it can be 'o' or 'x'
        team1 = random.randrange(1, 3)
        if team1 == 1:
            team2 = 2
        else:
            team2 = 1
        self.player1 = Player(field_markings[team1], "Player1")
        self.player2 = Player(field_markings[team2], "Player2")

        if self.player1.team == "x":
            self.first = self.player1
            self.second = self.player2
        else:
            self.first = self.player2
            self.second = self.player1

        self.start()

    def tie(self):
        self.board.show()
        print("It's a tie. Well played!")
        return False

    def start(self):
        run = True
        counter = 0
        self.board.show()
        while run:
            # if below decides which player should make a move now
            if counter % 2 == 0:
                player = self.first
            else:
                player = self.second

            player.make_move(self.board)
            if self.board.is_victory(player.team, 3):
                self.board.show()
                print(player.name + " won! Congratulations!")
                run = False
            else:
                if self.board.is_not_full():
                    self.board.show()
                else:
                    run = self.tie()

            counter += 1
