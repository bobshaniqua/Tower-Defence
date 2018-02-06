import pygame as pg, time, sys
import mapgen, config as C

class Button():
    def __init__(self, action, size, position, ac, ic, img, afc, ifc, text):
        self.screen = C.screen
        self.b_img = [pg.Surface(size),pg.Surface(size)]   #creates list of 2 pygame surfaces of specified size
        self.b_img[0].fill((ic)) #fills surface 1 with inactive colour
        self.b_img[1].fill((ac)) #fills surface 2 with active colour
        self.rect = pg.Rect(position, size) #creates a rectangle with size dimensions using position coords
        self.index = 0 #index used to set which surface is displayed


#for images button
        self.image = img #sets image as instance variable so it can be used in other functions
        if img is not None:
            self.center_image = (self.image.get_rect()).center  #finds dimensions of image and sets the center of them to self.center_image
            self.center_b_img = (self.rect.center[0]-self.center_image[0]),(self.rect.center[1]-self.center_image[1]) #sets it so coords for image in button to be blit are in the center

#for text button
        self.text = text
        self.font = font("Minecraft.ttf",20,False,False,False)
        if text is not None:
            self.active_text = [(self.font.render(self.text, 1, ifc)),(self.font.render(self.text, 1, afc))]
            self.center_text = (self.active_text[0].get_rect()).center
            self.center_b_text = (self.rect.center[0]-self.center_text[0]),(self.rect.center[1]-self.center_text[1])

        self.action = action

    def draw(self):
        # draw selected image
        self.screen.blit(self.b_img[self.index], self.rect) #blits the surface
        if self.image is not None : self.screen.blit(self.image,(self.center_b_img))
        if self.text is not None : self.screen.blit(self.active_text[self.index],(self.center_b_text))

    def event_handler(self, event):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.index = 1
            if event.type == pg.MOUSEBUTTONDOWN: #Is button clicked
                if event.button == 1:exec(self.action)
        else: self.index = 0


def font(font,size,bold,italic,underline):
    text_font = pg.font.Font(font,size)
    text_font.set_bold(bold)
    text_font.set_italic(italic)
    text_font.set_underline(underline)
    return text_font


    #button code
def text_objects(text,font,colour):
    text_surface = (font).render(text, True, colour)
    return text_surface, text_surface.get_rect()


def button_object(msg,screen,x,y,w,h,fc,afc,ic,ac,action):
    pg.draw.rect(screen, ac,(x,y,w,h))
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(screen, ac, (x,y,w,h))
        text_surf, text_rect = text_objects(msg, font("Rabid Science.ttf",20,True,False,False), afc)
        if click[0] == 1 and action != None:
            exec(action)
            time.sleep(0.5)
    else:
        pg.draw.rect(screen, ic , (x,y,w,h))
        text_surf, text_rect = text_objects(msg, font("Rabid Science.ttf",20,True,False,False), fc)
    text_rect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(text_surf, text_rect)




def quit():
    pg.quit(), sys.exit()
