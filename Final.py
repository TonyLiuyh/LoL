from pygame import *
import pygame, sys
import time
from math import *
import math
import random
import time

pygame.init()

button1 = pygame.transform.scale(pygame.image.load("images/Button.png"), (300, 75))
screen = pygame.display.set_mode((1300, 650))
button2 = button1
button3 = button2
button4 = button3
button5 = button4
button6 = button5
button7 = button6
HowlingAbyss = pygame.transform.scale(pygame.image.load("images/Howling_Abyss.jpg"), (1300, 650))

def P():
    key = [False, False, False, False]

    Ez = pygame.image.load("images/ez.jpg")
    G = pygame.image.load("images/ez_G.jpg")
    H = pygame.image.load("images/ez_H.jpg")
    J = pygame.image.load("images/ez_J.jpg")
    K1 = pygame.image.load("images/ez_K1.png")
    K2 = pygame.image.load("images/ez_K2.jpg")
    L1 = pygame.image.load("images/ez_L1.png")
    L2 = pygame.image.load("images/ez_L2.jpg")
    M = pygame.image.load("images/Monster.png")
    H_ex = pygame.image.load("images/ez_H-explode.png")
    Bg = pygame.image.load("images/bg.png")
    Mon = pygame.image.load("images/Mons.png")
    defeat = pygame.image.load("images/defeat.png")
    Warrior = pygame.image.load("images/Warrior.png")
    Wizard = pygame.image.load("images/Wizard.png")
    Level = pygame.image.load("images/Level.png")
    score=0
    Exp=0
    Lv = 1

    LOL = pygame.transform.scale(Ez, (100, 100))
    Monster = pygame.transform.scale(M, (75, 75))
    bg = pygame.transform.scale(Bg, (1300, 650))
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

    Abilityh_x = 10000
    Abilityh_y = 6000
    Abilityk_x = [10000, 10000, 10000, 10000, 10000, 10000, 10000]
    Abilityk_y = [6000, 6000, 6000, 6000, 6000, 6000, 6000]
    Abilityl_x = 10000
    Abilityl_y = 6000
    defeatRect = defeat.get_rect()
    defeatRect.center = (500, 300)
    levelRect = level.get_rect()

    lolx = 100
    loly = 100
    def Fibonacci(x):
        a1 = 1
        a2 = 2
        a3 = 3
        for i in range(x - 1):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
        return(a3 * 10)

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
    healthRect = (250, 600, 600, 20)
    healthlength = 496
    totalHP = 5000
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
        screen.blit(Ability_h, (0, 600))
        screen.blit(Ability_j, (50, 600))
        screen.blit(Ability_k, (100, 600))
        screen.blit(Ability_l, (150, 600))
        for g in listg:
            screen.blit(NormalAttack, (g[0], g[1]))
        if badtimer==0:
            Monsters.append([1300, random.randint(0,525), MonHp, 0])
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
                Exp += 10
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
                Abilityh_x = 10000
                Abilityh_y = 6000
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
                    Abilityk_x[skill] = 10000
                    Abilityk_y[skill] = 6000
            index += 1

        
        healthlength = 596 * lolHP / totalHP
        
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
        if lolx > 1200:
            lolx = 1200
        if loly < 0:
            loly = 0
        if loly > 500:
            loly = 500
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
        if Abilityh_x < 1300:
            Abilityh_x += 20
        else:
            Abilityh_x = 10000
            Abilityh_y = 6000
        for skill in range(7):
            if Abilityk_x[skill] < 1300 and Abilityk_y[skill] < 650:
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
        if Abilityl_x < 1300:
            Abilityl_x += 20
        else:
            dmg_l = 800
            Abilityl_x = 10000
            Abilityl_y = 6000

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
        score_display= font.render("Score: " +str(score).zfill(1),True,(255,255,255))
        scoreRect = score_display.get_rect()
        scoreRect.center= (650,30)
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
            pygame.draw.line(screen,(255,0,0), (252, 610), (252 + healthlength, 610), 16)
        if lolHP < 0:
            lolHP = 0
        healthtext = font.render(str(lolHP) + "/" + str(totalHP).zfill(1), True, (0, 0, 0))
        healthrect = healthtext.get_rect()
        healthrect.center = (560, 610)
        screen.blit(healthtext, healthrect)
        badtimer -= 2
        pygame.display.flip()
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

