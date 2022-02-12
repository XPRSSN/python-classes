#importing pygame and bloatware
import pygame
import time


#racism
colorblack=(0,0,0);
colorwhite=(255,255,255);


#setting a monitor cause its not terminal friendly
pygame.init();
win=pygame.display.set_mode((800,800));
pygame.display.set_caption("pong");
clock=pygame.time.Clock();


#making a playermodel and hoping that GKI won't find a way to break it again
class PlayerModel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__();
        self.img=pygame.Surface((10,80));
        self.img.fill(colorwhite);
        self.rect=self.img.get_rect();
        self.x=0;
        self.y=0;

    def move(self):
        self.rect.move_ip(self.x , self.y);


class BallModel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__();
        self.img=pygame.Surface((10,10));
        self.img.fill(colorwhite);
        self.rect=self.img.get_rect();
        self.x=0;
        self.y=0;

    def move(self):
        self.rect.move_ip(self.x , self.y);
        if self.rect.y<5 or self.rect.y>795:
            self.y=self.y*-1;
        


p=PlayerModel(); # player controlled by WASD
p.rect.x=10;
p.rect.y=360;
p2=PlayerModel(); # player controlled by arrow keys
p2.rect.x=780;
p2.rect.y=360;
b=BallModel(); # ball
b.rect.x=390;
b.rect.y=390;
b.x=1;
b.y=2;
fps=75;
scorep=0;
scorep2=0;

# making mattcs and zuhn proud by making some shitty asf movemInt mechs
while scorep<5 and scorep2<5:
    pygame.display.update();
    win.fill(colorblack);
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                p.y=p.y - 10;
            elif i.key == pygame.K_s:
                p.y=p.y + 10;
            elif i.key == pygame.K_UP:
                p2.y=p2.y - 10;
            elif i.key == pygame.K_DOWN:
                p2.y=p2.y + 10;
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_w or i.key == pygame.K_s:
                p.y=0;
            elif i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                p2.y=0;

    if p.rect.y < 0:
        p.rect.y=0;
    if p.rect.y > 720:
        p.rect.y=720;
    if p2.rect.y<0:
        p2.rect.y=0;
    if p2.rect.y>720:
        p2.rect.y=720;

    if b.rect.y>p.rect.y-10 and b.rect.y<p.rect.y+80 and b.rect.x<p.rect.x+10:
        b.x = b.x*-1;

    if b.rect.y>p2.rect.y-10 and b.rect.y<p2.rect.y+80 and b.rect.x>p2.rect.x-10:
        b.x = b.x*-1;

    if b.rect.x<5:
        b.rect.x=395;
        b.rect.y=395;
        scorep=scorep+1;
        print("P1 score is now:", scorep);
    elif b.rect.x>795:
        b.rect.y=395;
        b.rect.x=395;
        scorep2=scorep2+1;
        print("P2 score is now:", scorep2);

    font=pygame.font.Font(None,70);
    text=font.render(str(scorep), 1, colorwhite);
    win.blit(text,(10,10));
    text=font.render(str(scorep2), 1 ,colorwhite);
    win.blit(text,(760,10));

    p.move();
    p2.move();
    b.move();
    win.blit(p.img , p.rect);
    win.blit(p2.img, p2.rect);
    win.blit(b.img, b.rect);
    clock.tick(fps);
