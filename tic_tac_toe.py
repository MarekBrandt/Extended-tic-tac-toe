from board import Board


def main():
    game_board = Board(3)
    game_board.change_field(3, 'o')
    game_board.change_field(6, 'x')
    game_board.show()


if __name__ == '__main__':
    main()
