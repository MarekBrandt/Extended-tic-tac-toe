import sys
from game import Game
import pygame as pg
import constants
from constants import COLORS
from interface import main_menu_text, options_menu_text, board_settings_menu_text

WIN = pg.display.set_mode((constants.WIDTH, constants.HEIGHT))
clock = pg.time.Clock()


# fract_width argument is the fraction of app window screen
def rects_for_menu(no_of_butt, fract_WIDTH=(2 / 3), gap=30, button_height=60):
    rectangles = []

    # total height is sum of buttons height and gaps between them
    rects_height = no_of_butt * button_height + (no_of_butt - 1) * gap
    width = constants.WIDTH * fract_WIDTH
    x = constants.WIDTH / 2 - width / 2  # WIDTH/2 - width/2
    y_start = constants.HEIGHT / 2 - rects_height / 2
    for i in range(no_of_butt):
        y = i * (button_height + gap) + y_start
        rectangles.append(pg.Rect(x, y, width, button_height))

    return rectangles


def draw_menu(rectangles, which_menu):
    WIN.fill(COLORS['black'])
    buttons_font = pg.font.Font(None, 32)
    caption = pg.font.Font(None, 40)
    txt_surface = ''
    for i in range(len(rectangles)):
        if i == 0:
            font = caption
        else:
            font = buttons_font
        pg.draw.rect(WIN, COLORS['white'], rectangles[i])
        if which_menu == 'main':
            txt_surface = font.render(main_menu_text[i], True, COLORS['black'])
        elif which_menu == 'options':
            txt_surface = font.render(options_menu_text[i], True, COLORS['black'])
        elif which_menu == 'board_set':
            txt_surface = font.render(board_settings_menu_text[i], True, COLORS['black'])
        WIN.blit(txt_surface, rectangles[i])
    pg.display.update()


def options(size, in_line, nickname1, nickname2):
    rectangles = rects_for_menu(4)
    run = True
    click = False
    while run:
        draw_menu(rectangles, 'options')
        pos = pg.mouse.get_pos()
        if click:
            if rectangles[1].collidepoint(pos):
                board_settings(size, in_line)
            elif rectangles[2].collidepoint(pos):
                nickname1, nickname2 = change_nicknames(nickname1, nickname2)
            elif rectangles[3].collidepoint(pos):
                run = False
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def board_settings(size, in_line):
    rectangles = rects_for_menu(5)
    run = True
    click = False
    while run:
        draw_menu(rectangles, 'board_set')
        pos = pg.mouse.get_pos()
        if click:
            if rectangles[2].collidepoint(pos):
                pass
            elif rectangles[3].collidepoint(pos):
                pass
            elif rectangles[4].collidepoint(pos):
                run = False
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


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

    pg.display.set_caption("Tic tac toe")

    pg.init()

    rectangles = rects_for_menu(5)

    run = True
    click = False
    while run:
        draw_menu(rectangles, 'main')
        pos = pg.mouse.get_pos()
        if click:
            if rectangles[1].collidepoint(pos):
                Game(WIN, size, in_line, nickname1, nickname2, False)
            elif rectangles[2].collidepoint(pos):
                Game(WIN, size, in_line, nickname1, nickname2, True)
            elif rectangles[3].collidepoint(pos):
                options(size, in_line, nickname1, nickname2)
                # size, in_line = change_board_settings(size, in_line)
            # elif rectangles[4].collidepoint(pos):
            # nickname1, nickname2 = change_nicknames(nickname1, nickname2)
            elif rectangles[4].collidepoint(pos):
                pg.quit()
                sys.exit()
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)

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


if __name__ == '__main__':
    main()
