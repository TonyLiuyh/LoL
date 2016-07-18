from pygame import *
import pygame
import time
from math import *
import math
import random

#Initialize the game
pygame.init()

#Create the screen
screen = pygame.display.set_mode((1000, 600))

#Definde key for moving
key = [False, False, False, False]

#Load images
Ez = pygame.image.load("images/ez.jpg")
G = pygame.image.load("images/G.jpg")
H = pygame.image.load("images/H.jpg")
J = pygame.image.load("images/J.jpg")
K1 = pygame.image.load("images/K1.png")
K2 = pygame.image.load("images/K2.jpg")
L1 = pygame.image.load("images/L1.png")
L2 = pygame.image.load("images/L2.jpg")
M = pygame.image.load("images/Monster.png")
H_ex = pygame.image.load("images/H-explode.png")
Bg = pygame.image.load("images/bg.png")
Mon = pygame.image.load("images/Mons.png")
defeat = pygame.image.load("images/defeat.png")
Warrior = pygame.image.load("images/Warrior.png")
Wizard = pygame.image.load("images/Wizard.png")
Level = pygame.image.load("images/Level.png")
score=0
Exp=0
Lv = 1
#Victory = pygame.image.load("images/victory.png")

#Vary the scale of images
LOL = pygame.transform.scale(Ez, (100, 100))
Monster = pygame.transform.scale(M, (75, 75))
bg = pygame.transform.scale(Bg, (1000, 600))
NormalAttack = pygame.transform.scale(G, (50, 50))
Ability_h = pygame.transform.scale(H, (50, 50))
Ability_j = pygame.transform.scale(J, (50, 50))
Ability_k = pygame.transform.scale(K2, (50, 50))
Ability_l = pygame.transform.scale(L2, (50, 50))
Skill_h = pygame.transform.scale(H, (50, 50))
Skill_k = pygame.transform.scale(K1, (50, 50))
Skill_l = pygame.transform.scale(L1, (80, 80))
H_explode = pygame.transform.scale(H_ex, (75, 75))
Monst = pygame.transform.scale(Mon, (25, 25))
level = pygame.transform.scale(Level, (90, 90))
#victory = pygame.transform.scale(Victory, (800, 670))

#Set the initial values of images' positions
Abilityh_x = 1000
Abilityh_y = 600
Abilityk_x = [1000, 1000, 1000, 1000, 1000, 1000, 1000]
Abilityk_y = [600, 600, 600, 600, 600, 600, 600]
Abilityl_x = 1000
Abilityl_y = 600
defeatRect = defeat.get_rect()
defeatRect.center = (500, 300)
levelRect = level.get_rect()
#victoryRect = victory.get_rect()
#victoryRect.center = (500, 300)
lolx = 100
loly = 100
def Fibonacci(x):
    a1 = 1
    a2 = 1
    a3 = 2
    for i in range(x - 1):
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    return(a3 * 10)

#Set the cooldown time
cd_g = 0
cd_h = 0
cd_j = 0
cd_k = 0
cd_l = 0
def zhengchangmoshi():
    global cdh, cdj, cdk, cdl
    cdh = 3000
    cdj = 10000
    cdk = 6000
    cdl = 30000
    atkrate = 1
def wuxianhuoli():
    global cdh, cdj, cdk, cdl
    cdh = 1000
    cdj = 1000
    cdk = 1000
    cdl = 1000
    atkrate = 10
zhengchangmoshi()

#Distance function
def distance(x1, y1, x2, y2):
    return(math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1) * (y2 - y1)))
    


Monsters = []
Mons = []
badtimer = 0
MonHp = 500
listg = []
listk = []
atkrate = 1
minimum = 250
gg = [0, 0]
b = 0
explode = [0, 0]
exist_ex = 0
dmg_l = 800
cdreductionj = 0
cdreductionk = 0
cdreductionl = 0
ang = 0
healthRect = (250, 550, 500, 20)
healthlength = 496
totalHP = 10000
lolHP = totalHP
for i in range(7):
    listk.append((i, i))
    
    
