from random import randint
from pygame import *
import time as tm
init() #! инициализация ресурсов библиотеки
resolution = (600,700)
window = display.set_mode(resolution,SCALED, vsync=1)
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
    def __init__(self,player_image,player_x,player_y,w,h,player_speed,speed_y):
        super().__init__(player_image,player_x,player_y,w,h,player_speed)
        self.speed_y = speed_y
    def ball_control(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y

        '''if (player1.rect.topright[1] - self.rect.topleft[1]) <= 5 or (player1.rect.topright[1] - self.rect.left) <= 5 or (player1.rect.topright[1] - self.rect.bottomleft[1]) <= 5:
            self.rect.x *= -1
        if (player2.rect.topleft[1] - self.rect.topright[1]) <= 5 or (player2.rect.topleft[1] - self.rect.right) <= 5 or (player2.rect.topleft[1] - self.rect.bottomright[1]) <= 5:
            self.rect.x *= -1
        if (player1.rect.right - self.rect.topleft[1]) <= 5 or (player1.rect.right - self.rect.left) <= 5 or (player1.rect.right - self.rect.bottomleft[1]):
            self.rect.x *= -1
        if (player2.rect.left - self.rect.topright[1]) <= 5 or (player2.rect.left - self.rect.right) <= 5 or (player2.rect.left - self.rect.bottomright[1]):
            self.rect.x *= -1
        if (player1.rect.bottomright[1] - self.rect.topleft[1]) <= 5 or (player1.rect.bottomright[1] - self.rect.left) <= 5 or (player1.rect.bottomright[1] - self.rect.bottomleft[1]):
            self.rect.x *= -1
        if (player2.rect.bottomleft[1] - self.rect.topright[1]) <= 5 or (player2.rect.bottomleft[1] - self.rect.right) <= 5 or (player2.rect.bottomleft[1] - self.rect.bottomright[1]):
            self.rect.x *= -1'''
        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.speed *= -1
            self.speed_y *= 1
        if self.rect.y < 10 or self.rect.y > 650:
            self.speed_y *= -1
class Button_PNG():
    def __init__(self,btn_image,btn_x,btn_y,w,h):
        self.image = transform.scale(image.load(btn_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = btn_x
        self.rect.y = btn_y
        self.pause_is_pressed = False

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



player1 = Player1("board.png",26,330,25,200,7)
player2 = Player2("board.png",550,330,25,200,7)
ball = Ball("ball.png",300,350,50,50,3,3)

pausebtn_png = Button_PNG("pause.png",475,5,45,45)
exitbtn_png = Button_PNG("exit.png",535,4,47,45)





font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,25)
font3 = font.Font(None,30)

lose = font1.render("YOU LOSE!",True,(255,0,0))
pause = font3.render("Pause...",True,(255,255,255))
restart = font2.render("Do you want to start over?Yes(y) or No(n)",True,(255,255,255))

mixer.init()
mixer.music.load("background_music.ogg")
mixer.music.set_volume(0.10)
mixer.music.play()

clock = time.Clock()

key_pressed_up1 = False
key_pressed_up2 = False
key_pressed_down1 = False
key_pressed_down2 = False
finish = False
game = True

player1_score = 0
player2_score = 0

while game:
    for e in event.get():
            if finish != True or pausebtn_png.pause_is_pressed != True:
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    x,y  = e.pos
                    if pausebtn_png.collidepoint(x,y):
                        pausebtn_png.pause_is_pressed = True
                        if finish != True:
                            mixer.music.stop()
                            window.blit(pause,(273,250))
                            #window.blit(hint,(325,265))
                            pausebtn_png.pause_is_pressed = False
                            finish = True
                        elif finish == True:
                                mixer.music.play()
                                finish = False
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                x,y  = e.pos
                if exitbtn_png.collidepoint(x,y):
                    game = False
            if e.type == QUIT:
                game = False
            '''if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if finish != True:
                        if num_fire < 20 and rel_time == False:
                            key_pressed = True'''
    keys_pressed = key.get_pressed()
    if keys_pressed[K_r]:
        if finish != False:
            ball.rect.y = 330
            ball.rect.x = 290
            player1.rect.y = 330
            player2.rect.y = 330
            player1_score = 0
            player2_score = 0
            finish = False
            ball.speed *= -1
            ball.speed_y *= -1
            mixer.music.play()
            
                
                     
                    
    if finish != True:
        if ball.rect.x > 530:
            player1_score += 1
            ball.rect.x = 300
            ball.rect.y = 350
            ball.speed_y *= -1
            ball.speed *= -1

        if ball.rect.x < 10:
            player2_score +=1
            ball.rect.x = 300
            ball.rect.y = 350
            ball.speed_y *= -1
            ball.speed *= -1

        text_players_score = font1.render(str(player1_score) + ":" + str(player2_score),1,(255,255,255))
        window.blit(background,(0,0))
        window.blit(text_players_score,(284,20))

        player1.reset()
        player2.reset()
        ball.reset()
        player1.control()
        player2.control()
        ball.ball_control()
        pausebtn_png.reset()
        exitbtn_png.reset()

        if player1_score == 10:
            lose = font1.render("Player2" + " LOSE!",True,(255,0,0))
            hint = font2.render("Press 'r' to restart the game...",True,(255,255,255))
            window.blit(lose,(200,355))
            window.blit(hint,(220,390))
            finish = True
        elif player2_score == 10:
            lose = font1.render("Player1" + " LOSE!",True,(255,0,0))
            hint = font2.render("Press 'r' to restart the game...",True,(255,255,255))
            window.blit(lose,(240,355))
            window.blit(hint,(220,390))
            finish = True

    clock.tick(60)
    display.update()