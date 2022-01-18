from constants import field_markings
import interface


class Player:
    """Represents a player"""

    def __init__(self, team, name):
        self.team = team
        self.name = name

    def make_move(self, board):
        run = True
        interface.act_on_message("your turn", board, self)
        while run:
            index = interface.act_on_message("choose field", board, self)
            try:
                index = int(index)

                if index < 1 or index > board.size ** 2:
                    interface.act_on_message("non-existing field", board, self)
                else:
                    index = index - 1  # now index is starting from 0
                    if board.board_list[index] != field_markings.index("empty"):
                        interface.act_on_message("occupied field", board, self)
                    else:
                        board.change_field(index, self.team)
                        run = False
            except ValueError:
                interface.act_on_message("value error", board, self)


