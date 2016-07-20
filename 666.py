from pygame import *
import pygame, sys
import time
from math import *
import math
import random
import time

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
Ez_l = pygame.transform.scale(pygame.image.load("images/ez_L1.png"), (80, 80))
ez_H_explode = pygame.transform.scale(pygame.image.load("images/ez_H-explode.png"), (75, 75))
EzPosition = [100, 200]
Ez_cd = [0, 0, 0, 0, 0]
ezatkrate = 2
Ezcd = [1000 / ezatkrate, 3000, 10000, 6000, 30000]
EzSpeed = 4
Ez_listg = []
Ez_hPosition = [10000, 10000, 0]
Ez_lPosition = [10000, 10000, 0]
Ez_listkx = [10000, 10000, 10000, 10000, 10000, 10000, 10000]
Ez_listky = [10000, 10000, 10000, 10000, 10000, 10000, 10000]
Ez_listkz = [0, 0, 0, 0, 0, 0, 0]
healthRect1 = (10, 10, 550, 30)
AngleK = 0

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
Lucian_listg = []
LuPosition = [1000, 200]
LuSpeed = 4
healthlength_p1= 546
healthlength_p2 =546
healthRect2 = (740, 10, 550, 30)

Bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (1300, 650))
KO = pygame.transform.scale(pygame.image.load("images/KO.png"), (1000, 400))
KORect = KO.get_rect()
KORect.center = (650, 325)

run = 1
ez_score = 0
lucian_score = 0

