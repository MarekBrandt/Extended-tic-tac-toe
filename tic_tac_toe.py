from game import Game
import pygame as pg
import constants
WIN = pg.display.set_mode((constants.WIDTH, constants.HEIGHT))


def draw_menu():
    font = pg.font.Font(None, 32)
    color = pg.Color((255, 255, 255))
    txt_surface = font.render("Welcome to Tic-Tac-Toe game.", True, color)
    WIN.blit(txt_surface, (100, 100))

    pg.display.flip()

def menu_options():
    print("Welcome to Tic-Tac-Toe game.")
    run = True
    while run:
        print("1. Play with human")
        print("2. Play with computer")
        print("3. Change board settings")
        print("4. Change players names")
        print("5. Quit game")
        print()
        option = input("Choose option: ")
        try:
            option = int(option)
            if 1 <= option <= 5:
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
                    size = change_board_size(in_line)
                elif option == 2:
                    in_line = change_win_condition(size)
                else:
                    return size, in_line
            else:
                print("Type correct number")
        except ValueError:
            print("Type number")


def change_board_size(win_cond):
    run = True
    while run:
        new_size = input("Type size of the board: ")
        try:
            new_size = int(new_size)
            if win_cond <= new_size < 11:
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
    run = True
    while run:
        print("First player nickname is " + nickname1)
        print("Second player nickname is " + nickname2)
        print()
        print("1. Change first player nickname")
        print("2. Change second player nickname")
        print("3. Return")
        print()
        option = input("Choose option: ")
        try:
            option = int(option)
            if 1 <= option <= 3:
                if option == 1:
                    nickname1 = change_nickname()
                elif option == 2:
                    nickname2 = change_nickname()
                else:
                    return nickname1, nickname2
            else:
                print("Type correct number")
        except ValueError:
            print("Type number")


def change_nickname():
    return input("Type new nickname: ")


def main():
    size = 3
    in_line = 3
    nickname1 = "Player1"
    nickname2 = "Player2"

    clock = pg.time.Clock()
    pg.display.set_caption("Tic tac toe")

    pg.init()

    run = True
    while run:
        draw_menu()
        clock.tick(constants.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                # todo teraz musisz zrobić menu w pygame, bo to nie zadziała

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()

        """else:
                option = menu_options()
                if option == 1:
                    Game(size, in_line, nickname1, nickname2, False)
                elif option == 2:
                    Game(size, in_line, nickname1, nickname2, True)
                elif option == 3:
                    size, in_line = change_board_settings(size, in_line)
                elif option == 4:
                    nickname1, nickname2 = change_nicknames(nickname1, nickname2)
                else:
                    print("Thank you for playing!")
                    run = False"""
    pg.quit()


if __name__ == '__main__':
    main()
