from constants import field_markings


class Player:
    """Represents a player"""

    def __init__(self, team, name):
        self.team = team
        self.name = name

    def make_move(self, board):
        run = True
        print(self.name + " it\'s your turn")
        while run:
            index = input("Choose a field. Fields are numbered from 1 to "
                          + str(board.size ** 2) + ": ")
            try:
                index = int(index)

                if index < 1 or index > board.size ** 2:
                    print("You can only choose field from 1 to " + str(board.size ** 2) + "!")
                else:
                    index = index - 1  # now index is starting from 0
                    if board.board_list[index] != field_markings.index("empty"):
                        print("This field is already occupied. Choose empty one!")
                    else:
                        board.change_field(index, self.team)
                        run = False
            except ValueError:
                print("Type number!")


