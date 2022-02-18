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


def draw_menu(rectangles, which_menu, highlighted = []):
    WIN.fill(COLORS['black'])
    buttons_font = pg.font.Font(None, 32)
    caption = pg.font.Font(None, 40)
    txt_surface = ''
    for i in range(len(rectangles)):
        if i == 0:
            font = caption
        else:
            font = buttons_font
        if i in highlighted:
            pg.draw.rect(WIN, COLORS['light_blue'], rectangles[i])
        else:
            pg.draw.rect(WIN, COLORS['white'], rectangles[i])
        if which_menu == 'main':
            txt_surface = font.render(main_menu_text[i], True, COLORS['black'])
        elif which_menu == 'options':
            txt_surface = font.render(options_menu_text[i], True, COLORS['black'])
        elif which_menu == 'board_set':
            txt_surface = font.render(board_settings_menu_text[i], True, COLORS['black'])
        elif which_menu == 'change_nick':
            txt_surface = font.render(change_nicknames_menu_text[i], True, COLORS['black'])

        txt_x = rectangles[i].width/2 - txt_surface.get_width()/2 + rectangles[i].x
        txt_y = rectangles[i].height/2 - txt_surface.get_height()/2 + rectangles[i].y

        WIN.blit(txt_surface, (txt_x, txt_y, txt_surface.get_width(), txt_surface.get_height()))
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
    old_nicks = [nickname1, nickname2]
    nicks = [nickname1[:], nickname2[:]]
    rectangles = rects_for_menu(4)
    run = True
    click = False
    while run:
        # takes text displayed in button concatenates to it size of the board
        tokens = change_nicknames_menu_text[1].split(': ')
        change_nicknames_menu_text[1] = tokens[0] + ': ' + nicks[0]

        # takes text displayed in button concatenates to it win condition
        tokens = change_nicknames_menu_text[2].split(': ')
        change_nicknames_menu_text[2] = tokens[0] + ': ' + nicks[1]

        draw_menu(rectangles, 'change_nick', [which+1])
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


if __name__ == '__main__':
    main()
