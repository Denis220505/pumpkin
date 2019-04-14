import pygame
import random
pygame.init()
clock=pygame.time.Clock()
#настройки экрана
#RED=(255,0,0)
background = pygame.image.load("Background.png")
HIGH=600
SIZE=800
gamedisplay=pygame.display.set_mode((SIZE, HIGH))
pygame.display.set_caption("Hello")
#тыква
pumpkin=pygame.image.load("pumpkin_face_off.png")
pumpkin_rect = pumpkin.get_rect()
speedX = 1
speedY = 1
#описание прямоугольника
surf = pygame.Surface((100,20))
surf.fill((199,9,99))
rect = surf.get_rect()
rect.bottom = HIGH
RECW = 100
RECH = 20
RECX = 0
RECY = HIGH - RECH
RECS = 3
RECL = RECX
RECR = RECX + RECW
#описание корзины
basket = pygame.image.load("basket.png")
basket = pygame.transform.scale(basket,(50,50))
basketRECT = basket.get_rect()
basketRECT.x = 400
basketRECT.y = 0
basket.set_colorkey((255,255,255))
#бонусы
bonus = 0
#настройки шрифтов
pygame.font.init()
font1 = pygame.font.SysFont(None,50)
font2 = pygame.font.SysFont('Comic Sans MS',50)

#настройки игры
game = True

while game:
    text1 = font1.render("bonus="+str(bonus),True,(250,134,46))
    gamedisplay.blit(text1,(600,0))
    sec = pygame.time.get_ticks()//1000
    text2 = font1.render("time:"+str(sec),True,(250,134,46))
    gamedisplay.blit(text2,(600,50))
    
    gamedisplay.blit(basket,(basketRECT.x,basketRECT.y))
#настройка выхода из игры
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
#настройки тыквы
    pumpkin_rect.x+=speedX
    pumpkin_rect.y+=speedY
    if pumpkin_rect.bottom >= HIGH:
        text3 = font2.render("YOU LOSE,it's your score:" + str(bonus)+"time"+str(sec), True, (250, 134, 46))
        gamedisplay.blit(text3, (0,300 ))
    if pumpkin_rect.right >= SIZE:
        speedX*=-1
    if pumpkin_rect.top<= 0:
        speedY*=-1
    if pumpkin_rect.left <= 0:
        speedX*=-1
    
    gamedisplay.blit(pumpkin, (pumpkin_rect.x, pumpkin_rect.y))
    #настройки прямоугольниика
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect.x > 0:
        rect.x -= RECS
    if keys[pygame.K_RIGHT] and rect.right < SIZE:
        rect.x += RECS
    
    gamedisplay.blit(surf,rect)
    #настройки соударений
    if rect.top == pumpkin_rect.bottom and pumpkin_rect.right > rect.left and pumpkin_rect.left < rect.right:
        speedY *=-1
    if pumpkin_rect.colliderect(basketRECT):
        bonus += 1
        pumpkin_rect.x = 100
        pumpkin_rect.y = 100
        basketRECT.x = random.randint(0,SIZE - basketRECT.width)
        basketRECT.y = random.randint(0,HIGH - basketRECT.height)

    pygame.display.update()
    gamedisplay.blit(background,(0,0))
    clock.tick(60)
pygame.quit()
    
