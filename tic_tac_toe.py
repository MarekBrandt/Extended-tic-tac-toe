from game import Game


def menu_options():
    print("Welcome to Tic-Tac-Toe game.")
    run = True
    while run:
        print("1. Play")
        print("2. Change board settings")
        print("3. Change players names")
        print("4. Quit game")
        print()
        option = input("Choose option: ")
        try:
            option = int(option)
            if 1 <= option <= 4:
                return option
            else:
                print("That is not correct number!")
        except ValueError:
            print("You have to type number!")


def change_board_settings(size, in_line):
    run = True
    while run:
        print("Actual settings:")
        print("Size of the board: " + str(size) + "x" + str(size))
        print("You will win if you get " + str(in_line) + " X or O's in line")
        print()
        print("1. Change size of the board")
        print("2. Change number of fields in line win condition")
        print("3. Return to menu")
        print()
        option = input("Choose option: ")
        try:
            option = int(option)
            if 1 <= option <= 3:
                if option == 1:
                    size = change_board_size()
                elif option == 2:
                    in_line = change_win_condition(size)
                else:
                    return size, in_line
            else:
                print("Type correct number")
        except ValueError:
            print("Type number")


def change_board_size():
    run = True
    while run:
        new_size = input("Type size of the board: ")
        try:
            new_size = int(new_size)
            if 3 <= new_size < 11:
                print("Actual board size is " + str(new_size) + "x" + str(new_size))
                return new_size
            else:
                print("Try a number in range 3 to 10")
        except ValueError:
            print("Type correct number")


def change_win_condition(size):
    run = True
    while run:
        in_line = input("Type the length of winning line: ")
        try:
            in_line = int(in_line)
            if 2 <= in_line <= size:
                print("Changes accepted")
                return in_line
            else:
                print("Try a number in range 3 to size of the board, which is: " + str(size))
        except ValueError:
            print("Type correct number")


def change_nicknames(nickname1, nickname2):
    pass  # todo


def main():
    size = 3
    in_line = 3
    nickname1 = "Player1"
    nickname2 = "Player2"

    run = True
    while run:
        option = menu_options()
        if option == 1:
            Game(size, in_line, nickname1, nickname2)
        elif option == 2:
            size, in_line = change_board_settings(size, in_line)
        elif option == 3:
            change_nicknames(nickname1, nickname2)
        else:
            print("Thank you for playing!")
            run = False


if __name__ == '__main__':
    main()