while 1:
    run = 1
    if EzPosition[0]<0:
        EzPosition[0]=0
    if EzPosition[0]>1200:
        EzPosition[0]=1200
    if EzPosition[1]<0:
        EzPosition[1]=0
    if EzPosition[1]>550:
        EzPosition[1]=550
    if LuPosition[0]<0:
        LuPosition[0]=0
    if LuPosition[0]>1200:
        LuPosition[0]=1200
    if LuPosition[1]<0:
        LuPosition[1]=0
    if LuPosition[1]>550:
        LuPosition[1]=550


    screen.blit(Bg, (0, 0))
    screen.blit(Ez, (EzPosition[0], EzPosition[1]))
    screen.blit(Lucian, (LuPosition[0], LuPosition[1]))
    pygame.draw.rect(screen, (255, 255, 255), healthRect1, 0)
    pygame.draw.rect(screen, (255, 255, 255), healthRect2, 0)


    screen.blit(Ez_h, (Ez_hPosition[0], Ez_hPosition[1]))
    for skill in range(7):
        screen.blit(Ez_k, (Ez_listkx[skill], Ez_listky[skill]))
    screen.blit(Ez_l, (Ez_lPosition[0], Ez_lPosition[1]))
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
                if (EzPosition[0] - LuPosition[0]) ** 2 + (EzPosition[1] - LuPosition[1]) ** 2 <= 360000:
                    if Ez_cd[0] == 0:
                        Ez_listg.append([EzPosition[0] + 25, EzPosition[1] + 25, 0])
                        Ez_timeg = pygame.time.get_ticks()
                        #Ez_cd[0] = Ezcd[0]                    
            elif event.key == K_4:
                if Ez_cd[1] == 0:
                    Ez_hPosition[0] = EzPosition[0] + 25
                    Ez_hPosition[1] = EzPosition[1] + 25
                    a = LuPosition[0] - EzPosition[0]
                    b = LuPosition[1] - EzPosition[1]
                    if a != 0:
                        Ez_hPosition[2] = atan(b / a)
                    if a > 0 and b >= 0:
                        ez_cosh = cos(Ez_hPosition[2])
                        ez_sinh = sin(Ez_hPosition[2])
                    if a > 0 and b <= 0:
                        ez_cosh = cos(Ez_hPosition[2])
                        ez_sinh = sin(Ez_hPosition[2])
                    if a < 0 and b >= 0:
                        ez_cosh = 0 - cos(Ez_hPosition[2])
                        ez_sinh = 0 - sin(Ez_hPosition[2])
                    if a < 0 and b <= 0:
                        ez_cosh = 0 - cos(Ez_hPosition[2])
                        ez_sinh = 0 - sin(Ez_hPosition[2])
                    Ez_timeh = pygame.time.get_ticks()
                    #Ez_cd[1] = Ezcd[1]
            elif event.key == K_5:
                if Ez_cd[2] == 0:
                    P = pygame.mouse.get_pos()
                    if P[0] - EzPosition[0] != 0:
                        a = P[1] - EzPosition[1] - 50
                        b = P[0] - EzPosition[0] - 50
                        if b != 0:
                            angle233 = math.atan(math.sqrt((a*a) / (b*b)))
                        if a >= 0 and b > 0:
                            EzPosition[0] += cos(angle233) * 300
                            EzPosition[1] += sin(angle233) * 300
                        if a >= 0 and b < 0:
                            EzPosition[0] -= cos(angle233) * 300
                            EzPosition[1] += sin(angle233) * 300
                        if a <= 0 and b > 0:
                            EzPosition[0] += cos(angle233) * 300
                            EzPosition[1] -= sin(angle233) * 300
                        if a <= 0 and b < 0:
                            EzPosition[0] -= cos(angle233) * 300
                            EzPosition[1] -= sin(angle233) * 300
                    else:
                        if P[1] < EzPosition[1]:
                            EzPosition[1] -= 300
                        else:
                            EzPosition[1] += 300
                    Ez_timej = pygame.time.get_ticks()
                    Ez_cd[2] = Ezcd[2]
            elif event.key == K_6:
                if Ez_cd[3] == 0:
                    a1 = LuPosition[1] - EzPosition[1]
                    b1 = LuPosition[0] - EzPosition[0]
                    if b1 != 0:
                        AngleK = atan(a1 / b1)
                    else:
                        AngleK = math.pi/2
                    for skill in range(7):
                        Ez_listkx[skill] = EzPosition[0] + 25
                        Ez_listky[skill] = EzPosition[1] + 25
                        Ez_listkz[skill] = AngleK + (skill - 3) * math.pi / 9         
                    Ez_timek = pygame.time.get_ticks()
                    dmgk = 0
                    #Ez_cd[3] = Ezcd[3]                                            
            elif event.key == K_7:
                if Ez_cd[4] == 0:
                    Ez_lPosition[0] = EzPosition[0]
                    Ez_lPosition[1] = EzPosition[1]
                    Ez_timel = pygame.time.get_ticks()
                    Ez_cd[4] = Ezcd[4]
            
            elif event.key == K_UP:
                key2[0] = True
            elif event.key == K_DOWN:
                key2[1] = True
            elif event.key == K_LEFT:
                key2[2] = True
            elif event.key == K_RIGHT:
                key2[3] = True
            elif event.key == K_n:
                if (EzPosition[0] - LuPosition[0]) ** 2 + (EzPosition[1] - LuPosition[1]) ** 2 <= 360000:
                    if Lucian_cd[0] == 0:
                        Lucian_listg.append([LuPosition[0] + 25, LuPosition[1] + 25, 0])
                        Lucian_timeg = pygame.time.get_ticks()                
