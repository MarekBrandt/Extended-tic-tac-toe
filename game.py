import interface
from board import Board
from player import Player
from computer import Computer
from constants import field_markings
import pygame as pg
import sys
import random


class Game:
    def __init__(self, WIN, size, in_line, nickname1, nickname2, game_with_ai):
        self.WIN = WIN
        self.board = Board(size, in_line)
        # every game draw player1 team it can be 'o' or 'x'
        team1 = random.randrange(1, 3)
        if team1 == 1:
            team2 = 2
        else:
            team2 = 1
        self.player1 = Player(field_markings[team1], nickname1)
        if not game_with_ai:
            self.player2 = Player(field_markings[team2], nickname2)
        else:
            self.player2 = Computer(field_markings[team2])

        if self.player1.team == "x":
            self.first = self.player1
            self.second = self.player2
        else:
            self.first = self.player2
            self.second = self.player1

        self.start()

    def tie(self):
        self.board.show(self.WIN)
        return False

    def start(self):
        run = True  # the game screen is shown
        in_game = True  # represents if game is played at the moment
        counter = 0
        while run:
            if in_game:
                # if below decides which player should make a move now
                if counter % 2 == 0:
                    player = self.first
                else:
                    player = self.second

                interface.board_message = player.name + " your move"
                self.board.show(self.WIN)

                if self.board.size <= 3:
                    run = player.make_move(self.board)
                else:
                    run = player.make_move2(self.board)
                if self.board.is_victory() == field_markings.index(player.team):
                    self.board.show(self.WIN)
                    interface.board_message = "Victory! " + player.name + " won!"
                    in_game = False
                else:
                    if self.board.is_not_full():
                        self.board.show(self.WIN)
                    else:
                        interface.board_message = "It's a tie. Well played"
                        in_game = False
            else:
                self.board.show(self.WIN)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False
                if event.type == pg.MOUSEBUTTONDOWN and not in_game:
                    run = False

            counter += 1
        interface.board_message = ""
