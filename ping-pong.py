from random import randint
from pygame import *
import time as tm
init() #! инициализация ресурсов библиотеки
resolution = (600,700)
window = display.set_mode(resolution)
display.set_caption("Ping-pong")
background = transform.scale(image.load("ping-pong_field.png"),resolution)
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,w,h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player1(GameSprite):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y< 500:
            self.rect.y += self.speed
class Player2(GameSprite):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y< 500:
            self.rect.y += self.speed


player1 = Player1("board.png",50,330,25,200,5)
player2 = Player2("board.png",550,330,25,200,5)

'''mixer.init()
mixer.music.load("space.ogg")
mixer.music.set_volume(0.05)
mixer.music.play()'''

font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,25)
font3 = font.Font(None,30)
lose = font1.render("YOU LOSE!",True,(255,0,0))
pause = font3.render("Pause...",True,(255,255,255))
restart = font2.render("Do you want to start over?Yes(y) or No(n)",True,(255,255,255))

clock = time.Clock()
key_pressed = False
finish = False
game = True
while game:
    for e in event.get():
        #if finish != True or pausebtn_png.pause_is_pressed != True:
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                x,y  = e.pos
                '''if pausebtn_png.collidepoint(x,y):
                    pausebtn_png.pause_is_pressed = True'''
                if finish != True:
                        mixer.music.stop()
                        window.blit(pause,(340,250))
                        #window.blit(hint,(325,265))
                        #pausebtn_png.pause_is_pressed = False
                        finish = True
                elif finish == True:
                        mixer.music.play()
                        finish = False
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                x,y  = e.pos
            #if exitbtn_png.collidepoint(x,y):
                #game = False
            if e.type == QUIT:
                game = False
            '''if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if finish != True:
                        if num_fire < 20 and rel_time == False:
                            key_pressed = True'''
            if finish != True:
                    window.blit(background,(0,0))
                    #pausebtn_png.reset()
                    #exitbtn_png.reset()
                    player1.reset()
                    player2.reset()
                    #mega_bullets.draw(window)
                    #mega_bullets.update()
                    #bullets.draw(window)
                    #bullets.update()'''
                    #enemies.draw(window)
                    #asteroids.draw(window)
                    player1.control()
                    player2.control()
    clock.tick(60)
    display.update()