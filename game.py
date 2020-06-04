import pygame
import random 

pygame.init()
gameDisplay = pygame.display.set_mode((600,400))
pygame.display.set_caption('GAME')
clock = pygame.time.Clock()

randomx= random.randint(0,200)
randomy= random.randint(0,200)
crandomx= random.randint(0,500)
crandomy= random.randint(0,500)

dead = False

while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            #print(event)    
    
    pygame.draw.rect(gameDisplay,(225,0,255),(randomx,randomy,20,20))
    pygame.draw.circle(gameDisplay,(255,255,0),(crandomx,crandomy),10,10)
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and randomy > 20:
        randomy -=0.02
    if key[pygame.K_s] and randomy < 350:
        randomy +=0.02
    if key[pygame.K_d] and randomx<550:
        randomx +=0.02
    if key[pygame.K_a] and randomx>20:
        randomx -=0.02
    if(abs(randomx-crandomx)<30 and abs(randomy - crandomy)<30):
       pygame.draw.circle(gameDisplay,(255,0,255),(crandomx,crandomy),10,10)
    
    pygame.display.update()
    gameDisplay.fill((0,0,0))
    
pygame.quit()
