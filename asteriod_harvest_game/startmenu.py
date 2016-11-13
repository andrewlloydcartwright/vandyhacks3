import pygame as py
from settings import *
from main import *

class StartMenu():
    def __init__(self, screen, items, COLOR):
        self.screen = screen
        self.COLOR = COLOR
        self.clock = py.time.Clock()
        self.items = items

    def run(self):
        mainLoop = True
        while mainLoop:
            self.clock.tick(50)

            for event in py.event.get():
                if event.type == py.QUIT:
                    mainLoop = False


            self.screen.fill(self.COLOR)
            py.display.flip()
if __name__ == "__main__":
    #Create the Screen
    screen = py.display.set_mode((HEIGHT,WIDTH))
    menu_items = ('Start', 'Quit')
    py.display.set_caption('Start Menu')
    sm = StartMenu(screen, menu_items, BLACK)
    sm.run()
