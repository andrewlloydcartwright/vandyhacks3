import pygame as py
from settings import *

class Player(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(player_img, (50,38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.image_orig = player_img
        self.image = self.image_orig.copy()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0



    def update(self):
        self.speedx = 0
        self.speedy = 0
        #Get Keys
        keystate = py.key.get_pressed()
        if keystate[py.K_LEFT]:
            self.speedx = -8
        if keystate[py.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        if keystate[py.K_UP]:
            self.speedy = -8
        if keystate[py.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy

        #Boundaries
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
