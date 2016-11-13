#Imports
import pygame as py
import random
from settings import *
from sprites import *
from enemies import *
from bullet import *


class Game:
    def __init__(self):
        #initilaize game window, etc
        py.init()
        py.mixer.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
##        self.screen = py.display.set_mode(self.screen, py.RESIZABLE)
        py.display.set_caption(TITLE)
        self.clock = py.time.Clock()
        self.running = True
        self.font_name = py.font.match_font(FONT_NAME)

    def new(self):
        #start new Game
        self.score = 0
        self.all_sprites = py.sprite.Group()
        self.platforms = py.sprite.Group()
        #Reference-link to game
        self.player = Player(self)
        self.mob = Mob(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.mob)
        for plats in PLATFORM_List:
            p = Platform(*plats)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Game Loop update
        self.all_sprites.update()
        #when player collides with platform when falling
        if self. player.vel.y > 0:
            hits = py.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)

            #check if mob collibe with player
        hits = py.sprite.spritecollide(player,mobs, True, py.sprite.collide_circle)
        if hits:
            running = True

        #checks if bullets collide with mob
        hits = py.sprite.groupcollide(mobs, bullets, True,True)
       #Loop to generate just as many new mobs as were the ones killed
        for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)


    def events(self):
        #Game Loop events
        for event in py.event.get():
            # check for closing window
            if event.type == py.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    self.player.jump()

    def draw(self):
        #Draw Game Loops
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        py.display.flip()

    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, CYAN, WIDTH/2,HEIGHT/4)
        self.draw_text("Press arrow keys to move and space to jump", 20, WHITE, WIDTH/2, (HEIGHT*3/4)-40)
        self.draw_text("Press a key to play...",20, WHITE, WIDTH/2, HEIGHT *3/4)
        py.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        #Game Over/Continue
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER!", 48, CYAN, WIDTH/2,HEIGHT/4)
        self.draw_text("Score: " + str(self.score), 20, WHITE, WIDTH/2, (HEIGHT*3/4)-40)
        self.draw_text("Press a key to play again",20, WHITE, WIDTH/2, HEIGHT *3/4)


    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in py.event.get():
                if event.type == py.QUIT:
                    waiting  = False
                    self.running = False
                if event.type == py.KEYUP:
                    waiting = False


    def draw_text(self, text, size, color, x,y):
        font = py.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

py.quit()
