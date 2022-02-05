import pygame 
import time
import random

pygame.init();

colorblack=(0,0,0,);
colorwhite=(255,255,255);
colorred=(255,0,0);
colorblue=(0,0,255);
colorgreen=(0,255,0);

wn=pygame.display.set_mode((800,800));
pygame.display.set_caption("Space Invaders");
wn.fill((colorblack));
clock=pygame.time.Clock();
fps=75


class Playermodel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__();
        self.img=pygame.Surface((20,20));
        self.img.fill(colorwhite);
        self.rect=self.img.get_rect();
        self.rect.x=380;
        self.rect.y=760;

    def draw(self):
        wn.blit(self.img, (self.rect.x, self.rect.y));

class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__();
        self.img = pygame.Surface((5,5));
        self.img.fill(colorred);
        self.rect=self.img.get_rect();
        self.rect.x=x;
        self.rect.y=y;

    def draw(self):
        wn.blit(self.img, (self.rect.x,self.rect.y));
        self.rect.y=self.rect.y+1;

p1=Playermodel();
alien=Alien(30,30)

gamestate=True;
while(gamestate==True):
    clock.tick(fps);
    p1.draw();
    alien.draw();
    keys=pygame.key.get_pressed();
    if keys[pygame.K_RIGHT]==True:
        p1.rect.x=p1.rect.x+5;
    elif keys[pygame.K_LEFT]==True:
        p1.rect.x=p1.rect.x-5;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamestate=False;
    pygame.display.update();
