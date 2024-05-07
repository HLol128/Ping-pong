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
class Ball(GameSprite):
    def ball_control(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.speed *= -1
        if self.rect.y < 50:
            self.speed *= -1
        if self.rect.x > 550 or self.rect.x < 50:
            self.speed *= -1
#! у player1 мяч отбивается от задней грани(исправить)!!!

player1 = Player1("board.png",26,330,25,200,5)
player2 = Player2("board.png",550,330,25,200,5)
ball = Ball("ball.png",300,350,50,50,3)
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
key_pressed_up1 = False
key_pressed_up2 = False
key_pressed_down1 = False
key_pressed_down2 = False
finish = False
game = True
while game:
    for e in event.get():
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
            if e.type == KEYDOWN:
                if e.key == K_w:
                    key_pressed_up1 = True
                if e.key == K_UP:
                    key_pressed_up2 = True
                if e.key == K_s:
                    key_pressed_down1 = True
                if e.key == K_DOWN:
                    key_pressed_down2 = True
            if e.type == KEYUP:
                if e.key == K_w:
                    key_pressed_up1 = False
                if e.key == K_UP:
                    key_pressed_up2 = False
                if e.key == K_s:
                    key_pressed_down1 = False
                if e.key == K_DOWN:
                    key_pressed_down2 = False
    if finish != True:
        if key_pressed_up1 == True:
            if player1.rect.y > 0 and player1.rect.y != 0:
                player1.rect.y -= player1.speed
        if key_pressed_up2 == True:
            if player2.rect.y > 0 and player2.rect.y != 0:
                player2.rect.y -= player2.speed
        if key_pressed_down1 == True:
            if player1.rect.y < 500 and player1.rect.y != 500:
                player1.rect.y += player1.speed
        if key_pressed_down2 == True:
            if player2.rect.y < 500 and player2.rect.y != 500:
                player2.rect.y += player2.speed
                
                     
                    
    if finish != True:
        window.blit(background,(0,0))
        #pausebtn_png.reset()
        #exitbtn_png.reset()
        player1.reset()
        player2.reset()
        ball.reset()
        #mega_bullets.draw(window)
        #mega_bullets.update()
        #bullets.draw(window)
        #bullets.update()'''
        #enemies.draw(window)
        #asteroids.draw(window)
        player1.control()
        player2.control()
        ball.ball_control()

    clock.tick(60)
    display.update()