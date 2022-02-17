import sys
from game import Game
import pygame as pg
import constants
from constants import COLORS
from interface import main_menu_text, options_menu_text, board_settings_menu_text, change_nicknames_menu_text

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
        elif which_menu == 'change_nick':
            txt_surface = font.render(change_nicknames_menu_text[i], True, COLORS['black'])
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
            # board settings
            if rectangles[1].collidepoint(pos):
                size, in_line = board_settings(size, in_line)
            # nicknames
            elif rectangles[2].collidepoint(pos):
                nickname1, nickname2 = change_nicknames_menu(nickname1, nickname2)
            # quit
            elif rectangles[3].collidepoint(pos):
                return size, in_line, nickname1, nickname2
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def board_settings(size, in_line):
    rectangles = rects_for_menu(4)
    run = True
    click = False
    while run:
        # takes text displayed in button concatenates to it size of the board
        tokens = board_settings_menu_text[1].split(': ')
        board_settings_menu_text[1] = tokens[0] + ': ' + str(size)

        # takes text displayed in button concatenates to it win condition
        tokens = board_settings_menu_text[2].split(': ')
        board_settings_menu_text[2] = tokens[0] + ': ' + str(in_line)

        draw_menu(rectangles, 'board_set')
        pos = pg.mouse.get_pos()
        if click:
            if rectangles[1].collidepoint(pos):
                size += 1
                if size > 10:
                    size = 3
            elif rectangles[2].collidepoint(pos):
                in_line += 1
                if in_line > 10:
                    in_line = 3
            elif rectangles[3].collidepoint(pos):
                return size, in_line
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def change_nicknames_menu(nickname1, nickname2):
    rectangles = rects_for_menu(4)
    run = True
    click = False
    while run:
        # takes text displayed in button concatenates to it size of the board
        tokens = change_nicknames_menu_text[1].split(': ')
        change_nicknames_menu_text[1] = tokens[0] + ': ' + nickname1

        # takes text displayed in button concatenates to it win condition
        tokens = change_nicknames_menu_text[2].split(': ')
        change_nicknames_menu_text[2] = tokens[0] + ': ' + nickname2

        draw_menu(rectangles, 'change_nick')
        pos = pg.mouse.get_pos()
        if click:
            if rectangles[1].collidepoint(pos):
                nickname1 = changing_nickname(nickname1, nickname2, 0)
            elif rectangles[2].collidepoint(pos):
                nickname2 = changing_nickname(nickname1, nickname2, 1)
            elif rectangles[3].collidepoint(pos):
                return nickname1, nickname2
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def changing_nickname(nickname1, nickname2, which):
    if which == 0:
        new_nicks = ["", nickname2]
    else:
        new_nicks = [nickname1, ""]
    rectangles = rects_for_menu(4)
    run = True
    click = False
    while run:
        # takes text displayed in button concatenates to it size of the board
        tokens = change_nicknames_menu_text[1].split(': ')
        change_nicknames_menu_text[1] = tokens[0] + ': ' + new_nicks[0]

        # takes text displayed in button concatenates to it win condition
        tokens = change_nicknames_menu_text[2].split(': ')
        change_nicknames_menu_text[2] = tokens[0] + ': ' + new_nicks[1]

        draw_menu(rectangles, 'change_nick')
        if click:
            return new_nicks[which]
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if new_nicks[which]:
                        new_nicks[which] = new_nicks[which][:-1]
                else:
                    new_nicks[which] += event.unicode

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
            # 2 players
            if rectangles[1].collidepoint(pos):
                Game(WIN, size, in_line, nickname1, nickname2, False)
            # player vs AI
            elif rectangles[2].collidepoint(pos):
                Game(WIN, size, in_line, nickname1, nickname2, True)
            # settings
            elif rectangles[3].collidepoint(pos):
                size, in_line, nickname1, nickname2 = options(size, in_line, nickname1, nickname2)
            # quit
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
