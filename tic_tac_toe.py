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
                    input("Type size of the board")
            else:
                print("Type correct number")
        except ValueError:
            print("Type number")


def main():
    size = 3
    in_line = 3
    nickname1 = "Player1"
    nickname2 = "Player2"

    option = menu_options()

    if option == 1:
        Game(size, in_line, nickname1, nickname2)
    elif option == 2:
        change_board_settings(size, in_line)

    run = True
    while run:
        size = input("Type the width of the board: ")
        try:
            size = int(size)
            if 3 <= size < 11:
                print("Creating a board " + str(size) + "x" + str(size))
                run = False
            else:
                print("Try a number in range 3 to 10")
        except ValueError:
            print("You have to type a number")
    game = Game(size)


if __name__ == '__main__':
    main()
