messages = [
    "your turn",
    "choose field",
    "non-existing field",
    "occupied field",
    "value error",
    "victory",
    "tie"
]


def act_on_message(message, board, player):
    message_id = messages.index(message)
    if message_id == 0:
        print(player.name + " it\'s your turn")
    elif message_id == 1:
        index = input("Choose a field. Fields are numbered from 1 to "
                      + str(board.size ** 2) + ": ")
        return index
    elif message_id == 2:
        print("You can only choose field from 1 to " + str(board.size ** 2) + "!")
    elif message_id == 3:
        print("This field is already occupied. Choose empty one!")
    elif message_id == 4:
        print("This have to be a number")
    elif message_id == 5:
        print(player.name + " playing " + player.team.upper() + " won! Congratulations!")
    elif message_id == 6:
        print("It's a tie. Well played!")
