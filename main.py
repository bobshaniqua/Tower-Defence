import pygame as pg, time, os, csv, operator, sys
import startup, config as C
from pygame.locals import *


pg.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.display.set_caption("Tower Defence")

print ("Game initialising. Display size: ", C.game_screen_full_w,"x", C.game_screen_h)


if __name__ == "__main__":
    startup.game()
