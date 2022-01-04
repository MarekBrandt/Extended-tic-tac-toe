class Player:
    """Represents a player"""

    def __init__(self, team):
        self.team = team

    def make_move(self, board, index):
        board.change_field(index, self.team)

