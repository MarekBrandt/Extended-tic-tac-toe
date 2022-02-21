import sys
from game import Game
import pygame as pg
import constants
from menus import Menus

WIN = pg.display.set_mode((constants.WIDTH, constants.HEIGHT))
clock = pg.time.Clock()


def options(size, in_line, nickname1, nickname2):
    menu = Menus(WIN, 'options')
    run = True
    click = False
    while run:
        menu.draw()
        pos = pg.mouse.get_pos()
        if click:
            # board settings
            if menu.rectangles[1].collidepoint(pos):
                size, in_line = board_settings(size, in_line)
            # nicknames
            elif menu.rectangles[2].collidepoint(pos):
                nickname1, nickname2 = change_nicknames_menu(nickname1, nickname2)
            # resolution
            elif menu.rectangles[3].collidepoint(pos):
                if change_resolution():
                    pg.display.set_mode((constants.WIDTH, constants.HEIGHT))
                    main()
            # quit
            elif menu.rectangles[4].collidepoint(pos):
                return size, in_line, nickname1, nickname2
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return size, in_line, nickname1, nickname2

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def change_resolution():
    menu = Menus(WIN, 'resolution')
    run = True
    click = False
    while run:
        menu.draw()
        pos = pg.mouse.get_pos()
        if click:
            # 600x600
            if menu.rectangles[1].collidepoint(pos):
                constants.WIDTH = 600
                constants.HEIGHT = 600
                return 1
            if menu.rectangles[2].collidepoint(pos):
                constants.WIDTH = 720
                constants.HEIGHT = 480
                return 1
            if menu.rectangles[3].collidepoint(pos):
                constants.WIDTH = 1280
                constants.HEIGHT = 720
                return 1

            # quit
            elif menu.rectangles[4].collidepoint(pos):
                run = False
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def board_settings(size, in_line):
    menu = Menus(WIN, 'board_set')
    run = True
    click = False
    while run:
        # takes text displayed in button concatenates to it size of the board
        tokens = menu.menu_text[1].split(': ')
        menu.menu_text[1] = tokens[0] + ': ' + str(size)

        # takes text displayed in button concatenates to it win condition
        tokens = menu.menu_text[2].split(': ')
        menu.menu_text[2] = tokens[0] + ': ' + str(in_line)

        menu.draw()
        pos = pg.mouse.get_pos()
        if click:
            if menu.rectangles[1].collidepoint(pos):
                size += 1
                if size > 10:
                    size = 3
            elif menu.rectangles[2].collidepoint(pos):
                in_line += 1
                if in_line > 10:
                    in_line = 3
            elif menu.rectangles[3].collidepoint(pos):
                return size, in_line
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return size, in_line

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def change_nicknames_menu(nickname1, nickname2):
    menu = Menus(WIN, 'change_nick')
    run = True
    click = False
    while run:
        # takes text displayed in button concatenates to it size of the board
        tokens = menu.menu_text[1].split(': ')
        menu.menu_text[1] = tokens[0] + ': ' + nickname1

        # takes text displayed in button concatenates to it win condition
        tokens = menu.menu_text[2].split(': ')
        menu.menu_text[2] = tokens[0] + ': ' + nickname2

        menu.draw()
        pos = pg.mouse.get_pos()
        if click:
            if menu.rectangles[1].collidepoint(pos):
                nickname1 = changing_nickname(nickname1, nickname2, 0)
            elif menu.rectangles[2].collidepoint(pos):
                nickname2 = changing_nickname(nickname1, nickname2, 1)
            elif menu.rectangles[3].collidepoint(pos):
                return nickname1, nickname2
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return nickname1, nickname2

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        clock.tick(constants.FPS)


def changing_nickname(nickname1, nickname2, which):
    old_nicks = [nickname1, nickname2]
    nicks = [nickname1[:], nickname2[:]]
    menu = Menus(WIN, 'change_nick')
    run = True
    click = False
    while run:
        # takes text displayed in button concatenates to it size of the board
        tokens = menu.menu_text[1].split(': ')
        menu.menu_text[1] = tokens[0] + ': ' + nicks[0]

        # takes text displayed in button concatenates to it win condition
        tokens = menu.menu_text[2].split(': ')
        menu.menu_text[2] = tokens[0] + ': ' + nicks[1]

        menu.draw([which + 1])
        if click:
            if not nicks[which]:
                return old_nicks[which]
            return nicks[which]
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return old_nicks[which]
                if event.key == pg.K_RETURN:
                    if not nicks[which]:
                        return old_nicks[which]
                    return nicks[which]
                if event.key == pg.K_BACKSPACE:
                    if nicks[which]:
                        nicks[which] = nicks[which][:-1]
                else:
                    nicks[which] += event.unicode

        clock.tick(constants.FPS)


def main():
    size = 3
    in_line = 3
    nickname1 = "Player1"
    nickname2 = "Player2"

    pg.display.set_caption("Tic tac toe")

    pg.init()

    menu = Menus(WIN, 'main')

    run = True
    click = False
    while run:
        menu.draw()
        pos = pg.mouse.get_pos()
        if click:
            # 2 players
            if menu.rectangles[1].collidepoint(pos):
                Game(WIN, size, in_line, nickname1, nickname2, False)
            # player vs AI
            elif menu.rectangles[2].collidepoint(pos):
                Game(WIN, size, in_line, nickname1, nickname2, True)
            # settings
            elif menu.rectangles[3].collidepoint(pos):
                size, in_line, nickname1, nickname2 = options(size, in_line, nickname1, nickname2)
            # quit
            elif menu.rectangles[4].collidepoint(pos):
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


if __name__ == '__main__':
    main()
