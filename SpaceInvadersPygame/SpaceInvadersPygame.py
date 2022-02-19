# imports (sometimes unused)
import pygame
import time

# defining colors
colorblack=(0,0,0);
colorwhite=(255,255,255);
colorred=(255,0,0);
colorgreen=(0,255,0);
colorblue=(0,0,255);
colorpurple=(129,0,184);

# screen settings
pygame.init();
window=pygame.display.set_mode((800,800));
pygame.display.set_caption("Space Invaders");
window.fill(colorblack);
clock=pygame.time.Clock();
fps=75;

# Playermodel class
class Playermodel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__();
        self.img=pygame.Surface((20,20));
        self.img.fill(colorpurple);
        self.rect=self.img.get_rect();
        self.rect.x=380;
        self.rect.y=760;

    def draw(self):
        window.blit(self.img,(self.rect.x,self.rect.y));

# enemy (alien) class
class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__();
        self.img=pygame.Surface((20,20));
        self.img.fill(colorred);
        self.rect=self.img.get_rect();
        self.rect.x=x;
        self.rect.y=y;

    def draw(self):
        window.blit(self.img,(self.rect.x,self.rect.y));
        self.rect.y=self.rect.y+1;

# projectile (bullet) class
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__();
        self.img=pygame.Surface((2,5));
        self.img.fill((255,255,0));
        self.rect=self.img.get_rect();
        self.rect.x=x;
        self.rect.y=y;
    def draw(self):
        window.blit(self.img,(self.rect.x,self.rect.y));
        self.rect.y=self.rect.y-3;
    
    def contact(self,al):
        if al.rect.y+20>self.rect.y and al.rect.x+20<self.rect.x and al.rect.x<self.rect.x+2:
            return True;
        else:
            return False;

        
# entity spawining
aliens=[];
bullets=[];
p1=Playermodel();
for j in range(3):
    for i in range(25):
        alien1=Alien(i*30+30,j*30+30);
        aliens.append(alien1);

# main game loop
gamestate=True;
while gamestate==True:
    clock.tick(fps);
    p1.draw();
    if p1.rect.x<0:
        p1.rect.x=0;
    if p1.rect.x>780:
        p1.rect.x=780;
    for al in aliens:
        al.draw();
    keys=pygame.key.get_pressed();
    if keys[pygame.K_RIGHT]==True:
        p1.rect.x=p1.rect.x+5;
    elif keys[pygame.K_LEFT]==True:
        p1.rect.x=p1.rect.x-5;
    elif keys [pygame.K_SPACE]:
        shot=Bullet(p1.rect.x+10,p1.rect.y-10);
        bullets.append(shot);
    for i in bullets:
        for alien in aliens:
            if i.contact(alien):
                bullets.remove(i);
                aliens.remove(alien);
        i.draw();
    for shot in bullets:
        shot.draw();
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False;
    pygame.display.update();
    window.fill(colorblack);
