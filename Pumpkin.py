import pygame
import random
pygame.init()
clock=pygame.time.Clock()

#настройки экрана
background = pygame.image.load("Background.png")
HIGH=background.get_height()
SIZE=background.get_width()
gamedisplay=pygame.display.set_mode((SIZE, HIGH))
pygame.display.set_caption("Pumpkin")


#тыква
pumpkin=pygame.image.load("pumpkin_face_off.png").convert_alpha()
pumpkin_rect = pumpkin.get_rect()
speedX = 1
speedY = 1

#описание прямоугольника
surf = pygame.Surface((100,20))
surf.fill((199,9,99))
rect = surf.get_rect()
rect.bottom = HIGH

RECS = 3

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
exit = False
game = True

best_time = 0
best_score = 0

while not exit:
    clock.tick(60)


    #настройка выхода из игры
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit = True
    keys = pygame.key.get_pressed()
    if game:

        gamedisplay.blit(background, (0, 0))
        #настройки тыквы
        pumpkin_rect.x+=speedX
        pumpkin_rect.y+=speedY

        if pumpkin_rect.bottom >= HIGH: #Коснулись земли
            text3 = font2.render("YOU LOSE, it's your score:" + str(bonus)+", time:"+str(sec), True, (250, 134, 46))
            gamedisplay.blit(text3, (0,300 ))
            game = False

        if pumpkin_rect.left <= 0 or pumpkin_rect.right >= SIZE : #Левый и правый край
            speedX*=-1

        if pumpkin_rect.top<= 0:
            speedY*=-1


        #настройки прямоугольниика

        if keys[pygame.K_LEFT] and rect.left > 0:
            rect.x -= RECS
        if keys[pygame.K_RIGHT] and rect.right < SIZE:
            rect.x += RECS


        #настройки соударений
        if rect.top == pumpkin_rect.bottom and pumpkin_rect.right > rect.left and pumpkin_rect.left < rect.right:
            speedY *=-1

        if pumpkin_rect.colliderect(basketRECT):
            bonus += 1
            pumpkin_rect.x = 1
            pumpkin_rect.y = 1
            basketRECT.x = random.randint(0,SIZE - basketRECT.width)
            basketRECT.y = random.randint(0,HIGH - basketRECT.height)



        #Вывод бонусов на экран
        text_bonus = font1.render("bonus=" + str(bonus), True, (250, 134, 46))
        gamedisplay.blit(text_bonus, (600, 0))

        #Вывод времени на экран
        sec = pygame.time.get_ticks() // 1000
        text_time = font1.render("time:" + str(sec), True, (250, 134, 46))
        gamedisplay.blit(text_time, (600, 50))

        #Вывод спрайтов
        gamedisplay.blit(surf,rect)
        gamedisplay.blit(basket, (basketRECT.x, basketRECT.y))
        gamedisplay.blit(pumpkin, (pumpkin_rect.x, pumpkin_rect.y))
        pygame.display.update()


pygame.quit()
    