def PVP():
    key1 = [False, False, False, False]
    key2 = [False, False, False, False]

    Ez_cdtext = [0, 0, 0, 0, 0]
    Ez_cdRect = [0, 0, 0, 0, 0]
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
    Lucian_l = pygame.transform.scale(pygame.image.load("images/Lucian_L.png"), (60, 60))
    Lucian_listhx = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    Lucian_listhy = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    Lucian_listhz = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]
    Lucian_cd = [0, 0, 0, 0, 0]
    Luciancd = [1000, 5000, 7000, 10000, 30000]
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
    cdreductionj = 0
    cdreductionk = 0
    cdreductionl = 0
    damageava = 1
    atk = 1
    dmgav = 1
    draw = 0
    draw2 = 0
    Lu_jPosition = [10000, 10000, 0]
    length = 0
    DrawPos = [0, 0]
    Lu_sinj = 0
    Lu_cosj = 0
    lav = 0
    ltimer = 26
    Lucian_listl = []
    keycontrol = 0

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
        screen.blit(ez_h, (0, 600))
        screen.blit(ez_j, (50, 600))
        screen.blit(ez_k, (100, 600))
        screen.blit(ez_l, (150, 600))
        screen.blit(lucian_h, (1100, 600))
        screen.blit(lucian_j, (1150, 600))
        screen.blit(lucian_k, (1200, 600))
        screen.blit(lucian_l, (1250, 600))



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
                            Ez_cd[0] = Ezcd[0]                    
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
                        Ez_cd[1] = Ezcd[1]
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
                        Ez_cd[3] = Ezcd[3]                                            
                elif event.key == K_7:
                    if Ez_cd[4] == 0:
                        Ez_lPosition[0] = EzPosition[0] + 10
                        Ez_lPosition[1] = EzPosition[1] + 10
                        Ez_timel = pygame.time.get_ticks()
                        Ez_cd[4] = Ezcd[4]
                        a = LuPosition[0] - EzPosition[0]
                        b = LuPosition[1] - EzPosition[1]
                        if a != 0:
                            Ez_lPosition[2] = atan(b / a)
                        if a > 0 and b >= 0:
                            ez_cosl = cos(Ez_lPosition[2])
                            ez_sinl = sin(Ez_lPosition[2])
                        if a > 0 and b <= 0:
                            ez_cosl = cos(Ez_lPosition[2])
                            ez_sinl = sin(Ez_lPosition[2])
                        if a < 0 and b >= 0:
                            ez_cosl = 0 - cos(Ez_lPosition[2])
                            ez_sinl = 0 - sin(Ez_lPosition[2])
                        if a < 0 and b <= 0:
                            ez_cosl = 0 - cos(Ez_lPosition[2])
                            ez_sinl = 0 - sin(Ez_lPosition[2])
                        dmgav = 1
                
                elif event.key == K_UP:
                    key2[0] = True
                elif event.key == K_DOWN:
                    key2[1] = True
                elif event.key == K_LEFT:
                    key2[2] = True
                elif event.key == K_RIGHT:
                    key2[3] = True
                elif event.key == K_n and keycontrol == 0:
                    if (EzPosition[0] - LuPosition[0]) ** 2 + (EzPosition[1] - LuPosition[1]) ** 2 <= 360000:
                        if Lucian_cd[0] == 0:
                            Lucian_listg.append([LuPosition[0] + 25, LuPosition[1] + 25, 0])
                            Lucian_timeg = pygame.time.get_ticks()
                            Lu_timeg = pygame.time.get_ticks()
                elif event.key == 109 and keycontrol == 0:
                    if (EzPosition[0] - LuPosition[0]) ** 2 + (EzPosition[1] - LuPosition[1]) ** 2 <= 360000:
                        print('M1')
                        if Lucian_cd[1] == 0:
                            print('M2')
                            a = LuPosition[0] - EzPosition[0]
                            b = LuPosition[1] - EzPosition[1]
                            if a != 0:
                                Lu_angleh = atan(b / a)
                            if a > 0 and b >= 0:
                                Lu_cosh = cos(Lu_angleh)
                                Lu_sinh = sin(Lu_angleh)
                            if a > 0 and b <= 0:
                                Lu_cosh = cos(Lu_angleh)
                                Lu_sinh = sin(Lu_angleh)
                            if a < 0 and b >= 0:
                                Lu_cosh = 0 - cos(Lu_angleh)
                                Lu_sinh = 0 - sin(Lu_angleh)
                            if a < 0 and b <= 0:
                                Lu_cosh = 0 - cos(Lu_angleh)
                                Lu_sinh = 0 - sin(Lu_angleh)
                            for n in range(15):
                                Lucian_listhx[n] = LuPosition[0] + 25 - Lu_cosh * n * 50
                                Lucian_listhy[n] = LuPosition[1] + 25 - Lu_sinh * n * 50
                                Lucian_listhz[n] = n
                            atk = 1.5
                            damageava = 1
                    print("M")
                elif event.key == 44 and keycontrol == 0:
                    print(",")
                    if Lucian_cd[2] == 0:
                        a = LuPosition[0] - EzPosition[0]
                        b = LuPosition[1] - EzPosition[1]
                        Lu_jPosition[0] = LuPosition[0] + 25
                        Lu_jPosition[1] = LuPosition[1] + 25
                        if a != 0:
                            Lu_jPosition[2] = atan(b / a)
                        if a > 0 and b >= 0:
                            Lu_cosj = cos(Lu_jPosition[2])
                            Lu_sinj = sin(Lu_jPosition[2])
                        if a > 0 and b <= 0:
                            Lu_cosj = cos(Lu_jPosition[2])
                            Lu_sinj = sin(Lu_jPosition[2])
                        if a < 0 and b >= 0:
                            Lu_cosj = 0 - cos(Lu_jPosition[2])
                            Lu_sinj = 0 - sin(Lu_jPosition[2])
                        if a < 0 and b <= 0:
                            Lu_cosj = 0 - cos(Lu_jPosition[2])
                            Lu_sinj = 0 - sin(Lu_jPosition[2])
                        dmgavj = 1
                        Lu_timeh = pygame.time.get_ticks()
                        Lucian_cd[1] = Luciancd[1]
                    
                elif event.key == 46:
                    if Lucian_cd[3] == 0:
                        P = pygame.mouse.get_pos()
                        if P[0] - LuPosition[0] != 0:
                            a = P[1] - LuPosition[1] - 50
                            b = P[0] - LuPosition[0] - 50
                            if b != 0:
                                angle266 = math.atan(math.sqrt((a*a) / (b*b)))
                            if a >= 0 and b > 0:
                                LuPosition[0] += cos(angle266) * 300
                                LuPosition[1] += sin(angle266) * 300
                            if a >= 0 and b < 0:
                                LuPosition[0] -= cos(angle266) * 300
                                LuPosition[1] += sin(angle266) * 300
                            if a <= 0 and b > 0:
                                LuPosition[0] += cos(angle266) * 300
                                LuPosition[1] -= sin(angle266) * 300
                            if a <= 0 and b < 0:
                                LuPosition[0] -= cos(angle266) * 300
                                LuPosition[1] -= sin(angle266) * 300
                        else:
                            if P[1] < LuPosition[1]:
                                LuPosition[1] -= 300
                            else:
                                LuPosition[1] += 300
                        Lu_timej = pygame.time.get_ticks()
                        Lucian_cd[2] = Luciancd[2]
                    
                elif event.key == 47:
                    if Lucian_cd[4] == 0:
                        a = LuPosition[0] - EzPosition[0]
                        b = LuPosition[1] - EzPosition[1]
                        if a != 0:
                            anglel = atan(b / a)
                        if a > 0 and b >= 0:
                            Lu_cosl = cos(anglel)
                            Lu_sinl = sin(anglel)
                        if a > 0 and b <= 0:
                            Lu_cosl = cos(anglel)
                            Lu_sinl = sin(anglel)
                        if a < 0 and b >= 0:
                            Lu_cosl = 0 - cos(anglel)
                            Lu_sinl = 0 - sin(anglel)
                        if a < 0 and b <= 0:
                            Lu_cosl = 0 - cos(anglel)
                            Lu_sinl = 0 - sin(anglel)
                        ltimer = 0
                        lav = 1
                        keycontrol = 1
 
                        
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


        if ltimer <= 25:
            if ltimer % 2 == 0:
                Lucian_listl.append([LuPosition[0] - 20 * Lu_sinl + 25, LuPosition[1] + 20 * Lu_cosl + 25])
            if ltimer % 2 == 1:
                Lucian_listl.append([LuPosition[0] + 20 * Lu_sinl + 25, LuPosition[1] - 20 * Lu_cosl + 25])
        else:
            lav = 0
            keycontrol = 0


        if lav == 1:
            ltimer += 0.25
                
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

        if Ez_lPosition[0] > -80 and Ez_lPosition[0] < 1300 and Ez_lPosition[1] > -80 and Ez_lPosition[1] < 650:
            Ez_lPosition[0] += ez_cosl * 30
            Ez_lPosition[1] += ez_sinl * 30
        else:
            Ez_lPosition[0] = 10000
            Ez_lPosition[1] = 10000
            Ez_lPosition[2] = 0
            dmgav = 1
        if pygame.Rect(Ez_lPosition[0], Ez_lPosition[1], 80, 80).colliderect(LuCoRect):
            if dmgav == 1:
                lucian_cHP -= 600
            dmgav = 0

        
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
        indexg = 0

        
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
                Lucian_listg.pop(indexg)
                ez_cHP -= 100 * atk
                atk = 1
            indexg += 1


           
        for a in range(15):
            LuhRect = Lucian_h.get_rect()
            LuhRect.left = Lucian_listhx[a]
            LuhRect.top = Lucian_listhy[a]
            if damageava == 1:
                if LuhRect.colliderect(EzCoRect) and Lucian_listhz[a] > -5 and Lucian_listhz[a] < 6:
                    ez_cHP -= 600
                    damageava = 0

        if Lu_jPosition[0] > -50 and Lu_jPosition[0] < 1300 and Lu_jPosition[1] > -50 and Lu_jPosition[1] < 1300:
            Lu_jPosition[0] -= Lu_cosj * 20
            Lu_jPosition[1] -= Lu_sinj * 20
            length += 1
        else:
            Lu_jPosition = [10000, 10000, 0]
            length = 0

        indexl = 0
        for sl in Lucian_listl:
            if sl[0] > -50 and sl[0] < 1300 and sl[1] > -50 and sl[1] < 1300:
                sl[0] -= 30 * Lu_cosl
                sl[1] -= 30 * Lu_sinl
            else:
                Lucian_listl.pop(indexl)
            if Rect(sl[0], sl[1], 60, 60).colliderect(EzCoRect):
                Lucian_listl.pop(indexl)
                ez_cHP -= 80
            indexl += 1
            
        if Rect(Lu_jPosition[0], Lu_jPosition[1], 50, 50).colliderect(EzCoRect):
            ez_cHP -= 300
            DrawPos[0] = Lu_jPosition[0]
            DrawPos[1] = Lu_jPosition[1]
            Lu_jPosition[0] = 10000
            Lu_jPosition[1] = 10000
            Lu_jPosition[2] = 0
            draw = 1
            length = 0
            dmgavj = 0
        elif length >= 30:
            DrawPos[0] = Lu_jPosition[0]
            DrawPos[1] = Lu_jPosition[1]
            Lu_jPosition[0] = 10000
            Lu_jPosition[1] = 10000
            Lu_jPosition[2] = 0
            draw = 1
            length = 0
            
        if draw == 1:
            if draw2 < 10:
                for r in range(8):
                    if r - draw2 > 0 and r - draw2 < 5:
                        screen.blit(Lucian_j, (DrawPos[0] + r * Lu_cosj * 20, DrawPos[1] + r * Lu_sinj * 20))
                        screen.blit(Lucian_j, (DrawPos[0] + r * Lu_sinj * 20, DrawPos[1] - r * Lu_cosj * 20))
                        screen.blit(Lucian_j, (DrawPos[0] - r * Lu_cosj * 20, DrawPos[1] - r * Lu_sinj * 20))
                        screen.blit(Lucian_j, (DrawPos[0] - r * Lu_sinj * 20, DrawPos[1] + r * Lu_cosj * 20))
                        if Rect(DrawPos[0] + r * Lu_cosj * 20, DrawPos[1] + r * Lu_sinj * 20, 50, 50).colliderect(EzCoRect) and dmgavj == 1:
                            ez_cHP -= 300
                            dmgavj = 0
                        if Rect(DrawPos[0] + r * Lu_cosj * 20, DrawPos[1] - r * Lu_sinj * 20, 50, 50).colliderect(EzCoRect) and dmgavj == 1:
                            ez_cHP -= 300
                            dmgavj = 0
                        if Rect(DrawPos[0] - r * Lu_cosj * 20, DrawPos[1] - r * Lu_sinj * 20, 50, 50).colliderect(EzCoRect) and dmgavj == 1:
                            ez_cHP -= 300
                            dmgavj = 0
                        if Rect(DrawPos[0] - r * Lu_cosj * 20, DrawPos[1] + r * Lu_sinj * 20, 50, 50).colliderect(EzCoRect) and dmgavj == 1:
                            ez_cHP -= 300
                            dmgavj = 0
                draw2 += 0.5
            else:
                draw2 = 0
                draw = 0


            
            
        font = pygame.font.Font(None, 48)
        Score = font.render(str(int(ez_score))+" : "+ str(int(lucian_score)).zfill(1), True, (255, 255, 255))
        ScoreRect = Score.get_rect()
        ScoreRect.center = (650, 30)
        screen.blit(Score, ScoreRect)
        for Ezg in Ez_listg:
            screen.blit(Ez_g, (Ezg[0], Ezg[1]))
        for Lug in Lucian_listg:
            screen.blit(Lucian_g, (Lug[0], Lug[1]))
        screen.blit(Ez_h, (Ez_hPosition[0], Ez_hPosition[1]))
        for skill in range(7):
            screen.blit(Ez_k, (Ez_listkx[skill], Ez_listky[skill]))
        for skill in range(15):
            if Lucian_listhz[skill] + 5 > 0 and Lucian_listhz[skill] + 5 < 11:
                screen.blit(Lucian_h, (Lucian_listhx[skill], Lucian_listhy[skill]))
                Lucian_listhz[skill] -= 1
            if Lucian_listhz[skill] + 5 >= 11:
                Lucian_listhz[skill] -= 1
        screen.blit(Ez_h, (Ez_hPosition[0], Ez_hPosition[1]))
        screen.blit(Ez_l, (Ez_lPosition[0], Ez_lPosition[1]))
        screen.blit(Lucian_j, (Lu_jPosition[0], Lu_jPosition[1]))
        healthlength_p1 = 546 * ez_cHP / ez_tHP
        healthlength_p2 = 546 * lucian_cHP / lucian_tHP
        for skilll in Lucian_listl:
            screen.blit(Lucian_l, (skilll[0], skilll[1]))
        if ez_cHP > 0:
            pygame.draw.line(screen, (255, 0, 0), (12, 25), (12 + healthlength_p1, 25), 26)
        if lucian_cHP > 0:
            pygame.draw.line(screen, (255, 0, 0), (1288 - healthlength_p2, 25), (1288, 25), 26)

        font2 = pygame.font.Font(None, 36)
        for a in range(5):
            Ez_cdtext[a] = font2.render(str(Ez_cd[a]//1000 + 1), True, (255, 255, 255))
            Ez_cdRect[a] = Ez_cdtext[a].get_rect()
            Ez_cdRect[a].center = (-25 + 50 * a, 627)

        if Ez_cd[1] > 0:
            ez_h.set_alpha(150)
            Ez_cd[1] = Ezcd[1] - (pygame.time.get_ticks() - Ez_timeh)
            screen.blit(Ez_cdtext[1], Ez_cdRect[1])
        else:
            Ez_cd[1] = 0
            ez_h.set_alpha(255)

        if Ez_cd[2] > 0:
            ez_j.set_alpha(150)
            Ez_cd[2] = Ezcd[2] - (pygame.time.get_ticks() - Ez_timej) - cdreductionj
            screen.blit(Ez_cdtext[2], Ez_cdRect[2])
        else:
            Ez_cd[2] = 0
            ez_j.set_alpha(255)
            cdreductionj = 0

        if Ez_cd[3] > 0:
            ez_k.set_alpha(150)
            Ez_cd[3] = Ezcd[3] - (pygame.time.get_ticks() - Ez_timek) - cdreductionk
            screen.blit(Ez_cdtext[3], Ez_cdRect[3])
        else:
            Ez_cd[3] = 0
            ez_k.set_alpha(255)
            cdreductionk = 0

        if Ez_cd[0] > 0:
            Ez_cd[0] = Ezcd[0] - (pygame.time.get_ticks() - Ez_timeg)
        else:
            Ez_cd[0] = 0
        
        if Ez_cd[4] > 0:
            ez_l.set_alpha(150)
            Ez_cd[4] = Ezcd[4] - (pygame.time.get_ticks() - Ez_timel) - cdreductionl
            screen.blit(Ez_cdtext[4], Ez_cdRect[4])
        else:
            Ez_cd[4] = 0
            ez_l.set_alpha(255)
            cdreductionl = 0

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
            Lucian_listhx = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
            Lucian_listhy = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
            Lucian_listhz = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]
            damageava = 1
            atk = 1
            Ez_listg = []
            Lucian_listg = []
            Ez_cd = [0, 0, 0, 0, 0]
            Lucian_cd = [0, 0, 0, 0, 0]
            for skill in range(7):
                Ez_listkx[skill] = 10000
                Ez_listky[skill] = 10000
                Ez_listkz[skill] = 0
            Ez_hPosition = [10000, 10000, 0]
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
            Lucian_listhx = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
            Lucian_listhy = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
            Lucian_listhz = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]
            damageava = 1
            atk = 1
            LuPosition = [1000, 200]
            EzPosition = [100, 200]
            Ez_cd = [0, 0, 0, 0, 0]
            Lucian_cd = [0, 0, 0, 0, 0]
            Ez_listg = []
            Lucian_listg = []
            for skill in range(7):
                Ez_listkx[skill] = 10000
                Ez_listky[skill] = 10000
                Ez_listkz[skill] = 0
            Ez_hPosition = [10000, 10000, 0]
            




        pygame.display.flip()



