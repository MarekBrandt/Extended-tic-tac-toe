import constants
import pygame as pg
import interface


def decode_menu_set(menu_set):
    # deafult menu settings
    buttons_number = 3
    fract_WIDTH = (2 / 3)
    gap = 30
    button_height = 60
    if len(menu_set) >= 1:
        buttons_number = menu_set[0]
    if len(menu_set) >= 2:
        fract_WIDTH = menu_set[1]
    if len(menu_set) >= 3:
        gap = menu_set[2]
    if len(menu_set) >= 4:
        button_height = menu_set[3]

    return buttons_number, fract_WIDTH, gap, button_height


# fract_width argument is the fraction of app window screen
def rects_for_menu(menu_set):
    no_of_butt = menu_set[0]
    fract_WIDTH = menu_set[1]
    gap = menu_set[2]
    button_height = menu_set[3]
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


class Menus:

    def __init__(self, WIN, menu_name, menu_set):
        menu_set = decode_menu_set(menu_set)
        self.WIN = WIN
        self.rectangles = rects_for_menu(menu_set)

        # get text for this menu
        if menu_name == 'main':
            self.menu_text = interface.main_menu_text
        elif menu_name == 'options':
            self.menu_text = interface.options_menu_text
        elif menu_name == 'board_set':
            self.menu_text = interface.board_settings_menu_text
        elif menu_name == 'change_nick':
            self.menu_text = interface.change_nicknames_menu_text

    def draw(self, highlighted=[]):
        self.WIN.fill(constants.COLORS['black'])
        buttons_font = pg.font.Font(None, 32)
        caption = pg.font.Font(None, 40)
        for i in range(len(self.rectangles)):
            if i == 0:
                font = caption
            else:
                font = buttons_font
            if i in highlighted:
                pg.draw.rect(self.WIN, constants.COLORS['light_blue'], self.rectangles[i])
            else:
                pg.draw.rect(self.WIN, constants.COLORS['white'], self.rectangles[i])

            txt_surface = font.render(self.menu_text[i], True, constants.COLORS['black'])

            txt_x = self.rectangles[i].width / 2 - txt_surface.get_width() / 2 + self.rectangles[i].x
            txt_y = self.rectangles[i].height / 2 - txt_surface.get_height() / 2 + self.rectangles[i].y

            self.WIN.blit(txt_surface, (txt_x, txt_y, txt_surface.get_width(), txt_surface.get_height()))
        pg.display.update()
