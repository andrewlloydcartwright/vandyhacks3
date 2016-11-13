# Pygame template - skeleton for a new pygame project
import pygame as py
import random
from os import path
from settings import *
from sprites import *
from enemies import *
from bullet import *

img_dir = path.join(path.dirname(__file__), 'img')


class Game:
# initialize pygame and create window
    def __init__(self):
        py.init()
        py.mixer.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption(TITLE)
        self.clock = py.time.Clock()
        self.running = True
        self.font_name = py.font.match_font(FONT_NAME)
    #Game loop
    def run(self):
         # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    #initialize Game, Start new game
    def new(self):
        self.score = 0
        self.all_sprites = py.sprite.Group()
        self.player = self.Player()
        self.all_sprites.add(self.player)
        self.mobs = self.Mob()
        self.all_sprites.add(self.mobs)
        self.bullets = self.Bullet()
        self.all_sprites.add(self.bullets)
        self.run()

        #Load all game graphics
        background = pygame.image.load(path.join(img_dir,"bluestar.png")).convert()
        background_rect = background.get_rect()
        player_img = pygame.image.load(path.join(img_dir,"playerShip2_blue.png")).convert()
        meteor_img = pygame.image.load(path.join(img_dir,"meteorGrey_med1.png")).convert()
        laser_img = pygame.image.load(path.join(img_dir,"laserBlue16.png")).convert()

    def update(self):
        # Update
        self.all_sprites.update()
       #checks if bullets collide with mob
        hits = py.sprite.groupcollide(mobs, bullets, True,True)
        if hits:
            self.score += 10
       #Loop to generate just as many new mobs as were the ones killed
        for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        #check if mob collibe with player
        hits = py.sprite.spritecollide(player,mobs, True, py.sprite.collide_circle)
        if hits:
            self.score -= 10
            running = True



        for i in range(8):
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()



    def draw(self):
        # Draw / render
        self.screen.fill(BLACK)
        self.screen.blit(background, background_rect)
        self.all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        py.display.flip()

    #Start/Splash
    def show_start_screen(self):
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, CYAN, WIDTH/2,HEIGHT/4)
        self.draw_text("Press arrow keys to move and space to jump", 20, WHITE, WIDTH/2, (HEIGHT*3/4)-40)
        self.draw_text("Press a key to play...",20, WHITE, WIDTH/2, HEIGHT *3/4)
        py.display.flip()
        self.wait_for_key()

    #Game Over/Continue Screen
    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER!", 48, CYAN, WIDTH/2,HEIGHT/4)
        # self.draw_text("Score: " + str(self.score), 20, WHITE, WIDTH/2, (HEIGHT*3/4)-40)
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




#Call Game class

g = Game()
g.show_start_screen()

while g.running:
    g.new
    g.show_go_screen()


py.quit()
