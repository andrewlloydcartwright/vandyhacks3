#Imports
import pygame as py
from settings import *

class Bullet(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((10,20))
        self.image = laser_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y +=self.speedy
        #kill if it moves off the screen
        if self.rect.bottom < 0:
            self.kill()
