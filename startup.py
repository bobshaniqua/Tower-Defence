import pygame as pg, os, sys, csv
import config as C, button as B, mapgen


class Menu():
    def __init__(self):
        pg.init()
        self.screen = C.screen
        self.button_x = C.game_screen_full_w * 0.4
        self.button_y = [C.game_screen_h * 0.30, C.game_screen_h * 0.50, C.game_screen_h * 0.70]
        self.play_button = B.Button("mapgen.main()", (160, 40), (self.button_x,self.button_y[0]), C.L_BLUE, C.DARK_GREY, None, C.BLUE, C.L_BLUE, "Play")
        self.lead_button = B.Button("startup.Lead()", (200, 40), (self.button_x - 20,self.button_y[1]), C.L_BLUE, C.DARK_GREY, None, C.BLUE, C.L_BLUE, "Leaderboard")
        self.quit_button = B.Button("quit()", (160, 40), (self.button_x,self.button_y[2]), C.L_BLUE, C.DARK_GREY, None, C.BLUE, C.L_BLUE, "Quit")
        self.vol_button = B.Button(None, (50,50), (40,40), C.L_BLUE, C.DARK_GREY, None, C.BLUE, C.L_BLUE, "♫")
        self.menu_screen()

    def menu_screen(self):
        m_loop = False
        self.screen.fill(C.BLUE)
        while not m_loop:
            self.play_button.draw()
            self.lead_button.draw()
            self.quit_button.draw()
            self.vol_button.draw()
            event_main()
            pg.display.update()




class Lead():
    def __init__(self):
        self.screen = C.screen
        self.increment = 40
        self.back_x = C.game_screen_full_w*0.9
        self.back_y = C.game_screen_h*0.9
        self.leaderboard()

    def leaderboard(self):
        l_loop = False
        self.screen.fill(C.BLUE)
        self.leaderboard_sort()
        while not l_loop:
            quit_event()
            pg.display.update()
            B.button_object("Back",self.screen,self.back_x,self.back_y,80,30,C.L_BLUE,C.DARK_GREY,C.BLUE,C.L_BLUE,"startup.Menu()")

    def leaderboard_sort(self):
        with open ('leaderboard.csv','r') as csv_file:
            reader = csv.reader(csv_file)
            sorted_file = sorted(reader, key=lambda x: int(x[1]), reverse = True)
            sorted_file[:0] = [['Name','Score','Wave']]
            y_list_pos = C.game_screen_h*0.15
            for s in sorted_file[0:11]:
                self.leaderboard_blit(s[0:1], y_list_pos, C.game_screen_full_w*0.2)
                self.leaderboard_blit(s[1:2], y_list_pos, C.game_screen_full_w*0.4)
                self.leaderboard_blit(s[2:3], y_list_pos, C.game_screen_full_w*0.6)
                y_list_pos = y_list_pos + self.increment

    def leaderboard_blit(self, list_convert, y_list_pos, x_list_pos):
        to_blit = str(list_convert).replace('[','').replace(']','').replace(',','    ').replace("'","    ")
        label = ((B.font("Rabid Science.ttf",30, False, False, False)).render(to_blit, 1, C.L_BLUE))
        self.screen.blit(label,(x_list_pos,y_list_pos))


def game():
    live_menu = Menu()


#quit function
def event_main():
    for event in pg.event.get():
        live_menu.play_button.event_handler(event)
        live_menu.lead_button.event_handler(event)
        live_menu.quit_button.event_handler(event)
        live_menu.vol_button.event_handler(event)
        if event.type == pg.QUIT:
                pg.quit(), sys.exit()
