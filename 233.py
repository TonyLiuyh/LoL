from pygame import *
import pygame
import time
from math import *
import math
import random

pygame.init()
screen = pygame.display.set_mode((1000, 600))
key = [False, False, False, False]
Ez = pygame.image.load("ez.jpg")
LOL = pygame.transform.scale(Ez, (100, 100))
G = pygame.image.load("G.jpg")
H = pygame.image.load("H.jpg")
J = pygame.image.load("J.jpg")
K = pygame.image.load("K.jpg")
M = pygame.image.load("Monster.jpg")
Monster = pygame.transform.scale(M, (75, 75))
Abilityh_x = 1000
Abilityh_y = 600
Abilityk_x = [1000, 1000, 1000, 1000, 1000, 1000, 1000]
Abilityk_y = [600, 600, 600, 600, 600, 600, 600]
NormalAttack = pygame.transform.scale(G, (50, 50))
Ability_h = pygame.transform.scale(H, (50, 50))
Ability_j = pygame.transform.scale(J, (50, 50))
Ability_k = pygame.transform.scale(K, (50, 50))
Skill_h = pygame.transform.scale(H, (50, 50))
Skill_k = pygame.transform.scale(K, (50, 50))
lolx = 100
loly = 100
cd_g = 0
cd_h = 0
cd_j = 0
cd_k = 0
Monsters = []
badtimer = 0
MonHp = 500
listg = []
listk = []
atkrate = 2.5
minimum = 250
gg = [0, 0]

def zhengchangmoshi():
    global cdh, cdj, cdk
    cdh = 3000
    cdj = 10000
    cdk = 6000

def wuxianhuoli():
    global cdh, cdj, cdk
    cdh = 1000
    cdj = 1000
    cdk = 1000

def distance(x1, y1, x2, y2):
    return(math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1) * (y2 - y1)))
    

zhengchangmoshi()

for i in range(7):
    listk.append((i, i))
    
    
while 1:
    screen.fill(0)
    screen.blit(LOL, (lolx, loly))
    screen.blit(Skill_h, (Abilityh_x, Abilityh_y))
    for skill in range(7):
        screen.blit(Skill_k, (Abilityk_x[skill], Abilityk_y[skill]))
    screen.blit(Ability_h, (0, 550))
    screen.blit(Ability_j, (50, 550))
    screen.blit(Ability_k, (100, 550))
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
    for guys in Monsters:
        if guys[0] < -75 or guys[2] <= 0:
            Monsters.pop(index)
        guys[0] -= 0.5
        guyRect = pygame.Rect(Monster.get_rect())
        guyRect.left = guys[0]
        guyRect.top = guys[1]
        if hRect.colliderect(guyRect):
            guys[2] -= 1000
            Abilityh_x = 1000
            Abilityh_y = 600
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
                    g[2] = atan((guys[1] - g[1])/(guys[0] - g[0]))
        g[0] += 2 * cos(g[2])
        g[1] += 2 * sin(g[2])
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
                    cd_g = 1000 / atkrate
                    cdg = cd_g
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
        loly -= 1
    if key[1] == True:
        loly += 1
    if key[2] == True:
        lolx -= 1
    if key[3] == True:
        lolx += 1

    if Abilityh_x < 1000:
        Abilityh_x += 5
    for skill in range(7):
        if Abilityk_x[skill] < 1000 and Abilityk_y[skill] < 600:
            if skill == 0:
                Abilityk_x[skill] += 2
                Abilityk_y[skill] -= 3.46
            if skill == 1:
                Abilityk_x[skill] += 4 * 0.77
                Abilityk_y[skill] -= 4 * 0.64
            if skill == 2:
                Abilityk_x[skill] += 4 * 0.94
                Abilityk_y[skill] -= 4 * 0.34
            if skill == 3:
                Abilityk_x[skill] += 4
            if skill == 4:
                Abilityk_x[skill] += 4 * 0.94
                Abilityk_y[skill] += 4 * 0.34
            if skill == 5:
                Abilityk_x[skill] += 4 * 0.77
                Abilityk_y[skill] += 4 * 0.64            
            if skill == 6:
                Abilityk_x[skill] += 2
                Abilityk_y[skill] += 3.46 
                


    font = pygame.font.Font(None, 24)
    Abilityh_cd = font.render(str(cd_h//1000+1).zfill(2), True, (0, 0, 0))
    texthRect = Abilityh_cd.get_rect()
    texthRect.center = (Ability_h.get_width()/2, screen.get_height()-Ability_h.get_height()/2)
    Abilityj_cd = font.render(str(cd_j//1000+1).zfill(2), True, (0, 0, 0))
    textjRect = Abilityj_cd.get_rect()
    textjRect.center = (Ability_j.get_width()*3/2, screen.get_height()-Ability_j.get_height()/2)
    Abilityk_cd = font.render(str(cd_k//1000+1).zfill(2), True, (0, 0, 0))
    textkRect = Abilityk_cd.get_rect()
    textkRect.center = (Ability_k.get_width()*5/2, screen.get_height()-Ability_k.get_height()/2)
    if cd_h > 0:
        Ability_h.set_alpha(150)
        cd_h = cdh - (pygame.time.get_ticks() - time_h)
        screen.blit(Abilityh_cd, texthRect)
    else:
        cd_h = 0
        Ability_h.set_alpha(255)

    if cd_j > 0:
        Ability_j.set_alpha(150)
        cd_j = cdj - (pygame.time.get_ticks() - time_j)
        screen.blit(Abilityj_cd, textjRect)
    else:
        cd_j = 0
        Ability_j.set_alpha(255)

    if cd_k > 0:
        Ability_k.set_alpha(150)
        cd_k = cdk - (pygame.time.get_ticks() - time_k)
        screen.blit(Abilityk_cd, textkRect)
    else:
        cd_k = 0
        Ability_k.set_alpha(255)

    if cd_g > 0:
        cd_g = cdg - (pygame.time.get_ticks() - time_g)
    else:
        cd_g = 0

    badtimer -= 0.25
    pygame.display.flip()
    
        
        
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