bt1 = 0
bt2 = 0
bt3 = 0
bt4 = 0
bt5 = 0
bt6 = 0
bt7 = 0
font = pygame.font.Font(None, 40)
text1 = font.render("Play", True, (255, 255, 255))
text2 = font.render("Help", True, (255, 255, 255))
text3 = font.render("Quit", True, (255, 255, 255))
text4 = font.render("Single Player", True, (255, 255, 255))
text5 = font.render("PVP", True, (255, 255, 255))
text6 = font.render("Coming Soon...", True, (255, 255, 255))
text7 = font.render("Back", True, (255, 255, 255))
text1Rect = text1.get_rect()
text2Rect = text2.get_rect()
text3Rect = text3.get_rect()
text4Rect = text4.get_rect()
text5Rect = text5.get_rect()
text6Rect = text6.get_rect()
text7Rect = text7.get_rect()

b1pos = [500, 200]
b2pos = [500, 300]
b3pos = [500, 400]
b4pos = [500, -100]
b5pos = [500, -100]
b6pos = [500, -100]
b7pos = [500, -100]

move1 = 0

def move(button):
    if button == 1:
        for a in range(25):
            b1pos[1] -= 12
            b2pos[1] -= 16
            b3pos[1] -= 20
            screen.blit(HowlingAbyss, (0, 0))
            text1Rect.center = (b1pos[0] + 150, b1pos[1] + 40)
            text2Rect.center = (b2pos[0] + 150, b2pos[1] + 40)
            text3Rect.center = (b3pos[0] + 150, b3pos[1] + 40)
            screen.blit(button1, b1pos)
            screen.blit(text1, text1Rect)
            screen.blit(button2, b2pos)
            screen.blit(text2, text2Rect)
            screen.blit(button3, b3pos)
            screen.blit(text3, text3Rect)
            display.flip()
        time.sleep(0.3)
        for a in range(25):
            b4pos[1] += 12
            b5pos[1] += 16
            b6pos[1] += 20
            b7pos[1] += 24
            screen.blit(HowlingAbyss, (0, 0))
            text4Rect.center = (b4pos[0] + 150, b4pos[1] + 40)
            text5Rect.center = (b5pos[0] + 150, b5pos[1] + 40)
            text6Rect.center = (b6pos[0] + 150, b6pos[1] + 40)
            text7Rect.center = (b7pos[0] + 150, b7pos[1] + 40)
            screen.blit(button4, b4pos)
            screen.blit(text4, text4Rect)
            screen.blit(button5, b5pos)
            screen.blit(text5, text5Rect)
            screen.blit(button6, b6pos)
            screen.blit(text6, text6Rect)
            screen.blit(button7, b7pos)
            screen.blit(text7, text7Rect)
            display.flip()
    if button == 2:
        for a in range(25):
            b1pos[1] -= 12
            b2pos[1] -= 16
            b3pos[1] -= 20
            screen.blit(HowlingAbyss, (0, 0))
            text1Rect.center = (b1pos[0] + 150, b1pos[1] + 40)
            text2Rect.center = (b2pos[0] + 150, b2pos[1] + 40)
            text3Rect.center = (b3pos[0] + 150, b3pos[1] + 40)
            screen.blit(button1, b1pos)
            screen.blit(text1, text1Rect)
            screen.blit(button2, b2pos)
            screen.blit(text2, text2Rect)
            screen.blit(button3, b3pos)
            screen.blit(text3, text3Rect)
            display.flip()        
    if button == 7:
        for a in range(25):
            b4pos[1] -= 12
            b5pos[1] -= 16
            b6pos[1] -= 20
            b7pos[1] -= 24
            screen.blit(HowlingAbyss, (0, 0))
            text4Rect.center = (b4pos[0] + 150, b4pos[1] + 40)
            text5Rect.center = (b5pos[0] + 150, b5pos[1] + 40)
            text6Rect.center = (b6pos[0] + 150, b6pos[1] + 40)
            text7Rect.center = (b7pos[0] + 150, b7pos[1] + 40)
            screen.blit(button4, b4pos)
            screen.blit(text4, text4Rect)
            screen.blit(button5, b5pos)
            screen.blit(text5, text5Rect)
            screen.blit(button6, b6pos)
            screen.blit(text6, text6Rect)
            screen.blit(button7, b7pos)
            screen.blit(text7, text7Rect)
            display.flip()
        time.sleep(0.3)
        for a in range(25):
            b1pos[1] += 12
            b2pos[1] += 16
            b3pos[1] += 20
            screen.blit(HowlingAbyss, (0, 0))
            text1Rect.center = (b1pos[0] + 150, b1pos[1] + 40)
            text2Rect.center = (b2pos[0] + 150, b2pos[1] + 40)
            text3Rect.center = (b3pos[0] + 150, b3pos[1] + 40)
            screen.blit(button1, b1pos)
            screen.blit(button2, b2pos)
            screen.blit(button3, b3pos)
            screen.blit(text1, text1Rect)
            screen.blit(text2, text2Rect)
            screen.blit(text3, text3Rect)
            display.flip()
            
