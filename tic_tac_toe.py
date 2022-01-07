from game import Game


def main():
    print("Welcome to Tic-Tac-Toe game.")
    size = 3
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
