from pygame import *
import pygame
import time
from math import *
import math
import random

pygame.init()
screen = pygame.display.set_mode((1000, 600))
key = [False, False, False, False]
Ez = pygame.image.load("images/ez.jpg")
LOL = pygame.transform.scale(Ez, (100, 100))
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
Monster = pygame.transform.scale(M, (75, 75))
bg = pygame.transform.scale(Bg, (1000, 600))
Abilityh_x = 1000
Abilityh_y = 600
Abilityk_x = [1000, 1000, 1000, 1000, 1000, 1000, 1000]
Abilityk_y = [600, 600, 600, 600, 600, 600, 600]
Abilityl_x = 1000
Abilityl_y = 600
NormalAttack = pygame.transform.scale(G, (50, 50))
Ability_h = pygame.transform.scale(H, (50, 50))
Ability_j = pygame.transform.scale(J, (50, 50))
Ability_k = pygame.transform.scale(K2, (50, 50))
Ability_l = pygame.transform.scale(L2, (50, 50))
Skill_h = pygame.transform.scale(H, (50, 50))
Skill_k = pygame.transform.scale(K1, (50, 50))
Skill_l = pygame.transform.scale(L1, (80, 80))
H_explode = pygame.transform.scale(H_ex, (75, 75))
lolx = 100
loly = 100
cd_g = 0
cd_h = 0
cd_j = 0
cd_k = 0
cd_l = 0
Monsters = []
badtimer = 0
MonHp = 500
listg = []
listk = []
atkrate = 10
minimum = 250
gg = [0, 0]
b = 0
explode = [0, 0]
exist_ex = 0
dmg_l = 800
cdreductionj = 0
cdreductionk = 0
cdreductionl = 0

def zhengchangmoshi():
    global cdh, cdj, cdk, cdl
    cdh = 3000
    cdj = 10000
    cdk = 6000
    cdl = 30000
    atkrate = 1.5

def wuxianhuoli():
    global cdh, cdj, cdk, cdl
    cdh = 1000
    cdj = 1000
    cdk = 1000
    cdl = 1000
    atkrate = 10

def distance(x1, y1, x2, y2):
    return(math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1) * (y2 - y1)))
    

zhengchangmoshi()

for i in range(7):
    listk.append((i, i))
    
    
while 1:
    screen.blit(bg, (0, 0))
    if b:
        screen.blit(H_explode, exRect)
    screen.blit(LOL, (lolx, loly))
    screen.blit(Skill_h, (Abilityh_x, Abilityh_y))
    screen.blit(Skill_l, (Abilityl_x, Abilityl_y))
    for skill in range(7):
        screen.blit(Skill_k, (Abilityk_x[skill], Abilityk_y[skill]))
    screen.blit(Ability_h, (0, 550))
    screen.blit(Ability_j, (50, 550))
    screen.blit(Ability_k, (100, 550))
    screen.blit(Ability_l, (150, 550))
    for g in listg:
        screen.blit(NormalAttack, (g[0], g[1]))
    if badtimer==0:
        Monsters.append([1000, random.randint(0,475), MonHp])
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
        if guys[0] < -75 or guys[2] <= 0:
            Monsters.pop(index)
        guys[0] -= 2
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
        
    for guys in Monsters:
        screen.blit(Monster, (guys[0], guys[1]))

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
                    Abilityl_x = lolx + 100
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

    badtimer -= 2
    pygame.display.flip()
    
        
        
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
