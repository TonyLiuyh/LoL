from pygame import *
import pygame, sys
import time
from math import *
import math
import random

pygame.init()
screen = pygame.display.set_mode((1300, 650))
key1 = [False, False, False, False]
key2 = [False, False, False, False]


ez_tHP = 5000
ez_cHP = ez_tHP

lucian_tHP = 5000
lucian_cHP = lucian_tHP


Ez = pygame.transform.scale(pygame.image.load("images/ez.jpg"), (100, 100))
bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (1000, 600))
Ez_g = pygame.transform.scale(pygame.image.load("images/ez_G.jpg"), (50, 50))
ez_h = pygame.transform.scale(pygame.image.load("images/ez_H.jpg"), (50, 50))
ez_j = pygame.transform.scale(pygame.image.load("images/ez_J.jpg"), (50, 50))
ez_k = pygame.transform.scale(pygame.image.load("images/ez_K2.jpg"), (50, 50))
ez_l = pygame.transform.scale(pygame.image.load("images/ez_L2.jpg"), (50, 50))
Ez_h = ez_h
Ez_k = pygame.transform.scale(pygame.image.load("images/ez_K1.png"), (50, 50))
Ez_l = pygame.transform.scale(pygame.image.load("images/ez_L2.jpg"), (80, 80))
ez_H_explode = pygame.transform.scale(pygame.image.load("images/ez_H-explode.png"), (75, 75))
EzPosition = [100, 200]
Ez_cd = [0, 0, 0, 0, 0]
ezatkrate = 2
Ezcd = [1000 / ezatkrate, 3000, 10000, 6000, 30000]
Ez_hPosition = [10000, 10000]
Ez_listkx(7) = [10000]
Ez_listky(7) = [10000]

Lucian = pygame.transform.scale(pygame.image.load("images/Lucian.jpg"), (100, 100))
Lucian_g = pygame.transform.scale(pygame.image.load("images/Lucian_G.png"), (50, 50))
lucian_h = pygame.transform.scale(pygame.image.load("images/Lucian_H.png"), (50, 50))
lucian_j = pygame.transform.scale(pygame.image.load("images/Lucian_J.png"), (50, 50))
lucian_k = pygame.transform.scale(pygame.image.load("images/Lucian_K.jpg"), (50, 50))
lucian_l = pygame.transform.scale(pygame.image.load("images/Lucian_L.png"), (50, 50))
Lucian_h = lucian_h
Lucian_j = lucian_j
Lucian_l = lucian_l
Lucian_cd = [0, 0, 0, 0, 0]
Luciancd = Lucian_cd
LuPosition = [800, 200]
healthlength_p1= 550
healthlength_p2 =550
Bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (1300, 650))

ez_score = 0
lucian_score = 0

while 1:
    if ez_cHP <= 0:
        ez_cHP = ez_tHP
        lucian_cHP = lucian_tHP
        ez_score += 1
    if lucian_cHP <= 0:
        ez_cHP = ez_tHP
        lucian_cHP = lucian_tHP
        lucian_score += 1
    screen.blit(Bg, (0, 0))
    screen.blit(Ez, (EzPosition[0], EzPosition[1]))
    screen.blit(Lucian, (LuPosition[0], LuPosition[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                key1[0] = True
            elif event.key == K_s:
                key1[1] = True
            elif event.key == K_a:
                key1[2] = True
            elif event.key == K_d:
                key1[3] = True
            elif event.key == K_3:
                if Ez_cd[0] == 0:
                    Ez_listg.append([EzPosition[0] + 25, EzPosition[1] + 25, 0])
                    Ez_timeg = pygame.time.get_ticks()
                    Ezcd[0] = 1000 / Ezatkrate
                    Ez_cd[0] = Ezcd[0]                    
            elif event.key == K_4:
                if Ez_cd[1] == 0:
                    Ez_hPosition[0] = EzPosition[0] + 25
                    Ez_hPosition[1] = EzPosition[1] + 25
                    Ez_timeh = pygame.get_ticks()
                    Ez_cd[1] = Ezcd[1]
            elif event.key == K_5:
                if Ez_cd[2] == 0:
                    P = pygame.mouse.get_pos()
                    if P[0] - EzPosition[0] != 0:
                        angle233 = math.atan((P[1] - EzPosition[1])/(P[0]) - EzPosition[0])
                        EzPosition[0] += cos(angle233) * 300
                        EzPosition[1] += sin(angle233) * 300
                    else:
                        if P[1] < EzPosition[1]:
                            EzPosition[1] -= 300
                        else:
                            EzPosition[1] += 300
                    Ez_timej = pygame.get_ticks()
                    Ez_cd[2] = Ezcd[2]
            elif event.key == K_6:
                if Ez_cd[3] == 0:
                    for skill in range(7):
                        Ez_listkx[skill] = EzPosition[0] + 25
                        Ez_listky[skill] = EzPosition[1] + 25
                    Ez_timek = pygame.time.get_ticks()
                    Ez_cd[3] = Ezcd[]
                                            
            elif event.key == K_7:
            
            elif event.key == K_UP:
                key2[0] = True
            elif event.key == K_DOWN:
                key2[1] = True
            elif event.key == K_LEFT:
                key2[2] = True
            elif event.key == K_RIGHT:
                key2[3] = True
            elif event.key == 110:
            elif event.key == 109:
            elif event.key == 44:
            elif event.key == 46:
            elif event.key == 47:                
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                key1[0] = False
            elif event.key == K_s:
                key1[1] = False
            elif event.key == K_a:
                key1[2] = False
            elif event.key == K_d:
                key1[3] = False
            
            elif event.key == K_UP:
                key2[0] = False
            elif event.key == K_DOWN:
                key2[1] = False
            elif event.key == K_LEFT:
                key2[2] = False
            elif event.key == K_RIGHT:
                key2[3] = False
    if key1[0] == True:
        EzPosition[1] -= 8
    if key1[1] == True:
        EzPosition[1] += 8
    if key1[2] == True:
        EzPosition[0] -= 8
    if key1[3] == True:
        EzPosition[0] += 8

    if key2[0] == True:
        LuPosition[1] -= 4
    if key2[1] == True:
        LuPosition[1] += 4
    if key2[2] == True:
        LuPosition[0] -= 4
    if key2[3] == True:
        LuPosition[0] += 4
    
    font = pygame.font.Font(None, 48)
    Score = font.render(str(int(ez_score))+" : "+ str(int(lucian_score)).zfill(1), True, (255, 255, 255))
    ScoreRect = Score.get_rect()
    ScoreRect.center = (650, 30)
    screen.blit(Score, ScoreRect)

    pygame.display.flip()
    




        