while 1:
    if lolHP <= 0:
        screen.blit(defeat, defeatRect)
        break
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), healthRect, 0)
    if b:
        screen.blit(H_explode, exRect)
    screen.blit(LOL, (lolx, loly))
    levelRect.center = (lolx + 50, loly)
    screen.blit(level, levelRect)
    screen.blit(Skill_h, (Abilityh_x, Abilityh_y))
    screen.blit(Skill_l, (Abilityl_x, Abilityl_y))
    font1 = pygame.font.Font(None, 36)
    Levelnumber = font1.render(str(Lv).zfill(2),True,(255, 0, 0))
    lvRect = Levelnumber.get_rect()
    lvRect.center= (lolx + 50, loly + 5)
    screen.blit(Levelnumber, lvRect)
    for skill in range(7):
        screen.blit(Skill_k, (Abilityk_x[skill], Abilityk_y[skill]))
    screen.blit(Ability_h, (0, 550))
    screen.blit(Ability_j, (50, 550))
    screen.blit(Ability_k, (100, 550))
    screen.blit(Ability_l, (150, 550))
    for g in listg:
        screen.blit(NormalAttack, (g[0], g[1]))
    if badtimer==0:
        Monsters.append([1000, random.randint(0,475), MonHp, 0])
        badtimer=100
    index = 0
    index1 = 0
    hRect = Skill_h.get_rect()
    hRect.left = Abilityh_x
    hRect.top = Abilityh_y
    lRect = Skill_l.get_rect()
    lRect.left = Abilityl_x
    lRect.top = Abilityl_y
    for guys in Monsters:
        if guys[0] < -75:
            Monsters.pop(index)
        if guys[2] <= 0:
            score += 100
            Monsters.pop(index)
            Exp +=10
        if distance(guys[0], guys[1], lolx, loly) <= 400 and distance(guys[0], guys[1], lolx, loly) >= 200:
            if guys[0] - lolx != 0:
                ang = math.tan((guys[1] - loly) / (guys[0] - lolx))
            guys[0] -= 2 * cos(ang)
            guys[1] -= 2 * sin(ang)
        if distance(guys[0], guys[1], lolx, loly) > 400:
            guys[0] -= 2
        if distance(guys[0], guys[1], lolx, loly) <= 200:
            if guys[3] == 0:
                if guys[0] + 37.5 - lolx - 50 != 0:
                    angl = tan((guys[1] + 37.5 - loly - 50)/(guys[0] + 37.5 - lolx - 50))
                else:
                    angl = 0
                Mons.append([guys[0] + 37.5 - 12.5, guys[1] + 37.5 - 12.5, angl])
                guys[3] = 100
        guyRect = pygame.Rect(Monster.get_rect())
        guyRect.left = guys[0]
        guyRect.top = guys[1]
        if hRect.colliderect(guyRect):
            exRect = H_explode.get_rect()
            exRect.center = ((guyRect.center[0] + Abilityh_x + 50)/ 2, (guyRect.center[1] + Abilityh_y + 50)/ 2)
            guys[2] -= 700
            Abilityh_x = 1000
            Abilityh_y = 600
            time_ex = pygame.time.get_ticks()
            exist_ex = 500
            cdreductionj += 1000
            cdreductionk += 1000
            cdreductionl += 1000
        if lRect.colliderect(guyRect):
            guys[2] -= dmg_l
            dmg_l -= 150
            if dmg_l < 350:
                dmg_l = 350
        for skill in range(7):
            kRect = Skill_k.get_rect()
            kRect.left = Abilityk_x[skill]
            kRect.top = Abilityk_y[skill]
            if kRect.colliderect(guyRect):
                guys[2] -= 400
                Abilityk_x[skill] = 1000
                Abilityk_y[skill] = 600
        index += 1

    
    healthlength = 496 * lolHP / totalHP
    
    for guys in Monsters:
        screen.blit(Monster, (guys[0], guys[1]))
        if guys[3] != 0:
            guys[3] -= 1
    for m in Mons:
        screen.blit(Monst, (m[0], m[1]))
    for g in listg:
        minimum = 250
        for guys in Monsters:
            if distance(g[0], g[1], guys[0], guys[1]) <= 250:
                if distance(g[0], g[1], guys[0], guys[1]) < minimum:
                    minimum = distance(g[0], g[1], guys[0], guys[1])
                    if guys[0] - g[0] != 0:
                        g[2] = atan((guys[1] - g[1])/(guys[0] - g[0]))
        g[0] += 2 * cos(g[2]) * 4
        g[1] += 2 * sin(g[2]) * 4
        if g[0] < -50 or g[0] > 1000 or g[1] < -50 or g[1] > 600:
            listg.pop(index1)
        gRect = pygame.Rect(NormalAttack.get_rect())
        gRect.left = g[0]
        gRect.top = g[1]
        for guys in Monsters:
            guyRect = pygame.Rect(Monster.get_rect())
            guyRect.left = guys[0]
            guyRect.top = guys[1]
            if gRect.colliderect(guyRect):
                guys[2] -= 100
                if listg != []:
                    listg.pop(index1)
        index1 += 1
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                key[0] = True
            elif event.key == K_s:
                key[1] = True
            elif event.key == K_a:
                key[2] = True
            elif event.key == K_d:
                key[3] = True
            elif event.key == K_g:
                if cd_g == 0:
                    listg.append([lolx + 50, loly + 50, 0])
                    time_g = pygame.time.get_ticks()
                    cdg = 1000 / atkrate
                    cd_g = cdg
            elif event.key == K_h:
                if cd_h == 0:
                    Abilityh_x = lolx + 100
                    Abilityh_y = loly + 20
                    time_h = pygame.time.get_ticks()
                    cd_h = cdh
            elif event.key == K_j:
                if cd_j == 0:
                    position = pygame.mouse.get_pos()
                    lolx = position[0] - LOL.get_width()/2
                    loly = position[1] - LOL.get_height()/2
                    time_j = pygame.time.get_ticks()
                    cd_j = cdj
            elif event.key == K_k:
                if cd_k == 0:
                    for skill in range(7):
                        Abilityk_x[skill] = lolx + 100
                        Abilityk_y[skill] = loly + 20
                        time_k = pygame.time.get_ticks()
                        cd_k = cdk
            elif event.key == K_l:
                if cd_l == 0:
                    Abilityl_x = lolx + 10
                    Abilityl_y = loly + 10
                    time_l = pygame.time.get_ticks()
                    cd_l = cdl
            elif event.key == K_1:
                wuxianhuoli()
            elif event.key == K_2:
                zhengchangmoshi()
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                key[0] = False
            if event.key == K_s:
                key[1] = False
            if event.key == K_a:
                key[2] = False
            if event.key == K_d:
                key[3] = False
    lolcolliderect = pygame.Rect(lolx + 25, loly + 25, 50, 50)
    index3 = 0
    for m in Mons:
        mRect = pygame.Rect(m[0], m[1], 25, 25)
        if lolcolliderect.colliderect(mRect):
            Mons.pop(index3)
            lolHP -= 200
        else:
            m[0] -= 3 * cos(m[2])
            m[1] -= 3 * sin(m[2])
        index3 += 1
                
    if lolx < 0:
        lolx = 0
    if lolx > 900:
        lolx = 900
    if loly < 0:
        loly = 0
    if loly > 450:
        loly = 450
    if key[0] == True:
        loly -= 4
    if key[1] == True:
        loly += 4
    if key[2] == True:
        lolx -= 4
    if key[3] == True:
        lolx += 4
    if exist_ex > 0:
        exist_ex = 500 - (pygame.time.get_ticks() - time_ex)
        b = 1
    else:
        exist_ex = 0
        b = 0
    if Abilityh_x < 1000:
        Abilityh_x += 20
    for skill in range(7):
        if Abilityk_x[skill] < 1000 and Abilityk_y[skill] < 600:
            if skill == 0:
                Abilityk_x[skill] += 2 * 4
                Abilityk_y[skill] -= 3.46 * 4
            if skill == 1:
                Abilityk_x[skill] += 4 * 0.77 * 4
                Abilityk_y[skill] -= 4 * 0.64 * 4
            if skill == 2:
                Abilityk_x[skill] += 4 * 0.94 * 4
                Abilityk_y[skill] -= 4 * 0.34 * 4
            if skill == 3:
                Abilityk_x[skill] += 4 * 4
            if skill == 4:
                Abilityk_x[skill] += 4 * 0.94 * 4
                Abilityk_y[skill] += 4 * 0.34 * 4
            if skill == 5:
                Abilityk_x[skill] += 4 * 0.77 * 4
                Abilityk_y[skill] += 4 * 0.64 * 4         
            if skill == 6:
                Abilityk_x[skill] += 2 * 4
                Abilityk_y[skill] += 3.46 * 4
    if Abilityl_x < 1000:
        Abilityl_x += 20
    else:
        dmg_l = 800

    if Exp >= Fibonacci(Lv):
        Lv += 1
        Exp = 0

    font = pygame.font.Font(None, 24)
    Abilityh_cd = font.render(str(cd_h//1000+1).zfill(2), True, (255, 255, 255))
    texthRect = Abilityh_cd.get_rect()
    texthRect.center = (Ability_h.get_width()/2, screen.get_height()-Ability_h.get_height()/2)
    Abilityj_cd = font.render(str(cd_j//1000+1).zfill(2), True, (255, 255, 255))
    textjRect = Abilityj_cd.get_rect()
    textjRect.center = (Ability_j.get_width()*3/2, screen.get_height()-Ability_j.get_height()/2)
    Abilityk_cd = font.render(str(cd_k//1000+1).zfill(2), True, (255, 255, 255))
    textkRect = Abilityk_cd.get_rect()
    textkRect.center = (Ability_k.get_width()*5/2, screen.get_height()-Ability_k.get_height()/2)
    Abilityl_cd = font.render(str(cd_l//1000+1).zfill(2), True, (255, 255, 255))
    textlRect = Abilityl_cd.get_rect()
    textlRect.center = (Ability_l.get_width()*7/2, screen.get_height()-Ability_l.get_height()/2)
    score_display= font.render("Score: " +str(score).zfill(2),True,(255,255,255))
    scoreRect = score_display.get_rect()
    scoreRect.center= (500,30)
    screen.blit(score_display, scoreRect)
    
    if cd_h > 0:
        Ability_h.set_alpha(150)
        cd_h = cdh - (pygame.time.get_ticks() - time_h)
        screen.blit(Abilityh_cd, texthRect)
    else:
        cd_h = 0
        Ability_h.set_alpha(255)

    if cd_j > 0:
        Ability_j.set_alpha(150)
        cd_j = cdj - (pygame.time.get_ticks() - time_j) - cdreductionj
        screen.blit(Abilityj_cd, textjRect)
    else:
        cd_j = 0
        Ability_j.set_alpha(255)
        cdreductionj = 0

    if cd_k > 0:
        Ability_k.set_alpha(150)
        cd_k = cdk - (pygame.time.get_ticks() - time_k) - cdreductionk
        screen.blit(Abilityk_cd, textkRect)
    else:
        cd_k = 0
        Ability_k.set_alpha(255)
        cdreductionk = 0

    if cd_g > 0:
        cd_g = cdg - (pygame.time.get_ticks() - time_g)
    else:
        cd_g = 0
    
    if cd_l > 0:
        Ability_l.set_alpha(150)
        cd_l = cdl - (pygame.time.get_ticks() - time_l) - cdreductionl
        screen.blit(Abilityl_cd, textlRect)
    else:
        cd_l = 0
        Ability_l.set_alpha(255)
        cdreductionl = 0
    if lolHP > 0: 
        pygame.draw.line(screen,(255,0,0), (252, 560), (252 + healthlength, 560), 16)
    healthtext = font.render(str(lolHP) + "/" + str(totalHP).zfill(2), True, (0, 0, 0))
    healthrect = healthtext.get_rect()
    healthrect.center = (500, 560)
    screen.blit(healthtext, healthrect)
    badtimer -= 2
    pygame.display.flip()

    

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
