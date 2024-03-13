#Topic: Recycling and Global Warming

import pygame,random,time
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((800,800))
pygame.display.set_caption ('Recycling & Global Warming Project')

#Game title text functions
def gtitle (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',40)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
#Larger text function
def title (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',20)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
#Smaller text function
def subtext (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',17)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))

px,py = 375,375
bcolor = (144,238,144)
black = (0,0,0)
white = (255,255,255)
direct = 'n'
def player ():
    global px,py,direct,bag,play
    play = pygame.draw.rect (screen,(0,255,0),(px,py,50,50))
    pygame.draw.rect (screen,black,(px,py,50,50),2)
    if direct == 'n':
        pygame.draw.polygon (screen,(0,100,0),((px,py),(px+50,py),(px+50,py+10),(px+25,py+25),(px,py+10)))
        pygame.draw.rect (screen,(0,100,0),(px+50,py+10,20,20))
        pygame.draw.rect (screen,(black),(px+50,py+10,20,20),1)
        subtext (str(bag),px+56,py+10,(255,222,0))
    if direct == 's':
        pygame.draw.polygon (screen,(0,100,0),((px,py+50),(px+50,py+50),(px+50,py+40),(px+25,py+25),(px,py+40)))
        pygame.draw.rect (screen,(0,100,0),(px-20,py+20,20,20))
        pygame.draw.rect (screen,(black),(px-20,py+20,20,20),1)
        subtext (str(bag),px-14,py+20,(255,222,0))
    if direct == 'e':
        pygame.draw.polygon (screen,(0,100,0),((px,py),(px,py+50),(px+10,py+50),(px+25,py+25),(px+10,py)))
        pygame.draw.rect (screen,(0,100,0),(px+10,py-20,20,20))
        pygame.draw.rect (screen,(black),(px+10,py-20,20,20),1)
        subtext (str(bag),px+16,py+-20,(255,222,0))
    if direct == 'w':
        pygame.draw.polygon (screen,(0,100,0),((px+50,py),(px+50,py+50),(px+40,py+50),(px+25,py+25),(px+40,py)))
        pygame.draw.rect (screen,(0,100,0),(px+20,py+50,20,20))
        pygame.draw.rect (screen,(black),(px+20,py+50,20,20),1)
        subtext (str(bag),px+25,py+49,(255,222,0))

timel = 30
space = 0
pygame.time.set_timer (pygame.USEREVENT,1000)
losec = False
def timer ():
    global timel,losec,space
    pygame.draw.polygon (screen,(240,240,240),((750,10),(742,20),(742,140),(735,145),(750,160),(765,145),(758,140),(758,20)))
    if timel <= 0:
        pygame.draw.polygon (screen,(255,0,0),((750,10),(742,20),(742,140),(735,145),(750,160),(765,145),(758,140),(758,20)))
        losec = True
    elif 27 <= timel <= 30:
        space = 30 - timel
        pygame.draw.polygon (screen,(255,0,0),((750,160),(750-space*5,160-space*5),(750+space*5,160-space*5)))
    elif timel == 26:
        pygame.draw.polygon (screen,(255,0,0),((750,160),(735,145),(742,140),(758,140),(765,145)))
    elif 2 <= timel <= 25:
        space = 26 - timel
        pygame.draw.polygon (screen,(255,0,0),((750,160),(735,145),(742,140),(742,140-space*5),(758,140-space*5),(758,140),(765,145)))
    elif timel == 1:
        pygame.draw.polygon (screen,(255,0,0),((750,160),(735,145),(742,140),(742,20),(746,15),(754,15),(758,20),(758,140),(765,145)))
    pygame.draw.polygon (screen,(white),((750,10),(742,20),(742,140),(735,145),(750,160),(765,145),(758,140),(758,20)),2)

bx = random.randint (0,760)
by = random.randint (0,780)
def bottle ():
    image = pygame.image.load ('water_bottle.png')
    image = pygame.transform.scale (image,(40,20))
    screen.blit (image,(bx,by))

bag = 0
def check ():
    global bag,bx,by,px,py
    if bag < 5:
        if (px <= bx <= px + 50 or px <= bx + 40 <= px + 50) and (py <= by <= py + 50 or py <= by + 20 <= py + 50):
            bag = bag + 1
            bx = random.randint (0,760)
            by = random.randint (0,780)
    else:
        subtext ('Your bag is full! Unload it into  the recycle bin.',250,10,black)

recprox = False
def recb ():
    global bag,px,py,recprox
    pygame.draw.rect (screen,(0,51,255),(10,750,40,40))
    pygame.draw.rect (screen,(150,150,150),(10,750,40,40),1)
    pygame.draw.rect (screen,black,(15,755,30,30))
    if (0 <= px <= 70 or 0 <= px + 50 <= 70) and (730 <= py <= 800 or 730 <= py + 50 <= 800):
        title ('[E]',18,757,white)
        recprox = True
    else:
        recprox = False

stam = 200
sprint = False
exh = False
pmove = 2
def stamina ():
    global stam,sprint,exh,pmove,nmove,smove,emove,wmove,swim
    if sprint == True and exh == False and swim == False:
        pmove = 4
        if nmove == True or smove == True or emove == True or wmove == True:
            stam = stam - 1
            if stam <= 0:
                exh = True
    elif sprint == True and exh == False and swim == True:
        pmove = 3
        if nmove == True or smove == True or emove == True or wmove == True:
            stam = stam - 1
            if stam <= 0:
                exh = True
    if exh == True:
        pmove = 1
        if stam >= 100:
            exh = False
            pmove = 2
    pygame.draw.rect (screen,(white),(590,770,203,23))
    pygame.draw.rect (screen,(black),(590,770,203,23),2)
    pygame.draw.rect (screen,(0,255,255),(592,772,stam,20))
    title ('Stamina',660,770,black)

class raccoon ():
    def __init__ (self):
        self.x = random.randint (0,760)
        self.y = random.randint (0,760)
        self.move = round (random.uniform (0.5,1.5),2)
        self.direct = 'n'
    def display (self):
        global px,py,bag,play
        rac = pygame.draw.rect (screen,(50,50,50),(self.x,self.y,40,40))
        if self.direct == 'n' or self.direct == 's':
            pygame.draw.rect (screen,(white),(self.x,self.y+15,40,10))
        else:
            pygame.draw.rect (screen,(white),(self.x+15,self.y,10,40))

        if px > self.x - 8:
            self.direct = 'w'
            self.x = self.x + self.move
        if py > self.y - 8:
            self.direct = 'n'
            self.y = self.y + self.move
        if px < self.x - 8:
            self.direct = 'e'
            self.x = self.x - self.move
        if py < self.y - 8:
            self.direct = 's'
            self.y = self.y - self.move
        if rac.colliderect (play):
            if bag != 0:
                bag = bag - 1
            self.x = random.randint (0,760)
            self.y = random.randint (0,760)

def bench ():
    global px,py,stam,nmove,smove,emove,wmove
    image1 = pygame.image.load ('bench.png')
    image1 = pygame.transform.scale (image1,(80,40))
    screen.blit (image1,(80,750))
    if (80 <= px <= 170 or 80 <= px + 50 <= 170) or (730 <= py <= 800 or 730 <= py + 50 <= 800):
        if nmove == False and smove == False and emove == False and wmove == False and stam < 200:
            stam = stam + 1.5
            if stam >= 200:
                stam = 200
                exh = False
                pmove = 2

swim = False
def lake ():
    global px,py,stam,pmove,timel,exh,swim
    if 20 < timel <= 30:
        pygame.draw.rect (screen,(87,157,166),(700,640,200,80))
        pygame.draw.circle (screen,(87,157,166),(700,680),40)
    elif 10 < timel <= 20:
        pygame.draw.rect (screen,(87,157,166),(700,650,200,60))
        pygame.draw.circle (screen,(87,157,166),(700,680),30)
    elif 0 < timel <= 10:
        pygame.draw.rect (screen,(87,157,166),(700,660,200,40))
        pygame.draw.circle (screen,(87,157,166),(700,680),20)
    #Add player slowdown
    if 660 <= px + 50 <= 800 and (680 <= py <= 720 or 680 <= py + 50 <= 720):
        swim = True
    else:
        swim = False
    if swim == True:
        pmove = 1
        if nmove == True or smove == True or emove == True or wmove == True:
            stam = stam - 0.5
            if stam <= 0:
                exh = True
        if nmove == False and smove == False and emove == False and wmove == False and stam < 200:
            stam = stam + 2
            if stam >= 200:
                stam = 200
                exh = False
                pmove = 2
    else:
        pmove = 2

rlist = []
nmove = False
smove = False
emove = False
wmove = False
deposit = False
spawned = False
clock = pygame.time.Clock ()
score = 0
while True:
    screen.fill (bcolor)
    clock.tick (60)
    bench ()
    pygame.draw.circle (screen,(160,82,45),(700,680),42)
    pygame.draw.rect (screen,(160,82,45),(698,638,200,84))
    lake ()
    player ()
    timer ()
    recb ()
    check ()
    stamina ()
    bottle ()
    title ('Score: '+str(score),2,0,black)

    for loop in range (0,len(rlist),1):
        rlist[loop].display ()
    
    for event in pygame.event.get ():
        if event.type == pygame.USEREVENT:
            timel = timel - 1
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                nmove = True
            if event.key == K_s:
                smove = True
            if event.key == K_a:
                emove = True
            if event.key == K_d:
                wmove = True
            if event.key == K_e:
                deposit = True
            if event.key == K_LSHIFT:
                sprint = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                nmove = False
            if event.key == K_s:
                smove = False
            if event.key == K_a:
                emove = False
            if event.key == K_d:
                wmove = False
            if event.key == K_e:
                deposit = False
            if event.key == K_LSHIFT:
                sprint = False
                pmove = 2
    if nmove == True:
        direct = 'n'
        py = py - pmove
        if py <= 0:
            py = 0
    if smove == True:
        direct = 's'
        py = py + pmove
        if py >= 750:
            py = 750
    if emove == True:
        direct = 'e'
        px = px - pmove
        if px <= 0:
            px = 0
    if wmove == True:
        direct = 'w'
        px = px + pmove
        if px >= 750:
            px = 750
    if nmove == False and smove == False and emove == False and wmove == False and stam < 200:
        stam = stam + 1
        if stam >= 200:
            stam = 200
            exh = False
            pmove = 2
    if exh == True and (nmove == True or smove == True or emove == True or wmove == True) and stam < 200:
        stam = stam + 0.5
        if stam >= 200:
            stam = 200
            exh = False
            pmove = 2
    if deposit == True and recprox == True:
        score = score + (bag * 10)
        timel = timel + (bag * 5)
        bag = 0
        spawned = False
        if timel > 30:
            timel = 30

    if score % 100 == 0 and score != 0 and spawned == False:
        rlist.append (raccoon ())
        spawned = True

    pygame.display.update ()

    ask = True
    scores = []
    if losec == True:
        time.sleep (3)
        screen.fill (bcolor)
        title ('Oh no! You ran out of time.',290,350,(255,0,0))
        subtext ('Your score was '+str(score)+'.',330,380,black)
        hscore = open ('High_Score.txt','r+')
        for loop in hscore:
            scores.append (int (loop))
        highest = max (scores)
        if highest < score:
            title ('New High Score!',325,410,(255,222,0))
            hscore.write (str(score)+'\n')
        elif highest == score:
            title ('Ooh, you got the same as you\'re High Score.',225,410,(255,222,0))
        elif highest > score:
            title ('You\'re previous High Score was '+str (highest)+'.',260,410,(255,222,0))
        pygame.draw.rect (screen,(255,255,0),(100,470,150,30))
        pygame.draw.rect (screen,(255,0,0),(550,470,150,30))
        pygame.draw.rect (screen,(black),(100,470,150,30),2)
        pygame.draw.rect (screen,(black),(550,470,150,30),2)
        title ('Retry?',150,475,black)
        title ('Quit',610,475,black)
        while ask == True:
            for event in pygame.event.get ():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx,my = event.pos
                    if 100 <= mx <= 250 and 470 <= my <= 500:
                        losec = False
                        ask = False
                        score = 0
                        stam = 200
                        px = 375
                        py = 375
                        pmove = 2
                        bx = random.randint (0,760)
                        by = random.randint (0,780)
                        timel = 30
                        bag = 0
                        direct = 'n'
                        nmove = False
                        smove = False
                        emove = False
                        wmove = False
                        sprint = False
                        exh = False
                    if 550 <= mx <= 700 and 470 <= my <= 500:
                        pygame.quit ()
                        quit ()
            pygame.display.update ()

hscore.close ()
pygame.display.update ()