while 1:
    text1Rect.center = (b1pos[0] + 150, b1pos[1] + 40)
    text2Rect.center = (b2pos[0] + 150, b2pos[1] + 40)
    text3Rect.center = (b3pos[0] + 150, b3pos[1] + 40)
    text4Rect.center = (b4pos[0] + 150, b4pos[1] + 40)
    text5Rect.center = (b5pos[0] + 150, b5pos[1] + 40)
    text6Rect.center = (b6pos[0] + 150, b6pos[1] + 40)
    text7Rect.center = (b7pos[0] + 150, b7pos[1] + 40)
    screen.blit(HowlingAbyss, (0, 0))
    screen.blit(button1, b1pos)
    screen.blit(button2, b2pos)
    screen.blit(button3, b3pos)
    screen.blit(button4, b4pos)
    screen.blit(button5, b5pos)
    screen.blit(button6, b6pos)
    screen.blit(button7, b7pos)
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(text4, text4Rect)
    screen.blit(text5, text5Rect)
    screen.blit(text6, text6Rect)
    screen.blit(text7, text7Rect)
    p = mouse.get_pos()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if p[0] >= b1pos[0] and p[0] <= b1pos[0] + 300 and p[1] >= b1pos[1] and p[1] <= b1pos[1] + 75:
                bt1 = 1
            if p[0] >= b2pos[0] and p[0] <= b2pos[0] + 300 and p[1] >= b2pos[1] and p[1] <= b2pos[1] + 75:
                bt2 = 1
            if p[0] >= b3pos[0] and p[0] <= b3pos[0] + 300 and p[1] >= b3pos[1] and p[1] <= b3pos[1] + 75:
                bt3 = 1
            if p[0] >= b4pos[0] and p[0] <= b4pos[0] + 300 and p[1] >= b4pos[1] and p[1] <= b4pos[1] + 75:
                bt4 = 1
            if p[0] >= b5pos[0] and p[0] <= b5pos[0] + 300 and p[1] >= b5pos[1] and p[1] <= b5pos[1] + 75:
                bt5 = 1
            if p[0] >= b6pos[0] and p[0] <= b6pos[0] + 300 and p[1] >= b6pos[1] and p[1] <= b6pos[1] + 75:
                bt6 = 1
            if p[0] >= b7pos[0] and p[0] <= b7pos[0] + 300 and p[1] >= b7pos[1] and p[1] <= b7pos[1] + 75:
                bt7 = 1
        if event.type == MOUSEBUTTONUP:
            if bt1 == 1 and p[0] >= b1pos[0] and p[0] <= b1pos[0] + 300 and p[1] >= b1pos[1] and p[1] <= b1pos[1] + 75:
                move(1)
                bt1 = 0
            if bt2 == 1 and p[0] >= b2pos[0] and p[0] <= b2pos[0] + 300 and p[1] >= b2pos[1] and p[1] <= b2pos[1] + 75:
                move(2)
                bt2 = 0
            if bt3 == 1 and p[0] >= b3pos[0] and p[0] <= b3pos[0] + 300 and p[1] >= b3pos[1] and p[1] <= b3pos[1] + 75:
                pygame.quit()
                exit()
            if bt4 == 1 and p[0] >= b4pos[0] and p[0] <= b4pos[0] + 300 and p[1] >= b4pos[1] and p[1] <= b4pos[1] + 75:
                P()
                bt4 = 0
            if bt5 == 1 and p[0] >= b5pos[0] and p[0] <= b5pos[0] + 300 and p[1] >= b5pos[1] and p[1] <= b5pos[1] + 75:
                PVP()
                bt5 = 0
            if bt7 == 1 and p[0] >= b7pos[0] and p[0] <= b7pos[0] + 300 and p[1] >= b7pos[1] and p[1] <= b7pos[1] + 75:
                move(7)
                bt7 = 0
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.flip()
