from board import Board
from player import Player


def main():
    player1 = Player("o")
    player2 = Player("x")
    game_board = Board(3)
    player1.make_move(game_board, 4)
    player2.make_move(game_board, 8)
    game_board.show()


if __name__ == '__main__':
    main()