##            elif event.key == 109:
##            elif event.key == 44:
##            elif event.key == 46:
##            elif event.key == 47:                
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
        EzPosition[1] -= EzSpeed
    if key1[1] == True:
        EzPosition[1] += EzSpeed
    if key1[2] == True:
        EzPosition[0] -= EzSpeed
    if key1[3] == True:
        EzPosition[0] += EzSpeed

    if key2[0] == True:
        LuPosition[1] -= LuSpeed
    if key2[1] == True:
        LuPosition[1] += LuSpeed
    if key2[2] == True:
        LuPosition[0] -= LuSpeed
    if key2[3] == True:
        LuPosition[0] += LuSpeed

    EzCoRect = (EzPosition[0] + 25, EzPosition[1] + 25, 50, 50)
    LuCoRect = (LuPosition[0] + 25, LuPosition[1] + 25, 50, 50)
    if Ez_hPosition[0] > -50 and Ez_hPosition[0] < 1300 and Ez_hPosition[1] > -50 and Ez_hPosition[1] < 650:
        Ez_hPosition[0] += ez_cosh * 20
        Ez_hPosition[1] += ez_sinh * 20
    else:
        Ez_hPosition[0] = 10000
        Ez_hPosition[1] = 10000
        Ez_hPosition[2] = 0
    if pygame.Rect(Ez_hPosition[0], Ez_hPosition[1], 50, 50).colliderect(LuCoRect):
        lucian_cHP -= 400
        Ez_hPosition[0] = 10000
        Ez_hPosition[1] = 10000
        Ez_hPosition[2] = 0
        
    EzCoRect = (EzPosition[0] + 25, EzPosition[1] + 25, 50, 50)
    LuCoRect = (LuPosition[0] + 25, LuPosition[1] + 25, 50, 50)
    
    for skill in range(7):
        if Ez_listkx[skill] > -50 and Ez_listkx[skill] < 1300 and Ez_listky[skill] > -50 and Ez_listky[skill] < 1300:
            if a1 > 0 and b1 > 0:
                Ez_listkx[skill] += cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] += sin(Ez_listkz[skill]) * 13
            if a1 > 0 and b1 < 0:
                Ez_listkx[skill] -= cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] -= sin(Ez_listkz[skill]) * 13
            if a1 < 0 and b1 > 0:
                Ez_listkx[skill] += cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] += sin(Ez_listkz[skill]) * 13
            if a1 < 0 and b1 < 0:
                Ez_listkx[skill] -= cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] -= sin(Ez_listkz[skill]) * 13
            if a1 > 0 and b1 == 0:
                Ez_listkx[skill] -= cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] += sin(Ez_listkz[skill]) * 13
            if a1 < 0 and b1 == 0:
                Ez_listkx[skill] += cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] -= sin(Ez_listkz[skill]) * 13
            if a1 == 0 and b1 > 0:
                Ez_listkx[skill] += cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] += sin(Ez_listkz[skill]) * 13
            if a1 == 0 and b1 < 0:
                Ez_listkx[skill] -= cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] -= sin(Ez_listkz[skill]) * 13
            if a1 == 0 and b1 == 0:
                Ez_listkx[skill] -= cos(Ez_listkz[skill]) * 13
                Ez_listky[skill] += sin(Ez_listkz[skill]) * 13
                
        else:
            Ez_listkx[skill] = 10000
            Ez_listky[skill] = 10000
            Ez_listkz[skill] = 0
        Ez_kRect = Ez_k.get_rect()
        Ez_kRect.top = Ez_listky[skill]
        Ez_kRect.left = Ez_listkx[skill]
        if Ez_kRect.colliderect(LuCoRect):
            Ez_listkx[skill] = 10000
            Ez_listky[skill] = 10000
            Ez_listkz[skill] = 0
            if dmgk == 0:
                lucian_cHP -= 400
                dmgk = 1
            else:
                lucian_cHP -= 80
    index = 0
    for Ezg in Ez_listg:
        a = (LuPosition[0] + 50) - (Ezg[0] + 25)
        b = (LuPosition[1] + 50) - (Ezg[1] + 25)
        if a != 0:
            Ezg[2] = math.atan(b / a)
        if a > 0 and b >= 0:
            ez_cosg = cos(Ezg[2])
            ez_sing = sin(Ezg[2])
        if a > 0 and b <= 0:
            ez_cosg = cos(Ezg[2])
            ez_sing = sin(Ezg[2])
        if a < 0 and b >= 0:
            ez_cosg = 0 - cos(Ezg[2])
            ez_sing = 0 - sin(Ezg[2])
        if a < 0 and b <= 0:
            ez_cosg = 0 - cos(Ezg[2])
            ez_sing = 0 - sin(Ezg[2])
        Ezg[0] += ez_cosg * 8
        Ezg[1] += ez_sing * 8
        EzgRect = Ez_g.get_rect()
        EzgRect.left = Ezg[0]
        EzgRect.top = Ezg[1]
        if EzgRect.colliderect(LuCoRect):
            Ez_listg.pop(index)
            lucian_cHP -= 100
        index += 1
    index1 = 0

    
    for Lug in Lucian_listg:
        a = (EzPosition[0] + 50) - (Lug[0] + 25)
        b = (EzPosition[1] + 50) - (Lug[1] + 25)
        if a != 0:
            Lug[2] = math.atan(b / a)
        if a > 0 and b >= 0:
            Lu_cosg = cos(Lug[2])
            Lu_sing = sin(Lug[2])
        if a > 0 and b <= 0:
            Lu_cosg = cos(Lug[2])
            Lu_sing = sin(Lug[2])
        if a < 0 and b >= 0:
            Lu_cosg = 0 - cos(Lug[2])
            Lu_sing = 0 - sin(Lug[2])
        if a < 0 and b <= 0:
            Lu_cosg = 0 - cos(Lug[2])
            Lu_sing = 0 - sin(Lug[2])
        Lug[0] += Lu_cosg * 8
        Lug[1] += Lu_sing * 8
        LugRect = Lucian_g.get_rect()
        LugRect.left = Lug[0]
        LugRect.top = Lug[1]
        if LugRect.colliderect(EzCoRect):
            Lucian_listg.pop(index1)
            ez_cHP -= 100
        index1 += 1
    font = pygame.font.Font(None, 48)
    Score = font.render(str(int(ez_score))+" : "+ str(int(lucian_score)).zfill(1), True, (255, 255, 255))
    ScoreRect = Score.get_rect()
    ScoreRect.center = (650, 30)
    screen.blit(Score, ScoreRect)
    for Ezg in Ez_listg:
        screen.blit(Ez_g, (Ezg[0], Ezg[1]))
    for Lug in Lucian_listg:
        screen.blit(Lucian_g, (Lug[0], Lug[1]))
    healthlength_p1 = 546 * ez_cHP / ez_tHP
    healthlength_p2 = 546 * lucian_cHP / lucian_tHP
    if ez_cHP > 0:
        pygame.draw.line(screen, (255, 0, 0), (12, 25), (12 + healthlength_p1, 25), 26)
    if lucian_cHP > 0:
        pygame.draw.line(screen, (255, 0, 0), (1288 - healthlength_p2, 25), (1288, 25), 26)
    if ez_cHP <= 0:
        ez_cHP = ez_tHP
        lucian_cHP = lucian_tHP
        screen.blit(KO, KORect)
        pygame.display.flip()
        lucian_score += 1
        key1 = [False, False, False, False]
        key2 = [False, False, False, False]
        while run:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    run = 0
                if event.type == QUIT:
                    pygame.quit()
                    exit()
        LuPosition = [1000, 200]
        EzPosition = [100, 200]
        Ez_listg = []
        Lucian_listg = []
    if lucian_cHP <= 0:
        ez_cHP = ez_tHP
        lucian_cHP = lucian_tHP
        screen.blit(KO, KORect)
        pygame.display.flip()
        ez_score += 1
        key1 = [False, False, False, False]
        key2 = [False, False, False, False]
        while run:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    run = 0
                if event.type == QUIT:
                    pygame.quit()
                    exit()
        LuPosition = [1000, 200]
        EzPosition = [100, 200]
        Ez_listg = []
        Lucian_listg = []
    pygame.display.flip()
    




        

