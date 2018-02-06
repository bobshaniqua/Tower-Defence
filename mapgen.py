import pygame as pg, sys, random, time
import config, button as B

pg.init()
arial = pg.font.SysFont('Arial', 15)



class Grid():
    def __init__(self):
        self.tile_size = config.tile_size #Size of each tile in the grid
        self.map_width = config.map_width #Number of tiles per row (width of display)
        self.map_height = config.map_height #Number of tiles per column (height of display)
        self.screen = config.screen
        self.error_found = False
        self.map_file = ("hard_map.txt")
        self.grass_tile, self.rock_tile, self.water_tile = 0, 1, 2 #Keys for map features such as rocks, grass etc. are assigned here
        self.path_tile, self.point_tile, self.start_tile, self.end_tile, self.error_tile = 3, 4, 5, 6, 7 #Keys for the path the enemies follow are assigned here
        self.tilemap = [[self.grass_tile for w in range(self.map_width)] for h in range (self.map_height)] #Sets each row and column as grass tile by default
        self.textures = {
                            self.grass_tile : pg.image.load('grass.png'), self.path_tile : pg.image.load('path.png'),
                            self.rock_tile : pg.image.load('rock.png'), self.water_tile : pg.image.load('water.png'),
                            self.point_tile : pg.image.load('path.png'), self.start_tile : pg.image.load('path.png'),
                            self.end_tile : pg.image.load('path.png'), self.error_tile : pg.image.load('error.png')
                        }
        with open(self.map_file) as f:
            self.grid_map = [x.strip("\n") for x in f.readlines()] #splits txt file into a list with each line being an element




    def generate_grid(self):
        for rw in range (self.map_height): # for each row in the grid which is 48
            for cl in range (self.map_width): # for each column in each row which is 64
                to_split = (self.grid_map[rw]) #splits the list into 48 elements which each consist of 64 characters
                for i, x in enumerate (to_split[cl]): #for each character in to_split element. i = index of character, x = character
                    if   x == "G" : tile = self.grass_tile
                    elif x == "R" : tile = self.rock_tile
                    elif x == "W" : tile = self.water_tile
                    elif x == "T" : tile = self.path_tile
                    elif x == "P" : tile = self.point_tile
                    elif x == "X" : tile = self.start_tile
                    elif x == "Z" : tile = self.end_tile
                    else:
                        tile = self.error_tile
                        print("Error - Wrong Input: ", x ,"at location", rw, cl, " in map file",self.map_file)
                        self.error_found = True
                    self.tilemap[rw][cl] = tile

    def blit_grid(self):
        for row in range(self.map_height):
            for column in range (self.map_width):
                self.screen.blit(self.textures[self.tilemap[row][column]], (column*self.tile_size, row*self.tile_size))
        if self.error_found: #if unknown character in map, error_found will be set to true and this if statement will be ran
            self.error() #runs the function error

    def error(self):
        pg.display.update() #updates the display to display the map
        time.sleep(1)
        pg.draw.rect(self.screen, config.L_RED, (config.game_screen_w/2-200,config.game_screen_h/2,565,15)) #creates red rectangle
        error_font = B.font("vcr_osd.ttf",12,False,False,False)
        error_msg = error_font.render('ERROR FOUND IN MAP GENERATION. CHECK CONSOLE FOR MORE INFORMATION. SHUTTING DOWN', False, (0, 0, 0)) #sets up text
        self.screen.blit(error_msg,(config.game_screen_w/2-200,config.game_screen_h/2)) #blits text onto screen
        pg.display.update() #updates to display the text
        time.sleep(3), quit()


class Sidebar():
    def __init__(self):
        self.screen = config.screen
        self.side_w = config.side_screen_w
        self.side_h = config.game_screen_h
        self.side_x = config.game_screen_full_w - config.side_screen_w
        self.side_y = 0
        self.b_size = 50



    def blit_sidebar(self):
        pg.draw.rect(self.screen, config.L_BLUE, (self.side_x, self.side_y, self.side_w, self.side_h))
        testimage = pg.image.load('path.png')
        #B.button_img(testimage,self.screen,1124,500,self.b_size,self.b_size,config.L_BLUE,config.DARK_GREY, config.BLUE, config.L_BLUE,None)








#main function which manages grid class and quitting the game
def quit():
    pg.quit()
    sys.exit()

def main():
    live_grid = Grid()
    live_sidebar = Sidebar()
    live_grid.generate_grid()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        live_grid.blit_grid()
        live_sidebar.blit_sidebar()
        pg.display.update()



if __name__ == "__main__":
    main()
