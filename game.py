import constants
import interface
from board import Board
from player import Player
from computer import Computer
from constants import field_markings
import pygame as pg
import sys
import random


class Game:
    # __init__ sets variables and starts a game
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
        interface.act_on_message("tie", self.board, None)
        return False

    def start(self):
        run = True
        counter = 0
        self.board.show(self.WIN)
        while run:
            # if below decides which player should make a move now
            if counter % 2 == 0:
                player = self.first
            else:
                player = self.second

            if not player.make_move(self.board):
                run = False
            if self.board.is_victory() == field_markings.index(player.team):
                self.board.show(self.WIN)
                interface.act_on_message("victory", self.board, player)
                run = False
            else:
                if self.board.is_not_full():
                    self.board.show(self.WIN)
                else:
                    run = self.tie()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False

            counter += 1
