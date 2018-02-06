import pygame as pg

tile_size = 16
map_width = 64
map_height = 48
side_screen_w = 200

if tile_size < 12:
    raise RuntimeError("tile_size in config.py is below minimum accepted integer value. Recommended: tile_size = 16")

game_screen_w, game_screen_h  = (map_width * tile_size), (map_height * tile_size)

game_screen_full_w = game_screen_w + side_screen_w

screen = pg.display.set_mode((game_screen_full_w,game_screen_h))

clock = pg.time.Clock()

FPS = 30

#colours
RED = (160,27,17)
L_RED = (196,62,53)
BLUE = (10,10,51)
L_BLUE = (104,177,255)
GREEN = (26,165,97)
YELLOW = (236,239,55)
ORANGE = (255,167,15)
DARK_GREY = (34,34,34)
