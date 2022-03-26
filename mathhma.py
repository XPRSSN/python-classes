# LIBS
import pygame
from random import *
import time


# module and window init
pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Memory Game")
colorblack=(0,0,0)
colorwhite=(255,255,255)
window.fill(colorblack)


# cards class
class Card(pygame.sprite.Sprite):
    def __init__(self,x,y,number):
        super().__init__()
        self.x = x
        self.y = y
        self.number = number
        self.image= pygame.Surface((100,100))
        self.image.fill((colorwhite))
        self.rect = self.image.get_rect()

    def draw(self):
        window.blit(self.image,(self.x,self.y))
    

# possible nums generation
numbers=[]
for j in range(2):
    for i in range(10):
        numbers.append(i)
shuffle(numbers)

cards=[]
for i in range(4):
    for j in range(5):
        c = Card(10+110*j,10+110*i,numbers[0])
        numbers.remove(numbers[0])
        cards.append(c)

run = True
mousePos = [0,0]
pressed = []
correct=[]
wrong=[]
font = pygame.font.SysFont("Arial", 50)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    for c in cards:
        c.draw()
    mouse = pygame.mouse.get_pressed()#(False,False,False)
    if mouse[0] == True:
        mousePos = list(pygame.mouse.get_pos())

    for card in cards: 
        if mousePos[0] > card.x and mousePos[0]  < card.x + 100 and mousePos[1] > card.y and mousePos[1]  < card.y + 100:
            if len(pressed)<2 and card not in pressed and card not in correct:
                pressed.append(card)
            
    for pressedCard in pressed:
        number = font.render(str(pressedCard.number), False, colorblack) 
        window.blit(number, (pressedCard.x + 40, pressedCard.y + 40))

    if len(pressed)==2:
        if pressed[0].number==pressed[1].number:
            correct.append(pressed[0])
            correct.append(pressed[1])
        else:
            wrong.append(pressed[0])
            wrong.append(pressed[1])
        pressed.clear()
    
    for cor in correct:
        number = font.render(str(cor.number), False, (0,255,0)) 
        window.blit(number, (cor.x + 40, cor.y + 40))
    
    for wcard in wrong:
        number = font.render(str(wcard.number), False, (255,0,0)) 
        window.blit(number, (wcard.x + 40, wcard.y + 40))
    

    pygame.display.update()
    if len(wrong)>0:
        time.sleep(0.4)
        wrong.clear()
