
### import modules ###
import pygame
import random
from random import randint
import Tkinter as tk
from Tkinter import *
from pygame import *
import math
#import datetime
import sys
import time
pygame.init()
######################
### map1 ###
def map1():
    ### variables ###
    global score
    score = 0
    t1 = 1
    t2 = 1
    tp = 1
    t2on1 = 0
    t3on1 = 0
    tpon1 = 0
    t2on2 = 0
    t3on2 = 0
    tpon2 = 0
    t2on3 = 0
    t3on3 = 0
    tpon3 = 0
    t2on4 = 0
    t3on4 = 0
    tpon4 = 0
    t2on5 = 0
    t3on5 = 0
    tpon5 = 0
    t2on6 = 0
    t3on6 = 0
    tpon6 = 0
    t2on7 = 0
    t3on7 = 0
    tpon7 = 0
    t2on8 = 0
    t3on8 = 0
    tpon8 = 0
    t2on9 = 0
    t3on9 = 0
    tpon9 = 0
    t2bx = 600
    t2by = 555
    t3bx = 600
    t3by = 510
    tpbx = 490
    tpby = 530
    sbx = 450
    sby = 510
    ubx = 450
    uby = 545
    t2b1=0
    t3b1=0
    tpb1=0
    t2b2=0
    t3b2=0
    tpb2=0
    t2b3=0
    t3b3=0
    tpb3=0
    t2b4=0
    t3b4=0
    tpb4=0
    t2b5=0
    t3b5=0
    tpb5=0
    t2b6=0
    t3b6=0
    tpb6=0
    t2b7=0
    t3b7=0
    tpb7=0
    t2b8=0
    t3b8=0
    tpb8=0
    t2b9=0
    t3b9=0
    tpb9=0
    ### enemy variables ###
    enemy1xmove = 0
    enemy1ymove = 0
    enemy1spd = 0.2
    enemy1x = 20
    enemy1y = 20
    en1hp = 5000
    en1hps = en1hp

    enemy2xmove = 0
    enemy2ymove = 0
    enemy2spd = 0.2
    enemy2x = -10
    enemy2y = 20
    en2hp = 500
    en2hps = en2hp

    enemy3xmove = 0
    enemy3ymove = 0
    enemy3spd = 0.2
    enemy3x = -40
    enemy3y = 20
    en3hp = 500
    en3hps = en3hp

    enemy4xmove = 0
    enemy4ymove = 0
    enemy4spd = 0.2
    enemy4x = -70
    enemy4y = 20
    en4hp = 1000
    en4hps = en4hp

    enemy5xmove = 0
    enemy5ymove = 0
    enemy5spd = 0.2
    enemy5x = -100
    enemy5y = 20
    en5hp = 1000
    en5hps = en5hp

    enemy6xmove = 0
    enemy6ymove = 0
    enemy6spd = 0.2
    enemy6x = -130
    enemy6y = 20
    en6hp = 1000
    en6hps = en6hp

    enemy7xmove = 0
    enemy7ymove = 0
    enemy7spd = 0.2
    enemy7x = -160
    enemy7y = 20
    en7hp = 1000
    en7hps = en7hp

    enemy8xmove = 0
    enemy8ymove = 0
    enemy8spd = 0.2
    enemy8x = -190
    enemy8y = 20
    en8hp = 1000
    en8hps = en8hp

    enemy9xmove = 0
    enemy9ymove = 0
    enemy9spd = 0.2
    enemy9x = -220
    enemy9y = 20
    en9hp = 1000
    en9hps = en9hp

    enemy0xmove = 0
    enemy0ymove = 0
    enemy0spd = 0.2
    enemy0x = -250
    enemy0y = 20
    en0hp = 1000
    en0hps = en0hp
    ### colours ###
    black = [0,0,0]
    rd = [255,0,0]
    bl = [0,0,255]
    grn = [30,255,0]
    wht = [255,255,255]
    prpl = [150,0,250]
    ylw = [255,255,0]
    cyn = [0,150,255]
    pink = [255,20,150]
    grn2 = [50,200,150]
    pinkp = [255,153,153]
    ### tower variable ###
    cft1 = [680,125]
    cf1t2 = [165,125]
    cf1t3 = [165,125]
    cf1tp = [165,125]
    cf2t2 = [365,125]
    cf2t3 = [365,125]
    cf2tp = [365,125]
    cf3t2 = [565,125]
    cf3t3 = [565,125]
    cf3tp = [565,125]
    cf4t2 = [165,275]
    cf4t3 = [165,275]
    cf4tp = [165,275]
    cf5t2 = [365,275]
    cf5t3 = [365,275]
    cf5tp = [365,275]
    cf6t2 = [565,275]
    cf6t3 = [565,275]
    cf6tp = [565,275]
    cf7t2 = [125,405]
    cf7t3 = [125,405]
    cf7tp = [125,405]
    cf8t2 = [275,405]
    cf8t3 = [275,405]
    cf8tp = [275,405]
    cf9t2 = [435,405]
    cf9t3 = [435,405]
    cf9tp = [435,405]
    cft2b = [t2bx + 50,t2by + 20]
    cft3b = [t3bx + 50,t3by + 20]
    cftpb = [tpbx + 50,tpby + 20]
    ### start damage for towers ###
    t2b1d = 0.5
    t3b1d = 0.05
    tpb1d = 5.1
    t2b2d = 0.5
    t3b2d = 0.05
    tpb2d = 5.1
    t2b3d = 0.5
    t3b3d = 0.05
    tpb3d = 5.1
    t2b4d = 0.5
    t3b4d = 0.05
    tpb4d = 5.1
    t2b5d = 0.5
    t3b5d = 0.05
    tpb5d = 5.1
    t2b6d = 0.5
    t3b6d = 0.05
    tpb6d = 5.1
    t2b7d = 0.5
    t3b7d = 0.05
    tpb7d = 5.1
    t2b8d = 0.5
    t3b8d = 0.05
    tpb8d = 5.1
    t2b9d = 0.5
    t3b9d = 0.05
    tpb9d = 5.1
    ### towers variable ###
    zat2 = 0
    zat3 = 0
    zatp = 0
    ### hit box thing var ###
    bx1x = 150
    bx1y = 110
    bx2x = 350
    bx2y = 110
    bx3x = 550
    bx3y = 110
    bx4x = 150
    bx4y = 260
    bx5x = 350
    bx5y = 260
    bx6x = 550
    bx6y = 260
    bx7x = 110
    bx7y = 390
    bx8x = 260
    bx8y = 390
    bx9x = 420
    bx9y = 390
    ### making window ###
    screenx = 800
    screeny = 600
    font = pygame.font.SysFont("calibri",10)
    global screen
    screen = display.set_mode((screenx,screeny))
    display.set_caption('Map_1')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("calibri",20)

    image1 = pygame.image.load('beaver1.jpeg')
    
    money = 987
    ### making enemy surface ###
    enemy1_surf = pygame.Surface((40,40))
    enemy1_surf.set_colorkey(black)
    enemy1rect = enemy1_surf.get_rect()
    enemy1 = pygame.draw.circle(enemy1_surf,(rd),[enemy1rect.centerx, enemy1rect.centery],10)
    enemy1rect.left = enemy1x
    enemy1rect.top = enemy1y

    enemy2_surf = pygame.Surface((40,40))
    enemy2_surf.set_colorkey(black)
    enemy2rect = enemy2_surf.get_rect()
    enemy2 = pygame.draw.circle(enemy2_surf,(rd),[enemy2rect.centerx, enemy2rect.centery],10)
    enemy2rect.left = enemy2x
    enemy2rect.top = enemy2y
    
    enemy3_surf = pygame.Surface((40,40))
    enemy3_surf.set_colorkey(black)
    enemy3rect = enemy3_surf.get_rect()
    enemy3 = pygame.draw.circle(enemy3_surf,(rd),[enemy3rect.centerx, enemy3rect.centery],10)
    enemy3rect.left = enemy3x
    enemy3rect.top = enemy3y

    enemy4_surf = pygame.Surface((40,40))
    enemy4_surf.set_colorkey(black)
    enemy4rect = enemy4_surf.get_rect()
    enemy4 = pygame.draw.circle(enemy4_surf,(rd),[enemy4rect.centerx, enemy4rect.centery],10)
    enemy4rect.left = enemy4x
    enemy4rect.top = enemy4y

    enemy5_surf = pygame.Surface((40,40))
    enemy5_surf.set_colorkey(black)
    enemy5rect = enemy5_surf.get_rect()
    enemy5 = pygame.draw.circle(enemy5_surf,(rd),[enemy5rect.centerx, enemy5rect.centery],10)
    enemy5rect.left = enemy5x
    enemy5rect.top = enemy5y

    enemy6_surf = pygame.Surface((40,40))
    enemy6_surf.set_colorkey(black)
    enemy6rect = enemy6_surf.get_rect()
    enemy6 = pygame.draw.circle(enemy6_surf,(rd),[enemy6rect.centerx, enemy6rect.centery],10)
    enemy6rect.left = enemy6x
    enemy6rect.top = enemy6y

    enemy7_surf = pygame.Surface((40,40))
    enemy7_surf.set_colorkey(black)
    enemy7rect = enemy7_surf.get_rect()
    enemy7 = pygame.draw.circle(enemy7_surf,(rd),[enemy7rect.centerx, enemy7rect.centery],10)
    enemy7rect.left = enemy7x
    enemy7rect.top = enemy7y

    enemy8_surf = pygame.Surface((40,40))
    enemy8_surf.set_colorkey(black)
    enemy8rect = enemy8_surf.get_rect()
    enemy8 = pygame.draw.circle(enemy8_surf,(rd),[enemy8rect.centerx, enemy8rect.centery],10)
    enemy8rect.left = enemy8x
    enemy8rect.top = enemy8y

    enemy9_surf = pygame.Surface((40,40))
    enemy9_surf.set_colorkey(black)
    enemy9rect = enemy9_surf.get_rect()
    enemy9 = pygame.draw.circle(enemy9_surf,(rd),[enemy9rect.centerx, enemy9rect.centery],10)
    enemy9rect.left = enemy9x
    enemy9rect.top = enemy9y

    enemy0_surf = pygame.Surface((40,40))
    enemy0_surf.set_colorkey(black)
    enemy0rect = enemy0_surf.get_rect()
    enemy0 = pygame.draw.circle(enemy0_surf,(rd),[enemy0rect.centerx, enemy0rect.centery],10)
    enemy0rect.left = enemy0x
    enemy0rect.top = enemy0y

    en4slw = 0
    en2slw = 0
    en3slw = 0
    en1slw = 0
    en5slw = 0
    en6slw = 0
    en7slw = 0
    en8slw = 0
    en9slw = 0
    en0slw = 0
    ### while loop ###
    while True:
        display.update()
        screen.fill(black)
        t1 = 1
        t2 = 1
        tp = 1
        en4slw = 0
        en2slw = 0
        en3slw = 0
        en1slw = 0
        en5slw = 0
        en6slw = 0
        en7slw = 0
        en8slw = 0
        en9slw = 0
        en0slw = 0
        ### maze ###
        pygame.draw.rect(screen,(bl),Rect((5,5),(screenx - 10, screeny - 100)),2)
        pygame.draw.rect(screen,(grn),((10,100),(700,50)))
        pygame.draw.rect(screen,(grn),(100,250,690,50))
        pygame.draw.rect(screen,(grn),(100,300,60,150))
        pygame.draw.rect(screen,(grn),(250,360,60,140))
        pygame.draw.rect(screen,(grn),(400,300,60,150))
        pygame.draw.circle(screen,(cyn),(600,400),65)
        pygame.draw.polygon(screen, (bl),([cft1[0]-15,cft1[1]-15],[cft1[0]+15,cft1[1]-15],[cft1[0],cft1[1]+15]),5)

        pygame.draw.rect(screen,(grn2),(150,110,30,30))
        pygame.draw.rect(screen,(grn2),(350,110,30,30))
        pygame.draw.rect(screen,(grn2),(550,110,30,30))
        pygame.draw.rect(screen,(grn2),(150,260,30,30))
        pygame.draw.rect(screen,(grn2),(350,260,30,30))
        pygame.draw.rect(screen,(grn2),(550,260,30,30))
        pygame.draw.rect(screen,(grn2),(110,390,30,30))
        pygame.draw.rect(screen,(grn2),(260,390,30,30))
        pygame.draw.rect(screen,(grn2),(420,390,30,30))

        screen.blit(image1,(550,360))
        ### pic of t2 button ###
        pygame.draw.rect(screen,(ylw),(t2bx,t2by,100,40))
        pygame.draw.polygon(screen, (bl),([cft2b[0]-15,cft2b[1]-15],[cft2b[0]+15,cft2b[1]-15],[cft2b[0],cft2b[1]+15]),5)
        ### pic of t3 button ###
        pygame.draw.rect(screen,(ylw),(t3bx,t3by,100,40))
        pygame.draw.polygon(screen, (bl),([cft3b[0]-15,cft3b[1]+15],[cft3b[0]+15,cft3b[1]+15],[cft3b[0],cft3b[1]-15]),5)
        ### pic of tp button ###
        pygame.draw.rect(screen,(ylw),(tpbx,tpby,100,40))
        pygame.draw.circle(screen,(bl),(cftpb[0],cftpb[1]),15,5)
        ### pic of selling button ###
        if t2on1 == 1 or t3on1 == 1 or t2on2 == 1 or t3on2 == 1 or t2on3 == 1 or t3on3 == 1 or t2on4 == 1 or t3on4 == 1 or t2on5 == 1 or t3on5 == 1 or t2on6 == 1 or t3on6 == 1 or t2on7 == 1 or t3on7 == 1 or t2on8 == 1 or t3on8 == 1 or t2on9 == 1 or t3on9 == 1 or tpon1==1 or tpon2==1 or tpon3==1 or tpon4==1 or tpon5==1 or tpon6==1 or tpon7==1 or tpon8==1 or tpon9==1:
            if t2b1 == 1 or t3b1 == 1 or t2b2 == 1 or t3b2 == 1 or t2b3 == 1 or t3b3 == 1 or t2b4 == 1 or t3b4 == 1 or t2b5 == 1 or t3b5 == 1 or t2b6 == 1 or t3b6 == 1 or t2b7 == 1 or t3b7 == 1 or t2b8 == 1 or t3b8 == 1 or t2b9 == 1 or t3b9 == 1 or tpb1==1 or tpb2==1 or tpb3==1 or tpb4==1 or tpb5==1 or tpb6==1 or tpb7==1 or tpb8==1 or tpb9==1:
                pygame.draw.rect(screen,(ylw),(sbx,sby,30,30))
                if money > 9:
                    pygame.draw.rect(screen,(grn2),(ubx,uby,30,30))
                else:
                    pygame.draw.rect(screen,(rd),(ubx,uby,30,30))
        ### tower making stuff ###
        if t2on1 == 1:
            pygame.draw.polygon(screen, (bl),([cf1t2[0]-15,cf1t2[1]-15],[cf1t2[0]+15,cf1t2[1]-15],[cf1t2[0],cf1t2[1]+15]),5)
        if t3on1 == 1:
            pygame.draw.polygon(screen, (bl),([cf1t3[0]-15,cf1t3[1]+15],[cf1t3[0]+15,cf1t3[1]+15],[cf1t3[0],cf1t3[1]-15]),5)
        if tpon1 == 1:
            pygame.draw.circle(screen,(bl),(cf1tp[0],cf1tp[1]),15,5)
        if t2on2 == 1:
            pygame.draw.polygon(screen, (bl),([cf2t2[0]-15,cf2t2[1]-15],[cf2t2[0]+15,cf2t2[1]-15],[cf2t2[0],cf2t2[1]+15]),5)
        if t3on2 == 1:
            pygame.draw.polygon(screen, (bl),([cf2t3[0]-15,cf2t3[1]+15],[cf2t3[0]+15,cf2t3[1]+15],[cf2t3[0],cf2t3[1]-15]),5)
        if tpon2 == 1:
            pygame.draw.circle(screen,(bl),(cf2tp[0],cf2tp[1]),15,5)
        if t2on3 == 1:
            pygame.draw.polygon(screen, (bl),([cf3t2[0]-15,cf3t2[1]-15],[cf3t2[0]+15,cf3t2[1]-15],[cf3t2[0],cf3t2[1]+15]),5)
        if t3on3 == 1:
            pygame.draw.polygon(screen, (bl),([cf3t3[0]-15,cf3t3[1]+15],[cf3t3[0]+15,cf3t3[1]+15],[cf3t3[0],cf3t3[1]-15]),5)
        if tpon3 == 1:
            pygame.draw.circle(screen,(bl),(cf3tp[0],cf3tp[1]),15,5)
        if t2on4 == 1:
            pygame.draw.polygon(screen, (bl),([cf4t2[0]-15,cf4t2[1]-15],[cf4t2[0]+15,cf4t2[1]-15],[cf4t2[0],cf4t2[1]+15]),5)
        if t3on4 == 1:
            pygame.draw.polygon(screen, (bl),([cf4t3[0]-15,cf4t3[1]+15],[cf4t3[0]+15,cf4t3[1]+15],[cf4t3[0],cf4t3[1]-15]),5)
        if tpon4 == 1:
            pygame.draw.circle(screen,(bl),(cf4tp[0],cf4tp[1]),15,5)
        if t2on5 == 1:
            pygame.draw.polygon(screen, (bl),([cf5t2[0]-15,cf5t2[1]-15],[cf5t2[0]+15,cf5t2[1]-15],[cf5t2[0],cf5t2[1]+15]),5)
        if t3on5 == 1:
            pygame.draw.polygon(screen, (bl),([cf5t3[0]-15,cf5t3[1]+15],[cf5t3[0]+15,cf5t3[1]+15],[cf5t3[0],cf5t3[1]-15]),5)
        if tpon5 == 1:
            pygame.draw.circle(screen,(bl),(cf5tp[0],cf5tp[1]),15,5)
        if t2on6 == 1:
            pygame.draw.polygon(screen, (bl),([cf6t2[0]-15,cf6t2[1]-15],[cf6t2[0]+15,cf6t2[1]-15],[cf6t2[0],cf6t2[1]+15]),5)
        if t3on6 == 1:
            pygame.draw.polygon(screen, (bl),([cf6t3[0]-15,cf6t3[1]+15],[cf6t3[0]+15,cf6t3[1]+15],[cf6t3[0],cf6t3[1]-15]),5)
        if tpon6 == 1:
            pygame.draw.circle(screen,(bl),(cf6tp[0],cf6tp[1]),15,5)
        if t2on7 == 1:
            pygame.draw.polygon(screen, (bl),([cf7t2[0]-15,cf7t2[1]-15],[cf7t2[0]+15,cf7t2[1]-15],[cf7t2[0],cf7t2[1]+15]),5)
        if t3on7 == 1:
            pygame.draw.polygon(screen, (bl),([cf7t3[0]-15,cf7t3[1]+15],[cf7t3[0]+15,cf7t3[1]+15],[cf7t3[0],cf7t3[1]-15]),5)
        if tpon7 == 1:
            pygame.draw.circle(screen,(bl),(cf7tp[0],cf7tp[1]),15,5)
        if t2on8 == 1:
            pygame.draw.polygon(screen, (bl),([cf8t2[0]-15,cf8t2[1]-15],[cf8t2[0]+15,cf8t2[1]-15],[cf8t2[0],cf8t2[1]+15]),5)
        if t3on8 == 1:
            pygame.draw.polygon(screen, (bl),([cf8t3[0]-15,cf8t3[1]+15],[cf8t3[0]+15,cf8t3[1]+15],[cf8t3[0],cf8t3[1]-15]),5)
        if tpon8 == 1:
            pygame.draw.circle(screen,(bl),(cf8tp[0],cf8tp[1]),15,5)
        if t2on9 == 1:
            pygame.draw.polygon(screen, (bl),([cf9t2[0]-15,cf9t2[1]-15],[cf9t2[0]+15,cf9t2[1]-15],[cf9t2[0],cf9t2[1]+15]),5)
        if t3on9 == 1:
            pygame.draw.polygon(screen, (bl),([cf9t3[0]-15,cf9t3[1]+15],[cf9t3[0]+15,cf9t3[1]+15],[cf9t3[0],cf9t3[1]-15]),5)
        if tpon9 == 1:
            pygame.draw.circle(screen,(bl),(cf9tp[0],cf9tp[1]),15,5)
        ### enemy health bars ###
        pygame.draw.rect(screen,(cyn),(enemy1x+5,enemy1y,((en1hp/en1hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy2x+5,enemy2y,((en2hp/en2hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy3x+5,enemy3y,((en3hp/en3hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy4x+5,enemy4y,((en4hp/en4hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy5x+5,enemy5y,((en5hp/en5hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy6x+5,enemy6y,((en6hp/en6hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy7x+5,enemy7y,((en7hp/en7hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy8x+5,enemy8y,((en8hp/en8hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy9x+5,enemy9y,((en9hp/en9hps)*24),5))
        pygame.draw.rect(screen,(cyn),(enemy0x+5,enemy0y,((en0hp/en0hps)*24),5))
        ### dolla ###
        p = font.render(str('Your dolla: %i' % money),True,(ylw))
        screen.blit(p,(50,520))
        ### score ###
        q = font.render(str('Your score: %i' % score),True,(ylw))
        screen.blit(q,(50,570))
        ### path of enemy 1 ###
        if en1hp > 0:
            screen.blit(enemy1_surf,(enemy1x,enemy1y))
        else:
            enemy1spd = 0
            
        enemy1xmove = enemy1spd
        enemy1ymove = enemy1spd
        
        if enemy1x < 750 and enemy1y < 190:
            enemy1x += enemy1xmove
        elif enemy1x > 740 and enemy1y < 200:
            enemy1y += enemy1ymove
        elif enemy1y > 190 and enemy1x > 50 and enemy1y < 290:
            enemy1x -= enemy1xmove
        elif enemy1x < 60 and enemy1y > 190 and enemy1y < 460:
            enemy1y += enemy1ymove
        elif enemy1y > 450 and enemy1x < 200:
            enemy1x += enemy1xmove
        elif enemy1x > 190 and enemy1y > 300 and enemy1x < 300:
            enemy1y -= enemy1ymove
        elif enemy1y > 200 and enemy1x < 340:
            enemy1x += enemy1xmove
        elif enemy1x > 330 and enemy1y < 450 and enemy1x < 450:
            enemy1y += enemy1ymove
        elif enemy1y > 440 and enemy1x > 300 and enemy1x < 600:
            enemy1x += enemy1xmove
        elif enemy1x < 750 and enemy1y < 550 and enemy1y > 400:
            enemy1y -= enemy1ymove
        else:
            execfile('endgame.py')
            return
            
        ### path of enemy 2 ###
        if en2hp > 0:
            screen.blit(enemy2_surf,(enemy2x,enemy2y)) 
        else:
            enemy2spd = 0
            
        enemy2xmove = enemy2spd
        enemy2ymove = enemy2spd
        
        if enemy2x < 750 and enemy2y < 190:
            enemy2x += enemy2xmove
        elif enemy2x > 740 and enemy2y < 200:
            enemy2y += enemy2ymove
        elif enemy2y > 190 and enemy2x > 50 and enemy2y < 290:
            enemy2x -= enemy2xmove
        elif enemy2x < 60 and enemy2y > 190 and enemy2y < 460:
            enemy2y += enemy2ymove
        elif enemy2y > 450 and enemy2x < 200:
            enemy2x += enemy2xmove
        elif enemy2x > 190 and enemy2y > 300 and enemy2x < 300:
            enemy2y -= enemy2ymove
        elif enemy2y > 200 and enemy2x < 340:
            enemy2x += enemy2xmove
        elif enemy2x > 330 and enemy2y < 450 and enemy2x < 450:
            enemy2y += enemy2ymove
        elif enemy2y > 440 and enemy2x > 300 and enemy2x < 600:
            enemy2x += enemy2xmove
        elif enemy2x < 750 and enemy2y < 550 and enemy2y > 400:
            enemy2y -= enemy2ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy3 ###
        if en3hp > 0:
            screen.blit(enemy3_surf,(enemy3x,enemy3y))
        else:
            enemy3spd = 0
            
        enemy3xmove = enemy3spd
        enemy3ymove = enemy3spd
        
        if enemy3x < 750 and enemy3y < 190:
            enemy3x += enemy3xmove
        elif enemy3x > 740 and enemy3y < 200:
            enemy3y += enemy3ymove
        elif enemy3y > 190 and enemy3x > 50 and enemy3y < 290:
            enemy3x -= enemy3xmove
        elif enemy3x < 60 and enemy3y > 190 and enemy3y < 460:
            enemy3y += enemy3ymove
        elif enemy3y > 450 and enemy3x < 200:
            enemy3x += enemy3xmove
        elif enemy3x > 190 and enemy3y > 300 and enemy3x < 300:
            enemy3y -= enemy3ymove
        elif enemy3y > 200 and enemy3x < 340:
            enemy3x += enemy3xmove
        elif enemy3x > 330 and enemy3y < 450 and enemy3x < 450:
            enemy3y += enemy3ymove
        elif enemy3y > 440 and enemy3x > 300 and enemy3x < 600:
            enemy3x += enemy3xmove
        elif enemy3x < 750 and enemy3y < 550 and enemy3y > 400:
            enemy3y -= enemy3ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy4 ###
        if en4hp > 0:
            screen.blit(enemy4_surf,(enemy4x,enemy4y))
        else:
            enemy4spd = 0
            
        enemy4xmove = enemy4spd
        enemy4ymove = enemy4spd
        
        if enemy4x < 750 and enemy4y < 190:
            enemy4x += enemy4xmove
        elif enemy4x > 740 and enemy4y < 200:
            enemy4y += enemy4ymove
        elif enemy4y > 190 and enemy4x > 50 and enemy4y < 290:
            enemy4x -= enemy4xmove
        elif enemy4x < 60 and enemy4y > 190 and enemy4y < 460:
            enemy4y += enemy4ymove
        elif enemy4y > 450 and enemy4x < 200:
            enemy4x += enemy4xmove
        elif enemy4x > 190 and enemy4y > 300 and enemy4x < 300:
            enemy4y -= enemy4ymove
        elif enemy4y > 200 and enemy4x < 340:
            enemy4x += enemy4xmove
        elif enemy4x > 330 and enemy4y < 450 and enemy4x < 450:
            enemy4y += enemy4ymove
        elif enemy4y > 440 and enemy4x > 300 and enemy4x < 600:
            enemy4x += enemy4xmove
        elif enemy4x < 750 and enemy4y < 550 and enemy4y > 400:
            enemy4y -= enemy4ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy 5 ###
        if en5hp > 0:
            screen.blit(enemy5_surf,(enemy5x,enemy5y)) 
        else:
            enemy5spd = 0
            
        enemy5xmove = enemy5spd
        enemy5ymove = enemy5spd
        
        if enemy5x < 750 and enemy5y < 190:
            enemy5x += enemy5xmove
        elif enemy5x > 740 and enemy5y < 200:
            enemy5y += enemy5ymove
        elif enemy5y > 190 and enemy5x > 50 and enemy5y < 290:
            enemy5x -= enemy5xmove
        elif enemy5x < 60 and enemy5y > 190 and enemy5y < 460:
            enemy5y += enemy5ymove
        elif enemy5y > 450 and enemy5x < 200:
            enemy5x += enemy5xmove
        elif enemy5x > 190 and enemy5y > 300 and enemy5x < 300:
            enemy5y -= enemy5ymove
        elif enemy5y > 200 and enemy5x < 340:
            enemy5x += enemy5xmove
        elif enemy5x > 330 and enemy5y < 450 and enemy5x < 450:
            enemy5y += enemy5ymove
        elif enemy5y > 440 and enemy5x > 300 and enemy5x < 600:
            enemy5x += enemy5xmove
        elif enemy5x < 750 and enemy5y < 550 and enemy5y > 400:
            enemy5y -= enemy5ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy 2 ###
        if en6hp > 0:
            screen.blit(enemy6_surf,(enemy6x,enemy6y)) 
        else:
            enemy6spd = 0
            
        enemy6xmove = enemy6spd
        enemy6ymove = enemy6spd
        
        if enemy6x < 750 and enemy6y < 190:
            enemy6x += enemy6xmove
        elif enemy6x > 740 and enemy6y < 200:
            enemy6y += enemy6ymove
        elif enemy6y > 190 and enemy6x > 50 and enemy6y < 290:
            enemy6x -= enemy6xmove
        elif enemy6x < 60 and enemy6y > 190 and enemy6y < 460:
            enemy6y += enemy6ymove
        elif enemy6y > 450 and enemy6x < 200:
            enemy6x += enemy6xmove
        elif enemy6x > 190 and enemy6y > 300 and enemy6x < 300:
            enemy6y -= enemy6ymove
        elif enemy6y > 200 and enemy6x < 340:
            enemy6x += enemy6xmove
        elif enemy6x > 330 and enemy6y < 450 and enemy6x < 450:
            enemy6y += enemy6ymove
        elif enemy6y > 440 and enemy6x > 300 and enemy6x < 600:
            enemy6x += enemy6xmove
        elif enemy6x < 750 and enemy6y < 550 and enemy6y > 400:
            enemy6y -= enemy6ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy 2 ###
        if en7hp > 0:
            screen.blit(enemy7_surf,(enemy7x,enemy7y)) 
        else:
            enemy7spd = 0
            
        enemy7xmove = enemy7spd
        enemy7ymove = enemy7spd
        
        if enemy7x < 750 and enemy7y < 190:
            enemy7x += enemy7xmove
        elif enemy7x > 740 and enemy7y < 200:
            enemy7y += enemy7ymove
        elif enemy7y > 190 and enemy7x > 50 and enemy7y < 290:
            enemy7x -= enemy7xmove
        elif enemy7x < 60 and enemy7y > 190 and enemy7y < 460:
            enemy7y += enemy7ymove
        elif enemy7y > 450 and enemy7x < 200:
            enemy7x += enemy7xmove
        elif enemy7x > 190 and enemy7y > 300 and enemy7x < 300:
            enemy7y -= enemy7ymove
        elif enemy7y > 200 and enemy7x < 340:
            enemy7x += enemy7xmove
        elif enemy7x > 330 and enemy7y < 450 and enemy7x < 450:
            enemy7y += enemy7ymove
        elif enemy7y > 440 and enemy7x > 300 and enemy7x < 600:
            enemy7x += enemy7xmove
        elif enemy7x < 750 and enemy7y < 550 and enemy7y > 400:
            enemy7y -= enemy7ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy 8 ###
        if en8hp > 0:
            screen.blit(enemy8_surf,(enemy8x,enemy8y)) 
        else:
            enemy8spd = 0
            
        enemy8xmove = enemy8spd
        enemy8ymove = enemy8spd
        
        if enemy8x < 750 and enemy8y < 190:
            enemy8x += enemy8xmove
        elif enemy8x > 740 and enemy8y < 200:
            enemy8y += enemy8ymove
        elif enemy8y > 190 and enemy8x > 50 and enemy8y < 290:
            enemy8x -= enemy8xmove
        elif enemy8x < 60 and enemy8y > 190 and enemy8y < 460:
            enemy8y += enemy8ymove
        elif enemy8y > 450 and enemy8x < 200:
            enemy8x += enemy8xmove
        elif enemy8x > 190 and enemy8y > 300 and enemy8x < 300:
            enemy8y -= enemy8ymove
        elif enemy8y > 200 and enemy8x < 340:
            enemy8x += enemy8xmove
        elif enemy8x > 330 and enemy8y < 450 and enemy8x < 450:
            enemy8y += enemy8ymove
        elif enemy8y > 440 and enemy8x > 300 and enemy8x < 600:
            enemy8x += enemy8xmove
        elif enemy8x < 750 and enemy8y < 550 and enemy8y > 400:
            enemy8y -= enemy8ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy 2 ###
        if en9hp > 0:
            screen.blit(enemy9_surf,(enemy9x,enemy9y)) 
        else:
            enemy9spd = 0
            
        enemy9xmove = enemy9spd
        enemy9ymove = enemy9spd
        
        if enemy9x < 750 and enemy9y < 190:
            enemy9x += enemy9xmove
        elif enemy9x > 740 and enemy9y < 200:
            enemy9y += enemy9ymove
        elif enemy9y > 190 and enemy9x > 50 and enemy9y < 290:
            enemy9x -= enemy9xmove
        elif enemy9x < 60 and enemy9y > 190 and enemy9y < 460:
            enemy9y += enemy9ymove
        elif enemy9y > 450 and enemy9x < 200:
            enemy9x += enemy9xmove
        elif enemy9x > 190 and enemy9y > 300 and enemy9x < 300:
            enemy9y -= enemy9ymove
        elif enemy9y > 200 and enemy9x < 340:
            enemy9x += enemy9xmove
        elif enemy9x > 330 and enemy9y < 450 and enemy9x < 450:
            enemy9y += enemy9ymove
        elif enemy9y > 440 and enemy9x > 300 and enemy9x < 600:
            enemy9x += enemy9xmove
        elif enemy9x < 750 and enemy9y < 550 and enemy9y > 400:
            enemy9y -= enemy9ymove
        else:
            execfile('endgame.py')
            return
        ### path of enemy 2 ###
        if en0hp > 0:
            screen.blit(enemy0_surf,(enemy0x,enemy0y)) 
        else:
            enemy0spd = 0
            
        enemy0xmove = enemy0spd
        enemy0ymove = enemy0spd
        
        if enemy0x < 750 and enemy0y < 190:
            enemy0x += enemy0xmove
        elif enemy0x > 740 and enemy0y < 200:
            enemy0y += enemy0ymove
        elif enemy0y > 190 and enemy0x > 50 and enemy0y < 290:
            enemy0x -= enemy0xmove
        elif enemy0x < 60 and enemy0y > 190 and enemy0y < 460:
            enemy0y += enemy0ymove
        elif enemy0y > 450 and enemy0x < 200:
            enemy0x += enemy0xmove
        elif enemy0x > 190 and enemy0y > 300 and enemy0x < 300:
            enemy0y -= enemy0ymove
        elif enemy0y > 200 and enemy0x < 340:
            enemy0x += enemy0xmove
        elif enemy0x > 330 and enemy0y < 450 and enemy0x < 450:
            enemy0y += enemy0ymove
        elif enemy0y > 440 and enemy0x > 300 and enemy0x < 600:
            enemy0x += enemy0xmove
        elif enemy0x < 750 and enemy0y < 550 and enemy0y > 400:
            enemy0y -= enemy0ymove
        else:
            execfile('endgame.py')
            return
        ### tower1 shooting ###
        if math.sqrt(((math.fabs(cft1[0]- enemy1x))**2) + ((math.fabs(cft1[1] - enemy1y))**2)) < 150 and en1hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cft1),5)
            t1 += 1
            en1hp -= 0.5

        if math.sqrt(((math.fabs(cft1[0]- enemy2x))**2) + ((math.fabs(cft1[1] - enemy2y))**2)) < 150 and en2hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cft1),5)
            t1 += 1
            en2hp -= 0.5
            
        if math.sqrt(((math.fabs(cft1[0]- enemy3x))**2) + ((math.fabs(cft1[1] - enemy3y))**2)) < 150 and en3hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cft1),5)
            t1 += 1
            en3hp -= 0.5

        if math.sqrt(((math.fabs(cft1[0]- enemy4x))**2) + ((math.fabs(cft1[1] - enemy4y))**2)) < 150 and en4hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cft1),5)
            t1 += 1
            en4hp -= 0.5
        if math.sqrt(((math.fabs(cft1[0]- enemy5x))**2) + ((math.fabs(cft1[1] - enemy5y))**2)) < 150 and en5hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cft1),5)
            t1 += 1
            en5hp -= 0.5
        if math.sqrt(((math.fabs(cft1[0]- enemy6x))**2) + ((math.fabs(cft1[1] - enemy6y))**2)) < 150 and en6hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cft1),5)
            t1 += 1
            en6hp -= 0.5
        if math.sqrt(((math.fabs(cft1[0]- enemy7x))**2) + ((math.fabs(cft1[1] - enemy7y))**2)) < 150 and en7hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cft1),5)
            t1 += 1
            en7hp -= 0.5
        if math.sqrt(((math.fabs(cft1[0]- enemy8x))**2) + ((math.fabs(cft1[1] - enemy8y))**2)) < 150 and en8hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cft1),5)
            t1 += 1
            en8hp -= 0.5
        if math.sqrt(((math.fabs(cft1[0]- enemy9x))**2) + ((math.fabs(cft1[1] - enemy9y))**2)) < 150 and en9hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cft1),5)
            t1 += 1
            en9hp -= 0.5
        if math.sqrt(((math.fabs(cft1[0]- enemy0x))**2) + ((math.fabs(cft1[1] - enemy0y))**2)) < 150 and en0hp > -10 and t1 < 2:
            pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cft1),5)
            t1 += 1
            en0hp -= 0.5
            
        t1 -= 1
        ### box 1 ###
        ### tower2 shooting ###
        if t2on1 == 1:
            if math.sqrt(((math.fabs(cf1t2[0]- enemy1x))**2) + ((math.fabs(cf1t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf1t2),5)
                t2 += 1
                en1hp -= t2b1d

            if math.sqrt(((math.fabs(cf1t2[0]- enemy2x))**2) + ((math.fabs(cf1t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf1t2),5)
                t2 += 1
                en2hp -= t2b1d
                
            if math.sqrt(((math.fabs(cf1t2[0]- enemy3x))**2) + ((math.fabs(cf1t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf1t2),5)
                t2 += 1
                en3hp -= t2b1d

            if math.sqrt(((math.fabs(cf1t2[0]- enemy4x))**2) + ((math.fabs(cf1t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf1t2),5)
                t2 += 1
                en4hp -= t2b1d
            if math.sqrt(((math.fabs(cf1t2[0]- enemy5x))**2) + ((math.fabs(cf1t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf1t2),5)
                t2 += 1
                en5hp -= t2b1d
            if math.sqrt(((math.fabs(cf1t2[0]- enemy6x))**2) + ((math.fabs(cf1t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf1t2),5)
                t2 += 1
                en6hp -= t2b1d
            if math.sqrt(((math.fabs(cf1t2[0]- enemy7x))**2) + ((math.fabs(cf1t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf1t2),5)
                t2 += 1
                en7hp -= t2b1d
            if math.sqrt(((math.fabs(cf1t2[0]- enemy8x))**2) + ((math.fabs(cf1t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf1t2),5)
                t2 += 1
                en8hp -= t2b1d
            if math.sqrt(((math.fabs(cf1t2[0]- enemy9x))**2) + ((math.fabs(cf1t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf1t2),5)
                t2 += 1
                en9hp -= t2b1d
            if math.sqrt(((math.fabs(cf1t2[0]- enemy0x))**2) + ((math.fabs(cf1t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf1t2),5)
                t2 += 1
                en0hp -= t2b1d
            t2 -= 1
        ### tower3 shooting ###
        if t3on1 == 1:
            if math.sqrt(((math.fabs(cf1t3[0]- enemy1x))**2) + ((math.fabs(cf1t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf1t3),5)
                en1hp -= t3b1d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy2x))**2) + ((math.fabs(cf1t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf1t3),5)
                en2hp -= t3b1d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy3x))**2) + ((math.fabs(cf1t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf1t3),5)
                en3hp -= t3b1d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy4x))**2) + ((math.fabs(cf1t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf1t3),5)
                en4hp -= t3b1d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy5x))**2) + ((math.fabs(cf1t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf1t3),5)
                en5hp -= t3b1d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy6x))**2) + ((math.fabs(cf1t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf1t3),5)
                en6hp -= t3b1d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy7x))**2) + ((math.fabs(cf1t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf1t3),5)
                en7hp -= t3b1d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy8x))**2) + ((math.fabs(cf1t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf1t3),5)
                en8hp -= t3b1d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy9x))**2) + ((math.fabs(cf1t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf1t3),5)
                en9hp -= t3b1d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf1t3[0]- enemy0x))**2) + ((math.fabs(cf1t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf1t3),5)
                en0hp -= t3b1d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon1 == 1:
            if math.sqrt(((math.fabs(cf1tp[0]- enemy1x))**2) + ((math.fabs(cf1tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en1hp -= tpb1d

            if math.sqrt(((math.fabs(cf1tp[0]- enemy2x))**2) + ((math.fabs(cf1tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en2hp -= tpb1d
                
            if math.sqrt(((math.fabs(cf1tp[0]- enemy3x))**2) + ((math.fabs(cf1tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en3hp -= tpb1d

            if math.sqrt(((math.fabs(cf1tp[0]- enemy4x))**2) + ((math.fabs(cf1tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en4hp -= tpb1d
            if math.sqrt(((math.fabs(cf1tp[0]- enemy5x))**2) + ((math.fabs(cf1tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en5hp -= tpb1d
            if math.sqrt(((math.fabs(cf1tp[0]- enemy6x))**2) + ((math.fabs(cf1tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en6hp -= tpb1d
            if math.sqrt(((math.fabs(cf1tp[0]- enemy7x))**2) + ((math.fabs(cf1tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en7hp -= tpb1d
            if math.sqrt(((math.fabs(cf1tp[0]- enemy8x))**2) + ((math.fabs(cf1tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en8hp -= tpb1d
            if math.sqrt(((math.fabs(cf1tp[0]- enemy9x))**2) + ((math.fabs(cf1tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en9hp -= tpb1d
            if math.sqrt(((math.fabs(cf1tp[0]- enemy0x))**2) + ((math.fabs(cf1tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf1tp[0],cf1tp[1]]),5)
                tp += 1
                en0hp -= tpb1d
            tp -= 1
        ### box 2 ###
        ### tower2 shooting ###
        if t2on2 == 1:
            if math.sqrt(((math.fabs(cf2t2[0]- enemy1x))**2) + ((math.fabs(cf2t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf2t2),5)
                t2 += 1
                en1hp -= t2b2d

            if math.sqrt(((math.fabs(cf2t2[0]- enemy2x))**2) + ((math.fabs(cf2t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf2t2),5)
                t2 += 1
                en2hp -= t2b2d
                
            if math.sqrt(((math.fabs(cf2t2[0]- enemy3x))**2) + ((math.fabs(cf2t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf2t2),5)
                t2 += 1
                en3hp -= t2b2d

            if math.sqrt(((math.fabs(cf2t2[0]- enemy4x))**2) + ((math.fabs(cf2t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf2t2),5)
                t2 += 1
                en4hp -= t2b2d
            if math.sqrt(((math.fabs(cf2t2[0]- enemy5x))**2) + ((math.fabs(cf2t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf2t2),5)
                t2 += 1
                en5hp -= t2b2d
            if math.sqrt(((math.fabs(cf2t2[0]- enemy6x))**2) + ((math.fabs(cf2t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf2t2),5)
                t2 += 1
                en6hp -= t2b2d
            if math.sqrt(((math.fabs(cf2t2[0]- enemy7x))**2) + ((math.fabs(cf2t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf2t2),5)
                t2 += 1
                en7hp -= t2b2d
            if math.sqrt(((math.fabs(cf2t2[0]- enemy8x))**2) + ((math.fabs(cf2t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf2t2),5)
                t2 += 1
                en8hp -= t2b2d
            if math.sqrt(((math.fabs(cf2t2[0]- enemy9x))**2) + ((math.fabs(cf2t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf2t2),5)
                t2 += 1
                en9hp -= t2b2d
            if math.sqrt(((math.fabs(cf2t2[0]- enemy0x))**2) + ((math.fabs(cf2t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf2t2),5)
                t2 += 1
                en0hp -= t2b2d
            t2 -= 1
        ### tower3 shooting ###
        if t3on2 == 1:
            if math.sqrt(((math.fabs(cf2t3[0]- enemy1x))**2) + ((math.fabs(cf2t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf2t3),5)
                en1hp -= t3b2d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy2x))**2) + ((math.fabs(cf2t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf2t3),5)
                en2hp -= t3b2d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy3x))**2) + ((math.fabs(cf2t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf2t3),5)
                en3hp -= t3b2d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy4x))**2) + ((math.fabs(cf2t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf2t3),5)
                en4hp -= t3b2d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy5x))**2) + ((math.fabs(cf2t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf2t3),5)
                en5hp -= t3b2d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy6x))**2) + ((math.fabs(cf2t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf2t3),5)
                en6hp -= t3b2d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy7x))**2) + ((math.fabs(cf2t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf2t3),5)
                en7hp -= t3b2d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy8x))**2) + ((math.fabs(cf2t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf2t3),5)
                en8hp -= t3b2d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy9x))**2) + ((math.fabs(cf2t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf2t3),5)
                en9hp -= t3b2d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf2t3[0]- enemy0x))**2) + ((math.fabs(cf2t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf2t3),5)
                en0hp -= t3b2d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon2 == 1:
            if math.sqrt(((math.fabs(cf2tp[0]- enemy1x))**2) + ((math.fabs(cf2tp[1] - enemy1y))**2)) < 150 and en1hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en1hp -= tpb2d

            if math.sqrt(((math.fabs(cf2tp[0]- enemy2x))**2) + ((math.fabs(cf2tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en2hp -= tpb2d
                
            if math.sqrt(((math.fabs(cf2tp[0]- enemy3x))**2) + ((math.fabs(cf2tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en3hp -= tpb2d

            if math.sqrt(((math.fabs(cf2tp[0]- enemy4x))**2) + ((math.fabs(cf2tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en4hp -= tpb2d
            if math.sqrt(((math.fabs(cf2tp[0]- enemy5x))**2) + ((math.fabs(cf2tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en5hp -= tpb2d
            if math.sqrt(((math.fabs(cf2tp[0]- enemy6x))**2) + ((math.fabs(cf2tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en6hp -= tpb2d
            if math.sqrt(((math.fabs(cf2tp[0]- enemy7x))**2) + ((math.fabs(cf2tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en7hp -= tpb2d
            if math.sqrt(((math.fabs(cf2tp[0]- enemy8x))**2) + ((math.fabs(cf2tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en8hp -= tpb2d
            if math.sqrt(((math.fabs(cf2tp[0]- enemy9x))**2) + ((math.fabs(cf2tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en9hp -= tpb2d
            if math.sqrt(((math.fabs(cf2tp[0]- enemy0x))**2) + ((math.fabs(cf2tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf2tp[0],cf2tp[1]]),5)
                tp += 1
                en0hp -= tpb2d
            tp -= 1
        ### box 3 ###
        ### tower2 shooting ###
        if t2on3 == 1:
            if math.sqrt(((math.fabs(cf3t2[0]- enemy1x))**2) + ((math.fabs(cf3t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf3t2),5)
                t2 += 1
                en1hp -= t2b3d

            if math.sqrt(((math.fabs(cf3t2[0]- enemy2x))**2) + ((math.fabs(cf3t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf3t2),5)
                t2 += 1
                en2hp -= t2b3d
                
            if math.sqrt(((math.fabs(cf3t2[0]- enemy3x))**2) + ((math.fabs(cf3t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf3t2),5)
                t2 += 1
                en3hp -= t2b3d

            if math.sqrt(((math.fabs(cf3t2[0]- enemy4x))**2) + ((math.fabs(cf3t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf3t2),5)
                t2 += 1
                en4hp -= t2b3d
            if math.sqrt(((math.fabs(cf3t2[0]- enemy5x))**2) + ((math.fabs(cf3t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf3t2),5)
                t2 += 1
                en5hp -= t2b3d
            if math.sqrt(((math.fabs(cf3t2[0]- enemy6x))**2) + ((math.fabs(cf3t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf3t2),5)
                t2 += 1
                en6hp -= t2b3d
            if math.sqrt(((math.fabs(cf3t2[0]- enemy7x))**2) + ((math.fabs(cf3t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf3t2),5)
                t2 += 1
                en7hp -= t2b3d
            if math.sqrt(((math.fabs(cf3t2[0]- enemy8x))**2) + ((math.fabs(cf3t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf3t2),5)
                t2 += 1
                en8hp -= t2b3d
            if math.sqrt(((math.fabs(cf3t2[0]- enemy9x))**2) + ((math.fabs(cf3t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf3t2),5)
                t2 += 1
                en9hp -= t2b3d
            if math.sqrt(((math.fabs(cf3t2[0]- enemy0x))**2) + ((math.fabs(cf3t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf3t2),5)
                t2 += 1
                en0hp -= t2b3d
            t2 -= 1
        ### tower3 shooting ###
        if t3on3 == 1:
            if math.sqrt(((math.fabs(cf3t3[0]- enemy1x))**2) + ((math.fabs(cf3t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf3t3),5)
                en1hp -= t3b3d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy2x))**2) + ((math.fabs(cf3t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf3t3),5)
                en2hp -= t3b3d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy3x))**2) + ((math.fabs(cf3t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf3t3),5)
                en3hp -= t3b3d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy4x))**2) + ((math.fabs(cf3t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf3t3),5)
                en4hp -= t3b3d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy5x))**2) + ((math.fabs(cf3t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf3t3),5)
                en5hp -= t3b3d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy6x))**2) + ((math.fabs(cf3t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf3t3),5)
                en6hp -= t3b3d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy7x))**2) + ((math.fabs(cf3t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf3t3),5)
                en7hp -= t3b3d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy8x))**2) + ((math.fabs(cf3t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf3t3),5)
                en8hp -= t3b3d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy9x))**2) + ((math.fabs(cf3t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf3t3),5)
                en9hp -= t3b3d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf3t3[0]- enemy0x))**2) + ((math.fabs(cf3t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf3t3),5)
                en0hp -= t3b3d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon3 == 1:
            if math.sqrt(((math.fabs(cf3tp[0]- enemy1x))**2) + ((math.fabs(cf3tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en1hp -= tpb3d

            if math.sqrt(((math.fabs(cf3tp[0]- enemy2x))**2) + ((math.fabs(cf3tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en2hp -= tpb3d
                
            if math.sqrt(((math.fabs(cf3tp[0]- enemy3x))**2) + ((math.fabs(cf3tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en3hp -= tpb3d

            if math.sqrt(((math.fabs(cf3tp[0]- enemy4x))**2) + ((math.fabs(cf3tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en4hp -= tpb3d
            if math.sqrt(((math.fabs(cf3tp[0]- enemy5x))**2) + ((math.fabs(cf3tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en5hp -= tpb3d
            if math.sqrt(((math.fabs(cf3tp[0]- enemy6x))**2) + ((math.fabs(cf3tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en6hp -= tpb3d
            if math.sqrt(((math.fabs(cf3tp[0]- enemy7x))**2) + ((math.fabs(cf3tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en7hp -= tpb3d
            if math.sqrt(((math.fabs(cf3tp[0]- enemy8x))**2) + ((math.fabs(cf3tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en8hp -= tpb3d
            if math.sqrt(((math.fabs(cf3tp[0]- enemy9x))**2) + ((math.fabs(cf3tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en9hp -= tpb3d
            if math.sqrt(((math.fabs(cf3tp[0]- enemy0x))**2) + ((math.fabs(cf3tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf3tp[0],cf3tp[1]]),5)
                tp += 1
                en0hp -= tpb3d
            tp -= 1
        ### box 4 ###
        ### tower2 shooting ###
        if t2on4 == 1:
            if math.sqrt(((math.fabs(cf4t2[0]- enemy1x))**2) + ((math.fabs(cf4t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf4t2),5)
                t2 += 1
                en1hp -= t2b4d

            if math.sqrt(((math.fabs(cf4t2[0]- enemy2x))**2) + ((math.fabs(cf4t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf4t2),5)
                t2 += 1
                en2hp -= t2b4d
                
            if math.sqrt(((math.fabs(cf4t2[0]- enemy3x))**2) + ((math.fabs(cf4t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf4t2),5)
                t2 += 1
                en3hp -= t2b4d

            if math.sqrt(((math.fabs(cf4t2[0]- enemy4x))**2) + ((math.fabs(cf4t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf4t2),5)
                t2 += 1
                en4hp -= t2b4d
            if math.sqrt(((math.fabs(cf4t2[0]- enemy5x))**2) + ((math.fabs(cf4t2[1] - enemy4y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf4t2),5)
                t2 += 1
                en5hp -= t2b4d
            if math.sqrt(((math.fabs(cf4t2[0]- enemy6x))**2) + ((math.fabs(cf4t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf4t2),5)
                t2 += 1
                en6hp -= t2b4d
            if math.sqrt(((math.fabs(cf4t2[0]- enemy7x))**2) + ((math.fabs(cf4t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf4t2),5)
                t2 += 1
                en7hp -= t2b4d
            if math.sqrt(((math.fabs(cf4t2[0]- enemy8x))**2) + ((math.fabs(cf4t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf4t2),5)
                t2 += 1
                en8hp -= t2b4d
            if math.sqrt(((math.fabs(cf4t2[0]- enemy9x))**2) + ((math.fabs(cf4t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf4t2),5)
                t2 += 1
                en9hp -= t2b4d
            if math.sqrt(((math.fabs(cf4t2[0]- enemy0x))**2) + ((math.fabs(cf4t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf4t2),5)
                t2 += 1
                en0hp -= t2b4d
            t2 -= 1
        ### tower3 shooting ###
        if t3on4 == 1:
            if math.sqrt(((math.fabs(cf4t3[0]- enemy1x))**2) + ((math.fabs(cf4t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf4t3),5)
                en1hp -= t3b4d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy2x))**2) + ((math.fabs(cf4t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf4t3),5)
                en2hp -= t3b4d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy3x))**2) + ((math.fabs(cf4t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf4t3),5)
                en3hp -= t3b4d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy4x))**2) + ((math.fabs(cf4t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf4t3),5)
                en4hp -= t3b4d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy5x))**2) + ((math.fabs(cf4t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf4t3),5)
                en5hp -= t3b4d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy6x))**2) + ((math.fabs(cf4t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf4t3),5)
                en6hp -= t3b4d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy7x))**2) + ((math.fabs(cf4t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf4t3),5)
                en7hp -= t3b4d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy8x))**2) + ((math.fabs(cf4t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf4t3),5)
                en8hp -= t3b4d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy9x))**2) + ((math.fabs(cf4t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf4t3),5)
                en9hp -= t3b4d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf4t3[0]- enemy0x))**2) + ((math.fabs(cf4t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf4t3),5)
                en0hp -= t3b4d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon4 == 1:
            if math.sqrt(((math.fabs(cf4tp[0]- enemy1x))**2) + ((math.fabs(cf4tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en1hp -= tpb4d

            if math.sqrt(((math.fabs(cf4tp[0]- enemy2x))**2) + ((math.fabs(cf4tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en2hp -= tpb4d
                
            if math.sqrt(((math.fabs(cf4tp[0]- enemy3x))**2) + ((math.fabs(cf4tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en3hp -= tpb4d

            if math.sqrt(((math.fabs(cf4tp[0]- enemy4x))**2) + ((math.fabs(cf4tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en4hp -= tpb4d
            if math.sqrt(((math.fabs(cf4tp[0]- enemy5x))**2) + ((math.fabs(cf4tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en5hp -= tpb4d
            if math.sqrt(((math.fabs(cf4tp[0]- enemy6x))**2) + ((math.fabs(cf4tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en6hp -= tpb4d
            if math.sqrt(((math.fabs(cf4tp[0]- enemy7x))**2) + ((math.fabs(cf4tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en7hp -= tpb4d
            if math.sqrt(((math.fabs(cf4tp[0]- enemy8x))**2) + ((math.fabs(cf4tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en8hp -= tpb4d
            if math.sqrt(((math.fabs(cf4tp[0]- enemy9x))**2) + ((math.fabs(cf4tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en9hp -= tpb4d
            if math.sqrt(((math.fabs(cf4tp[0]- enemy0x))**2) + ((math.fabs(cf4tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf4tp[0],cf4tp[1]]),5)
                tp += 1
                en0hp -= tpb4d
            tp -= 1
        ### box 5 ###
        ### tower2 shooting ###
        if t2on5 == 1:
            if math.sqrt(((math.fabs(cf5t2[0]- enemy1x))**2) + ((math.fabs(cf5t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf5t2),5)
                t2 += 1
                en1hp -= t2b5d

            if math.sqrt(((math.fabs(cf5t2[0]- enemy2x))**2) + ((math.fabs(cf5t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf5t2),5)
                t2 += 1
                en2hp -= t2b5d
                
            if math.sqrt(((math.fabs(cf5t2[0]- enemy3x))**2) + ((math.fabs(cf5t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf2t2),5)
                t2 += 1
                en3hp -= t2b5d

            if math.sqrt(((math.fabs(cf5t2[0]- enemy4x))**2) + ((math.fabs(cf5t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf5t2),5)
                t2 += 1
                en4hp -= t2b5d
            if math.sqrt(((math.fabs(cf5t2[0]- enemy5x))**2) + ((math.fabs(cf5t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf5t2),5)
                t2 += 1
                en5hp -= t2b5d
            if math.sqrt(((math.fabs(cf5t2[0]- enemy6x))**2) + ((math.fabs(cf5t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf5t2),5)
                t2 += 1
                en6hp -= t2b5d
            if math.sqrt(((math.fabs(cf5t2[0]- enemy7x))**2) + ((math.fabs(cf5t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf5t2),5)
                t2 += 1
                en7hp -= t2b5d
            if math.sqrt(((math.fabs(cf5t2[0]- enemy8x))**2) + ((math.fabs(cf5t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf5t2),5)
                t2 += 1
                en8hp -= t2b5d
            if math.sqrt(((math.fabs(cf5t2[0]- enemy9x))**2) + ((math.fabs(cf5t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf5t2),5)
                t2 += 1
                en9hp -= t2b5d
            if math.sqrt(((math.fabs(cf5t2[0]- enemy0x))**2) + ((math.fabs(cf5t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf5t2),5)
                t2 += 1
                en0hp -= t2b5d
            t2 -= 1
        ### tower3 shooting ###
        if t3on5 == 1:
            if math.sqrt(((math.fabs(cf5t3[0]- enemy1x))**2) + ((math.fabs(cf5t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf5t3),5)
                en1hp -= t3b5d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy2x))**2) + ((math.fabs(cf5t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf5t3),5)
                en2hp -= t3b5d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy3x))**2) + ((math.fabs(cf5t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf5t3),5)
                en3hp -= t3b5d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy4x))**2) + ((math.fabs(cf5t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf5t3),5)
                en4hp -= t3b5d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy5x))**2) + ((math.fabs(cf5t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf5t3),5)
                en5hp -= t3b5d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy6x))**2) + ((math.fabs(cf5t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf5t3),5)
                en6hp -= t3b5d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy7x))**2) + ((math.fabs(cf5t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf5t3),5)
                en7hp -= t3b5d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy8x))**2) + ((math.fabs(cf5t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf5t3),5)
                en8hp -= t3b5d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy9x))**2) + ((math.fabs(cf5t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf5t3),5)
                en9hp -= t3b5d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf5t3[0]- enemy0x))**2) + ((math.fabs(cf5t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf5t3),5)
                en0hp -= t3b5d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon5 == 1:
            if math.sqrt(((math.fabs(cf5tp[0]- enemy1x))**2) + ((math.fabs(cf5tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en1hp -= tpb5d

            if math.sqrt(((math.fabs(cf5tp[0]- enemy2x))**2) + ((math.fabs(cf5tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en2hp -= tpb5d
                
            if math.sqrt(((math.fabs(cf5tp[0]- enemy3x))**2) + ((math.fabs(cf5tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en3hp -= tpb5d

            if math.sqrt(((math.fabs(cf5tp[0]- enemy4x))**2) + ((math.fabs(cf5tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en4hp -= tpb5d
            if math.sqrt(((math.fabs(cf5tp[0]- enemy5x))**2) + ((math.fabs(cf5tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en5hp -= tpb5d
            if math.sqrt(((math.fabs(cf5tp[0]- enemy6x))**2) + ((math.fabs(cf5tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en6hp -= tpb5d
            if math.sqrt(((math.fabs(cf5tp[0]- enemy0x))**2) + ((math.fabs(cf5tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en0hp -= tpb5d
            if math.sqrt(((math.fabs(cf5tp[0]- enemy7x))**2) + ((math.fabs(cf5tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en7hp -= tpb5d
            if math.sqrt(((math.fabs(cf5tp[0]- enemy8x))**2) + ((math.fabs(cf5tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en8hp -= tpb5d
            if math.sqrt(((math.fabs(cf5tp[0]- enemy9x))**2) + ((math.fabs(cf5tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf5tp[0],cf5tp[1]]),5)
                tp += 1
                en9hp -= tpb5d
            tp -= 1
        ### box 6 ###
        ### tower2 shooting ###
        if t2on6 == 1:
            if math.sqrt(((math.fabs(cf6t2[0]- enemy1x))**2) + ((math.fabs(cf6t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf6t2),5)
                t2 += 1
                en1hp -= t2b6d

            if math.sqrt(((math.fabs(cf6t2[0]- enemy2x))**2) + ((math.fabs(cf6t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf6t2),5)
                t2 += 1
                en2hp -= t2b6d
                
            if math.sqrt(((math.fabs(cf6t2[0]- enemy3x))**2) + ((math.fabs(cf6t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf6t2),5)
                t2 += 1
                en3hp -= t2b6d

            if math.sqrt(((math.fabs(cf6t2[0]- enemy4x))**2) + ((math.fabs(cf6t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf6t2),5)
                t2 += 1
                en4hp -= t2b6d
            if math.sqrt(((math.fabs(cf6t2[0]- enemy5x))**2) + ((math.fabs(cf6t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf6t2),5)
                t2 += 1
                en5hp -= t2b6d
            if math.sqrt(((math.fabs(cf6t2[0]- enemy6x))**2) + ((math.fabs(cf6t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf6t2),5)
                t2 += 1
                en6hp -= t2b6d
            if math.sqrt(((math.fabs(cf6t2[0]- enemy7x))**2) + ((math.fabs(cf6t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf6t2),5)
                t2 += 1
                en7hp -= t2b6d
            if math.sqrt(((math.fabs(cf6t2[0]- enemy8x))**2) + ((math.fabs(cf6t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf6t2),5)
                t2 += 1
                en8hp -= t2b6d
            if math.sqrt(((math.fabs(cf6t2[0]- enemy9x))**2) + ((math.fabs(cf6t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf6t2),5)
                t2 += 1
                en9hp -= t2b6d
            if math.sqrt(((math.fabs(cf6t2[0]- enemy0x))**2) + ((math.fabs(cf6t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf6t2),5)
                t2 += 1
                en0hp -= t2b6d
            t2 -= 1
        ### tower3 shooting ###
        if t3on6 == 1:
            if math.sqrt(((math.fabs(cf6t3[0]- enemy1x))**2) + ((math.fabs(cf6t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf6t3),5)
                en1hp -= t3b6d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy2x))**2) + ((math.fabs(cf6t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf6t3),5)
                en2hp -= t3b6d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy3x))**2) + ((math.fabs(cf6t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf6t3),5)
                en3hp -= t3b6d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy4x))**2) + ((math.fabs(cf6t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf6t3),5)
                en4hp -= t3b6d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy5x))**2) + ((math.fabs(cf6t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf6t3),5)
                en5hp -= t3b6d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy6x))**2) + ((math.fabs(cf6t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf6t3),5)
                en6hp -= t3b6d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy7x))**2) + ((math.fabs(cf6t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf6t3),5)
                en7hp -= t3b6d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy8x))**2) + ((math.fabs(cf6t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf6t3),5)
                en8hp -= t3b6d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy9x))**2) + ((math.fabs(cf6t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf6t3),5)
                en9hp -= t3b6d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf6t3[0]- enemy0x))**2) + ((math.fabs(cf6t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf6t3),5)
                en0hp -= t3b6d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon6 == 1:
            if math.sqrt(((math.fabs(cf6tp[0]- enemy1x))**2) + ((math.fabs(cf6tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en1hp -= tpb6d

            if math.sqrt(((math.fabs(cf6tp[0]- enemy2x))**2) + ((math.fabs(cf6tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en2hp -= tpb6d
                
            if math.sqrt(((math.fabs(cf6tp[0]- enemy3x))**2) + ((math.fabs(cf6tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en3hp -= tpb6d

            if math.sqrt(((math.fabs(cf6tp[0]- enemy4x))**2) + ((math.fabs(cf6tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en4hp -= tpb6d
            if math.sqrt(((math.fabs(cf6tp[0]- enemy5x))**2) + ((math.fabs(cf6tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en5hp -= tpb6d
            if math.sqrt(((math.fabs(cf6tp[0]- enemy6x))**2) + ((math.fabs(cf6tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en6hp -= tpb6d
            if math.sqrt(((math.fabs(cf6tp[0]- enemy7x))**2) + ((math.fabs(cf6tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en7hp -= tpb6d
            if math.sqrt(((math.fabs(cf6tp[0]- enemy8x))**2) + ((math.fabs(cf6tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en8hp -= tpb6d
            if math.sqrt(((math.fabs(cf6tp[0]- enemy9x))**2) + ((math.fabs(cf6tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en9hp -= tpb6d
            if math.sqrt(((math.fabs(cf6tp[0]- enemy0x))**2) + ((math.fabs(cf6tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf6tp[0],cf6tp[1]]),5)
                tp += 1
                en0hp -= tpb6d
            tp -= 1
        ### box 7 ###
        ### tower2 shooting ###
        if t2on7 == 1:
            if math.sqrt(((math.fabs(cf7t2[0]- enemy1x))**2) + ((math.fabs(cf7t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf7t2),5)
                t2 += 1
                en1hp -= t2b7d

            if math.sqrt(((math.fabs(cf7t2[0]- enemy2x))**2) + ((math.fabs(cf7t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf7t2),5)
                t2 += 1
                en2hp -= t2b7d
                
            if math.sqrt(((math.fabs(cf7t2[0]- enemy3x))**2) + ((math.fabs(cf7t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf7t2),5)
                t2 += 1
                en3hp -= t2b7d

            if math.sqrt(((math.fabs(cf7t2[0]- enemy4x))**2) + ((math.fabs(cf7t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf7t2),5)
                t2 += 1
                en4hp -= t2b7d
            if math.sqrt(((math.fabs(cf7t2[0]- enemy5x))**2) + ((math.fabs(cf7t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf7t2),5)
                t2 += 1
                en5hp -= t2b7d
            if math.sqrt(((math.fabs(cf7t2[0]- enemy6x))**2) + ((math.fabs(cf7t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf7t2),5)
                t2 += 1
                en6hp -= t2b7d
            if math.sqrt(((math.fabs(cf7t2[0]- enemy7x))**2) + ((math.fabs(cf7t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf7t2),5)
                t2 += 1
                en7hp -= t2b7d
            if math.sqrt(((math.fabs(cf7t2[0]- enemy8x))**2) + ((math.fabs(cf7t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf7t2),5)
                t2 += 1
                en8hp -= t2b7d
            if math.sqrt(((math.fabs(cf7t2[0]- enemy9x))**2) + ((math.fabs(cf7t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf7t2),5)
                t2 += 1
                en9hp -= t2b7d
            if math.sqrt(((math.fabs(cf7t2[0]- enemy0x))**2) + ((math.fabs(cf7t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf7t2),5)
                t2 += 1
                en0hp -= t2b7d
            t2 -= 1
        ### tower3 shooting ###
        if t3on7 == 1:
            if math.sqrt(((math.fabs(cf7t3[0]- enemy1x))**2) + ((math.fabs(cf7t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf7t3),5)
                en1hp -= t3b7d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy2x))**2) + ((math.fabs(cf7t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf7t3),5)
                en2hp -= t3b7d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy3x))**2) + ((math.fabs(cf7t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf7t3),5)
                en3hp -= t3b7d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy4x))**2) + ((math.fabs(cf7t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf7t3),5)
                en4hp -= t3b7d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy5x))**2) + ((math.fabs(cf7t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf7t3),5)
                en5hp -= t3b7d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy6x))**2) + ((math.fabs(cf7t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf7t3),5)
                en6hp -= t3b7d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy7x))**2) + ((math.fabs(cf7t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf7t3),5)
                en7hp -= t3b7d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy8x))**2) + ((math.fabs(cf7t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf7t3),5)
                en8hp -= t3b7d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy9x))**2) + ((math.fabs(cf7t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf7t3),5)
                en9hp -= t3b7d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf7t3[0]- enemy0x))**2) + ((math.fabs(cf7t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf7t3),5)
                en0hp -= t3b7d
                enemy0spd = 0.05
                en40slw = 1
        ### tower p shooting ###
        if tpon7 == 1:
            if math.sqrt(((math.fabs(cf7tp[0]- enemy1x))**2) + ((math.fabs(cf7tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en1hp -= tpb7d

            if math.sqrt(((math.fabs(cf7tp[0]- enemy2x))**2) + ((math.fabs(cf7tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en2hp -= tpb7d
                
            if math.sqrt(((math.fabs(cf7tp[0]- enemy3x))**2) + ((math.fabs(cf7tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en3hp -= tpb7d

            if math.sqrt(((math.fabs(cf7tp[0]- enemy4x))**2) + ((math.fabs(cf7tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en4hp -= tpb7d
            if math.sqrt(((math.fabs(cf7tp[0]- enemy5x))**2) + ((math.fabs(cf7tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en5hp -= tpb7d
            if math.sqrt(((math.fabs(cf7tp[0]- enemy6x))**2) + ((math.fabs(cf7tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en6hp -= tpb7d
            if math.sqrt(((math.fabs(cf7tp[0]- enemy7x))**2) + ((math.fabs(cf7tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en7hp -= tpb7d
            if math.sqrt(((math.fabs(cf7tp[0]- enemy8x))**2) + ((math.fabs(cf7tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en8hp -= tpb7d
            if math.sqrt(((math.fabs(cf7tp[0]- enemy9x))**2) + ((math.fabs(cf7tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en9hp -= tpb7d
            if math.sqrt(((math.fabs(cf7tp[0]- enemy0x))**2) + ((math.fabs(cf7tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf7tp[0],cf7tp[1]-30]),5)
                tp += 1
                en0hp -= tpb7d
            tp -= 1
        ### box 8 ###
        ### tower2 shooting ###
        if t2on8 == 1:
            if math.sqrt(((math.fabs(cf8t2[0]- enemy1x))**2) + ((math.fabs(cf8t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf8t2),5)
                t2 += 1
                en1hp -= t2b8d

            if math.sqrt(((math.fabs(cf8t2[0]- enemy2x))**2) + ((math.fabs(cf8t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf8t2),5)
                t2 += 1
                en2hp -= t2b8d
                
            if math.sqrt(((math.fabs(cf8t2[0]- enemy3x))**2) + ((math.fabs(cf8t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf8t2),5)
                t2 += 1
                en3hp -= t2b8d

            if math.sqrt(((math.fabs(cf8t2[0]- enemy4x))**2) + ((math.fabs(cf8t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf8t2),5)
                t2 += 1
                en4hp -= t2b8d
            if math.sqrt(((math.fabs(cf8t2[0]- enemy5x))**2) + ((math.fabs(cf8t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf8t2),5)
                t2 += 1
                en5hp -= t2b8d
            if math.sqrt(((math.fabs(cf8t2[0]- enemy6x))**2) + ((math.fabs(cf8t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf8t2),5)
                t2 += 1
                en6hp -= t2b8d
            if math.sqrt(((math.fabs(cf8t2[0]- enemy7x))**2) + ((math.fabs(cf8t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf8t2),5)
                t2 += 1
                en7hp -= t2b8d
            if math.sqrt(((math.fabs(cf8t2[0]- enemy8x))**2) + ((math.fabs(cf8t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf8t2),5)
                t2 += 1
                en8hp -= t2b8d
            if math.sqrt(((math.fabs(cf8t2[0]- enemy9x))**2) + ((math.fabs(cf8t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf8t2),5)
                t2 += 1
                en9hp -= t2b8d
            if math.sqrt(((math.fabs(cf8t2[0]- enemy0x))**2) + ((math.fabs(cf8t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf8t2),5)
                t2 += 1
                en0hp -= t2b8d
            t2 -= 1
        ### tower3 shooting ###
        if t3on8 == 1:
            if math.sqrt(((math.fabs(cf8t3[0]- enemy1x))**2) + ((math.fabs(cf8t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf8t3),5)
                en1hp -= t3b8d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy2x))**2) + ((math.fabs(cf8t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf8t3),5)
                en2hp -= t3b8d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy3x))**2) + ((math.fabs(cf8t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf8t3),5)
                en3hp -= t3b8d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy4x))**2) + ((math.fabs(cf8t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf8t3),5)
                en4hp -= t3b8d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy5x))**2) + ((math.fabs(cf8t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf8t3),5)
                en5hp -= t3b8d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy6x))**2) + ((math.fabs(cf8t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf8t3),5)
                en6hp -= t3b8d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy7x))**2) + ((math.fabs(cf8t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf8t3),5)
                en7hp -= t3b8d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy8x))**2) + ((math.fabs(cf8t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf8t3),5)
                en8hp -= t3b8d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy9x))**2) + ((math.fabs(cf8t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf8t3),5)
                en9hp -= t3b8d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf8t3[0]- enemy0x))**2) + ((math.fabs(cf8t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf8t3),5)
                en0hp -= t3b8d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon8 == 1:
            if math.sqrt(((math.fabs(cf8tp[0]- enemy1x))**2) + ((math.fabs(cf8tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en1hp -= tpb8d

            if math.sqrt(((math.fabs(cf8tp[0]- enemy2x))**2) + ((math.fabs(cf8tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en2hp -= tpb8d
                
            if math.sqrt(((math.fabs(cf8tp[0]- enemy3x))**2) + ((math.fabs(cf8tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en3hp -= tpb8d

            if math.sqrt(((math.fabs(cf8tp[0]- enemy4x))**2) + ((math.fabs(cf8tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en4hp -= tpb8d
            if math.sqrt(((math.fabs(cf8tp[0]- enemy5x))**2) + ((math.fabs(cf8tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en5hp -= tpb8d
            if math.sqrt(((math.fabs(cf8tp[0]- enemy6x))**2) + ((math.fabs(cf8tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en6hp -= tpb8d
            if math.sqrt(((math.fabs(cf8tp[0]- enemy7x))**2) + ((math.fabs(cf8tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en7hp -= tpb8d
            if math.sqrt(((math.fabs(cf8tp[0]- enemy8x))**2) + ((math.fabs(cf8tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en8hp -= tpb8d
            if math.sqrt(((math.fabs(cf8tp[0]- enemy9x))**2) + ((math.fabs(cf8tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en9hp -= tpb8d
            if math.sqrt(((math.fabs(cf8tp[0]- enemy0x))**2) + ((math.fabs(cf8tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf8tp[0],cf8tp[1]-30]),5)
                tp += 1
                en0hp -= tpb8d
            tp -= 1
        ### box 9 ###
        ### tower2 shooting ###
        if t2on9 == 1:
            if math.sqrt(((math.fabs(cf9t2[0]- enemy1x))**2) + ((math.fabs(cf9t2[1] - enemy1y))**2)) < 150 and en1hp >0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy1x+15,enemy1y+15],cf9t2),5)
                t2 += 1
                en1hp -= t2b9d

            if math.sqrt(((math.fabs(cf9t2[0]- enemy2x))**2) + ((math.fabs(cf9t2[1] - enemy2y))**2)) < 150 and en2hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy2x+15,enemy2y+15],cf9t2),5)
                t2 += 1
                en2hp -= t2b9d
                
            if math.sqrt(((math.fabs(cf9t2[0]- enemy3x))**2) + ((math.fabs(cf9t2[1] - enemy3y))**2)) < 150 and en3hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy3x+15,enemy3y+15],cf9t2),5)
                t2 += 1
                en3hp -= t2b9d

            if math.sqrt(((math.fabs(cf9t2[0]- enemy4x))**2) + ((math.fabs(cf9t2[1] - enemy4y))**2)) < 150 and en4hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy4x+15,enemy4y+15],cf9t2),5)
                t2 += 1
                en4hp -= t2b9d
            if math.sqrt(((math.fabs(cf9t2[0]- enemy5x))**2) + ((math.fabs(cf9t2[1] - enemy5y))**2)) < 150 and en5hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy5x+15,enemy5y+15],cf9t2),5)
                t2 += 1
                en5hp -= t2b9d
            if math.sqrt(((math.fabs(cf9t2[0]- enemy6x))**2) + ((math.fabs(cf9t2[1] - enemy6y))**2)) < 150 and en6hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy6x+15,enemy6y+15],cf9t2),5)
                t2 += 1
                en6hp -= t2b9d
            if math.sqrt(((math.fabs(cf9t2[0]- enemy7x))**2) + ((math.fabs(cf9t2[1] - enemy7y))**2)) < 150 and en7hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy7x+15,enemy7y+15],cf9t2),5)
                t2 += 1
                en7hp -= t2b9d
            if math.sqrt(((math.fabs(cf9t2[0]- enemy8x))**2) + ((math.fabs(cf9t2[1] - enemy8y))**2)) < 150 and en8hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy8x+15,enemy8y+15],cf9t2),5)
                t2 += 1
                en8hp -= t2b9d
            if math.sqrt(((math.fabs(cf9t2[0]- enemy9x))**2) + ((math.fabs(cf9t2[1] - enemy9y))**2)) < 150 and en9hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy9x+15,enemy9y+15],cf9t2),5)
                t2 += 1
                en9hp -= t2b9d
            if math.sqrt(((math.fabs(cf9t2[0]- enemy0x))**2) + ((math.fabs(cf9t2[1] - enemy0y))**2)) < 150 and en0hp > 0 and t2 < 2:
                pygame.draw.polygon(screen,(prpl),([enemy0x+15,enemy0y+15],cf9t2),5)
                t2 += 1
                en0hp -= t2b9d
            t2 -= 1
        ### tower3 shooting ###
        if t3on9 == 1:
            if math.sqrt(((math.fabs(cf9t3[0]- enemy1x))**2) + ((math.fabs(cf9t3[1] - enemy1y))**2)) < 150 and en1hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy1x+15,enemy1y+15],cf9t3),5)
                en1hp -= t3b9d
                enemy1spd = 0.05
                en1slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy2x))**2) + ((math.fabs(cf9t3[1] - enemy2y))**2)) < 150 and en2hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy2x+15,enemy2y+15],cf9t3),5)
                en2hp -= t3b9d
                enemy2spd = 0.05
                en2slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy3x))**2) + ((math.fabs(cf9t3[1] - enemy3y))**2)) < 150 and en3hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy3x+15,enemy3y+15],cf9t3),5)
                en3hp -= t3b9d
                enemy3spd = 0.05
                en3slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy4x))**2) + ((math.fabs(cf9t3[1] - enemy4y))**2)) < 150 and en4hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy4x+15,enemy4y+15],cf9t3),5)
                en4hp -= t3b9d
                enemy4spd = 0.05
                en4slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy5x))**2) + ((math.fabs(cf9t3[1] - enemy5y))**2)) < 150 and en5hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy5x+15,enemy5y+15],cf9t3),5)
                en5hp -= t3b9d
                enemy5spd = 0.05
                en5slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy6x))**2) + ((math.fabs(cf9t3[1] - enemy6y))**2)) < 150 and en6hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy6x+15,enemy6y+15],cf9t3),5)
                en6hp -= t3b9d
                enemy6spd = 0.05
                en6slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy7x))**2) + ((math.fabs(cf9t3[1] - enemy7y))**2)) < 150 and en7hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy7x+15,enemy7y+15],cf9t3),5)
                en7hp -= t3b9d
                enemy7spd = 0.05
                en7slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy8x))**2) + ((math.fabs(cf9t3[1] - enemy8y))**2)) < 150 and en8hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy8x+15,enemy8y+15],cf9t3),5)
                en8hp -= t3b9d
                enemy8spd = 0.05
                en8slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy9x))**2) + ((math.fabs(cf9t3[1] - enemy9y))**2)) < 150 and en9hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy9x+15,enemy9y+15],cf9t3),5)
                en9hp -= t3b9d
                enemy9spd = 0.05
                en9slw = 1
            if math.sqrt(((math.fabs(cf9t3[0]- enemy0x))**2) + ((math.fabs(cf9t3[1] - enemy0y))**2)) < 150 and en0hp > 0:
                pygame.draw.polygon(screen,(pink),([enemy0x+15,enemy0y+15],cf9t3),5)
                en0hp -= t3b9d
                enemy0spd = 0.05
                en0slw = 1
        ### tower p shooting ###
        if tpon9 == 1:
            if math.sqrt(((math.fabs(cf9tp[0]- enemy1x))**2) + ((math.fabs(cf9tp[1] - enemy1y))**2)) < 150 and en1hp >0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy1x+15,enemy1y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en1hp -= tpb9d

            if math.sqrt(((math.fabs(cf9tp[0]- enemy2x))**2) + ((math.fabs(cf9tp[1] - enemy2y))**2)) < 150 and en2hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy2x+15,enemy2y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en2hp -= tpb9d
                
            if math.sqrt(((math.fabs(cf9tp[0]- enemy3x))**2) + ((math.fabs(cf9tp[1] - enemy3y))**2)) < 150 and en3hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy3x+15,enemy3y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en3hp -= tpb9d

            if math.sqrt(((math.fabs(cf9tp[0]- enemy4x))**2) + ((math.fabs(cf9tp[1] - enemy4y))**2)) < 150 and en4hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy4x+15,enemy4y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en4hp -= tpb9d
            if math.sqrt(((math.fabs(cf9tp[0]- enemy5x))**2) + ((math.fabs(cf9tp[1] - enemy5y))**2)) < 150 and en5hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy5x+15,enemy5y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en5hp -= tpb9d
            if math.sqrt(((math.fabs(cf9tp[0]- enemy6x))**2) + ((math.fabs(cf9tp[1] - enemy6y))**2)) < 150 and en6hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy6x+15,enemy6y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en6hp -= tpb9d
            if math.sqrt(((math.fabs(cf9tp[0]- enemy7x))**2) + ((math.fabs(cf9tp[1] - enemy7y))**2)) < 150 and en7hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy7x+15,enemy7y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en7hp -= tpb9d
            if math.sqrt(((math.fabs(cf9tp[0]- enemy8x))**2) + ((math.fabs(cf9tp[1] - enemy8y))**2)) < 150 and en8hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy8x+15,enemy8y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en8hp -= tpb9d
            if math.sqrt(((math.fabs(cf9tp[0]- enemy9x))**2) + ((math.fabs(cf9tp[1] - enemy9y))**2)) < 150 and en9hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy9x+15,enemy9y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en9hp -= tpb9d
            if math.sqrt(((math.fabs(cf9tp[0]- enemy0x))**2) + ((math.fabs(cf9tp[1] - enemy0y))**2)) < 150 and en0hp > 0 and tp < 2:
                pygame.draw.polygon(screen,(wht),([enemy0x+15,enemy0y+15],[cf9tp[0],cf9tp[1]-30]),5)
                tp += 1
                en0hp -= tpb9d
            tp -= 1
        if en4slw != 1:
            enemy4spd = 0.2
        if en3slw != 1:   
            enemy3spd = 0.2
        if en2slw != 1:
            enemy2spd = 0.2
        if en1slw != 1:
            enemy1spd = 0.2
        if en5slw != 1:
            enemy5spd = 0.2
        if en6slw != 1:
            enemy6spd = 0.2
        if en7slw != 1:
            enemy7spd = 0.2
        if en8slw != 1:
            enemy8spd = 0.2
        if en9slw != 1:
            enemy9spd = 0.2
        if en0slw != 1:
            enemy0spd = 0.2
        
        ### respawn ###
        if en1hp <= 0:
            print '1'
            money += 1
            score += 1
            enemy1xmove = 0
            enemy1ymove = 0
            enemy1spd = 0.2
            enemy1x = 20
            enemy1y = 20
            en1hp = en1hps + 250
            en1hps = en1hp
        if en2hp <= 0:
            print '2'
            money += 1
            score +=1
            enemy2xmove = 0
            enemy2ymove = 0
            enemy2spd = 0.2
            enemy2x = 20
            enemy2y = 20
            en2hp = en2hps + 250
            en2hps = en2hp
        if en3hp <= 0:
            money += 1
            score+=1
            enemy3xmove = 0
            enemy3ymove = 0
            enemy3spd = 0.2
            enemy3x = 20
            enemy3y = 20
            en3hp = en3hps + 250
            en3hps = en3hp
        if en4hp <= 0:
            money += 1
            score+=1
            enemy4xmove = 0
            enemy4ymove = 0
            enemy4spd = 0.2
            enemy4x = 20
            enemy4y = 20
            en4hp = en4hps + 250
            en4hps = en4hp
        if en5hp <= 0:
            money += 1
            score+=1
            enemy5xmove = 0
            enemy5ymove = 0
            enemy5spd = 0.2
            enemy5x = 20
            enemy5y = 20
            en5hp = en5hps + 250
            en5hps = en5hp
        if en6hp <= 0:
            money += 1
            score+=1
            enemy6xmove = 0
            enemy6ymove = 0
            enemy6spd = 0.2
            enemy6x = 20
            enemy6y = 20
            en6hp = en6hps + 250
            en6hps = en6hp
        if en7hp <= 0:
            money += 1
            score+=1
            enemy7xmove = 0
            enemy7ymove = 0
            enemy7spd = 0.2
            enemy7x = 20
            enemy7y = 20
            en7hp = en7hps + 250
            en7hps = en7hp
        if en8hp <= 0:
            money += 1
            score+=1
            enemy8xmove = 0
            enemy8ymove = 0
            enemy8spd = 0.2
            enemy8x = 20
            enemy8y = 20
            en8hp = en4hps + 250
            en8hps = en4hp
        if en4hp <= 0:
            money += 1
            score+=1
            enemy4xmove = 0
            enemy4ymove = 0
            enemy4spd = 0.2
            enemy4x = 20
            enemy4y = 20
            en4hp = en4hps + 250
            en4hps = en4hp
        if en4hp <= 0:
            money += 1
            score+=1
            enemy4xmove = 0
            enemy4ymove = 0
            enemy4spd = 0.2
            enemy4x = 20
            enemy4y = 20
            en4hp = en4hps + 250
            en4hps = en4hp
        ### tower buttons ###
        mouse = pygame.mouse.get_pos()
        ### drawing t to mouse pos ###
        if zat2 == 1 and zat3 == 0 and zatp == 0:
            pygame.draw.polygon(screen, (cyn),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
            pygame.draw.circle(screen,(wht),(mouse[0],mouse[1]),150,2)
        if zat3 == 1 and zat2 == 0 and zatp == 0:
            pygame.draw.polygon(screen, (cyn),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
            pygame.draw.circle(screen,(wht),(mouse[0],mouse[1]),150,2)
        if zatp == 1 and zat2 == 0 and zat3 == 0:
            pygame.draw.circle(screen,(cyn),(mouse[0],mouse[1]),15,5)
            pygame.draw.circle(screen,(wht),(mouse[0],mouse[1]),150,2)
        
        ### t2 button click ###
        if mouse[0] < t2bx + 100 and mouse[0] > t2bx:
            if mouse[1] < t2by+40 and mouse[1] > t2by:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN and money >= 0:
                        zat2 = 1
        
        ### t3 button click ###
        if mouse[0] < t3bx + 100 and mouse[0] > t3bx:
            if mouse[1] < t3by+40 and mouse[1] > t3by:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN and money >= 0:
                        zat3 = 1
        ### tower p button click ###
        if mouse[0] < tpbx + 100 and mouse[0] > tpbx:
            if mouse[1] < tpby+40 and mouse[1] > tpby:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN and money >= 0:
                        zatp = 1
        ## escaping t select ###             
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    zat3 = 0
                    zat2 = 0
                    zatp = 0
                    t2b1 = 0
                    t3b1 = 0
                    tpb1 = 0
                    t2b2 = 0
                    t3b2 = 0
                    tpb2 = 0
                    t2b3 = 0
                    t3b3 = 0
                    tpb3 = 0
                    t2b4 = 0
                    t3b4 = 0
                    tpb4 = 0
                    t2b5 = 0
                    t3b5 = 0
                    tpb5 = 0
                    t2b6 = 0
                    t3b6 = 0
                    tpb6 = 0
                    t2b7 = 0
                    t3b7 = 0
                    tpb7 = 0
                    t2b8 = 0
                    t3b8 = 0
                    tpb8 = 0
                    t2b9 = 0
                    t3b9 = 0
                    tpb9 = 0
        ### box 1 ###
        ### building t2 ###
        if mouse[0] > bx1x and mouse[0] < bx1x +30:
            if mouse[1] > bx1y and mouse[1] < bx1y+30 and zat2 == 1 and t2on1 == 0 and money > 14  and t3on1 == 0 and tpon1 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on1 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx1x and mouse[0] < bx1x +30:
            if mouse[1] > bx1y and mouse[1] < bx1y+30 and zat3 == 1 and t3on1 == 0 and money > 14  and t2on1 == 0 and tpon1 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on1 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx1x and mouse[0] < bx1x +30:
            if mouse[1] > bx1y and mouse[1] < bx1y+30 and zatp == 1 and tpon1 == 0 and money > 14  and t2on1 == 0 and t3on1 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon1 = 1
                    money -= 15
        ### box 2 ###           
        ### building t2 ###
        if mouse[0] > bx2x and mouse[0] < bx2x +30:
            if mouse[1] > bx2y and mouse[1] < bx2y+30 and zat2 == 1 and t2on2 == 0 and money > 14  and t3on2 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on2 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx2x and mouse[0] < bx2x +30:
            if mouse[1] > bx2y and mouse[1] < bx2y+30 and zat3 == 1 and t3on2 == 0 and money > 14  and t2on2 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on2 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx2x and mouse[0] < bx2x +30:
            if mouse[1] > bx2y and mouse[1] < bx2y+30 and zatp == 1 and tpon2 == 0 and money > 14  and t2on2 == 0 and t3on2 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon2 = 1
                    money -= 15
        ### box 3 ###           
        ### building t2 ###
        if mouse[0] > bx3x and mouse[0] < bx3x +30:
            if mouse[1] > bx3y and mouse[1] < bx3y+30 and zat2 == 1 and t2on3 == 0 and money > 14  and t3on3 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on3 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx3x and mouse[0] < bx3x +30:
            if mouse[1] > bx3y and mouse[1] < bx3y+30 and zat3 == 1 and t3on3 == 0 and money > 14  and t2on3 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on3 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx3x and mouse[0] < bx3x +30:
            if mouse[1] > bx3y and mouse[1] < bx3y+30 and zatp == 1 and tpon3 == 0 and money > 14  and t2on3 == 0 and t3on3 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon3 = 1
                    money -= 15
        ### box 4 ###           
        ### building t2 ###
        if mouse[0] > bx4x and mouse[0] < bx4x +30:
            if mouse[1] > bx4y and mouse[1] < bx4y+30 and zat2 == 1 and t2on4 == 0 and money > 14  and t3on4 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on4 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx4x and mouse[0] < bx4x +30:
            if mouse[1] > bx4y and mouse[1] < bx4y+30 and zat3 == 1 and t3on4 == 0 and money > 14  and t2on4 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on4 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx4x and mouse[0] < bx4x +30:
            if mouse[1] > bx4y and mouse[1] < bx4y+30 and zatp == 1 and tpon4 == 0 and money > 14  and t2on4 == 0 and t3on4 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon4 = 1
                    money -= 15
        ### box 5 ###           
        ### building t2 ###
        if mouse[0] > bx5x and mouse[0] < bx5x +30:
            if mouse[1] > bx5y and mouse[1] < bx5y+30 and zat2 == 1 and t2on5 == 0 and money > 14  and t3on5 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on5 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx5x and mouse[0] < bx5x +30:
            if mouse[1] > bx5y and mouse[1] < bx5y+30 and zat3 == 1 and t3on5 == 0 and money > 14  and t2on5 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on5 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx5x and mouse[0] < bx5x +30:
            if mouse[1] > bx5y and mouse[1] < bx5y+30 and zatp == 1 and tpon5 == 0 and money > 14  and t2on5 == 0 and t3on5 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon5 = 1
                    money -= 15
        ### box 6 ###           
        ### building t2 ###
        if mouse[0] > bx6x and mouse[0] < bx6x +30:
            if mouse[1] > bx6y and mouse[1] < bx6y+30 and zat2 == 1 and t2on6 == 0 and money > 14  and t3on6 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on6 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx6x and mouse[0] < bx6x +30:
            if mouse[1] > bx6y and mouse[1] < bx6y+30 and zat3 == 1 and t3on6 == 0 and money > 14  and t2on6 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on6 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx6x and mouse[0] < bx6x +30:
            if mouse[1] > bx6y and mouse[1] < bx6y+30 and zatp == 1 and tpon6 == 0 and money > 14  and t2on6 == 0 and t3on6 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon6 = 1
                    money -= 15
        ### box 7 ###           
        ### building t2 ###
        if mouse[0] > bx7x and mouse[0] < bx7x +30:
            if mouse[1] > bx7y and mouse[1] < bx7y+30 and zat2 == 1 and t2on7 == 0 and money > 14  and t3on7 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on7 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx7x and mouse[0] < bx7x +30:
            if mouse[1] > bx7y and mouse[1] < bx7y+30 and zat3 == 1 and t3on7 == 0 and money > 14  and t2on7 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on7 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx7x and mouse[0] < bx7x +30:
            if mouse[1] > bx7y and mouse[1] < bx7y+30 and zatp == 1 and tpon7 == 0 and money > 14  and t2on7 == 0 and t3on7 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon7 = 1
                    money -= 15
        ### box 8 ###           
        ### building t2 ###
        if mouse[0] > bx8x and mouse[0] < bx8x +30:
            if mouse[1] > bx8y and mouse[1] < bx8y+30 and zat2 == 1 and t2on8 == 0 and money > 14  and t3on8 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on8 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx8x and mouse[0] < bx8x +30:
            if mouse[1] > bx8y and mouse[1] < bx8y+30 and zat3 == 1 and t3on8 == 0 and money > 14  and t2on8 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on8 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx8x and mouse[0] < bx8x +30:
            if mouse[1] > bx8y and mouse[1] < bx8y+30 and zatp == 1 and tpon8 == 0 and money > 14  and t2on8 == 0 and t3on8 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon8 = 1
                    money -= 15
        ### box 9 ###           
        ### building t2 ###
        if mouse[0] > bx9x and mouse[0] < bx9x +30:
            if mouse[1] > bx9y and mouse[1] < bx9y+30 and zat2 == 1 and t2on9 == 0 and money > 14  and t3on9 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]-15],[mouse[0]+15,mouse[1]-15],[mouse[0],mouse[1]+15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t2on9 = 1
                    money -= 15
        ### building t3 ###
        if mouse[0] > bx9x and mouse[0] < bx9x +30:
            if mouse[1] > bx9y and mouse[1] < bx9y+30 and zat3 == 1 and t3on9 == 0 and money > 14  and t2on9 == 0:
                pygame.draw.polygon(screen, (bl),([mouse[0]-15,mouse[1]+15],[mouse[0]+15,mouse[1]+15],[mouse[0],mouse[1]-15]),5)
                if event.type == MOUSEBUTTONDOWN:
                    t3on9 = 1
                    money -= 15
        ### building tp ###
        if mouse[0] > bx9x and mouse[0] < bx9x +30:
            if mouse[1] > bx9y and mouse[1] < bx9y+30 and zatp == 1 and tpon9 == 0 and money > 14  and t2on9 == 0 and t3on9 ==0:
                pygame.draw.circle(screen,(bl),(mouse[0],mouse[1]),15,5)
                if event.type == MOUSEBUTTONDOWN:
                    tpon9 = 1
                    money -= 15
            
        ### box 1 upgrading ###
        ### t2 ###
        if mouse[0] > bx1x and mouse[0] < bx1x +30:
           if mouse[1] > bx1y and mouse[1] < bx1y+30 and zat2 == 0 and t2on1 == 1 and t3on1 == 0 and t2b1 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b1 = 1
        ### t3 ###
        if mouse[0] > bx1x and mouse[0] < bx1x +30:
           if mouse[1] > bx1y and mouse[1] < bx1y+30 and zat3 == 0 and t3on1 == 1 and t2on1 == 0 and t3b1 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b1 = 1
        ### tp ###
        if mouse[0] > bx1x and mouse[0] < bx1x +30:
           if mouse[1] > bx1y and mouse[1] < bx1y+30 and zatp == 0 and tpon1 == 1 and t2on1 == 0 and tpb1 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb1 = 1
        ### box 2 upgrading ###
        ### t2 ###
        if mouse[0] > bx2x and mouse[0] < bx2x +30:
           if mouse[1] > bx2y and mouse[1] < bx2y+30 and zat2 == 0 and t2on2 == 1 and t3on2 == 0 and t2b2 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b2 = 1
        ### t3 ###
        if mouse[0] > bx2x and mouse[0] < bx2x +30:
           if mouse[1] > bx2y and mouse[1] < bx2y+30 and zat3 == 0 and t3on2 == 1 and t2on2 == 0 and t3b2 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b2 = 1
        ### tp ###
        if mouse[0] > bx2x and mouse[0] < bx2x +30:
           if mouse[1] > bx2y and mouse[1] < bx2y+30 and zatp == 0 and tpon2 == 1 and t3on2 == 0 and tpb2 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb2 = 1
        ### box 3 upgrading ###
        ### t2 ###
        if mouse[0] > bx3x and mouse[0] < bx3x +30:
           if mouse[1] > bx3y and mouse[1] < bx3y+30 and zat2 == 0 and t2on3 == 1 and t3on3 == 0 and t2b3 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b3 = 1
        ### t3 ###
        if mouse[0] > bx3x and mouse[0] < bx3x +30:
           if mouse[1] > bx3y and mouse[1] < bx3y+30 and zat3 == 0 and t3on3 == 1 and t2on3 == 0 and t3b3 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b3 = 1
        ### tp ###
        if mouse[0] > bx3x and mouse[0] < bx3x +30:
           if mouse[1] > bx3y and mouse[1] < bx3y+30 and zatp == 0 and tpon3 == 1 and t3on3 == 0 and tpb3 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb3 = 1
        ### box 4 upgrading ###
        ### t2 ###
        if mouse[0] > bx4x and mouse[0] < bx4x +30:
           if mouse[1] > bx4y and mouse[1] < bx4y+30 and zat2 == 0 and t2on4 == 1 and t3on4 == 0 and t2b4 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b4 = 1
        ### t3 ###
        if mouse[0] > bx4x and mouse[0] < bx4x +30:
           if mouse[1] > bx4y and mouse[1] < bx4y+30 and zat3 == 0 and t3on4 == 1 and t2on4 == 0 and t3b4 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b4 = 1
        ### tp ###
        if mouse[0] > bx4x and mouse[0] < bx4x +30:
           if mouse[1] > bx4y and mouse[1] < bx4y+30 and zatp == 0 and tpon4 == 1 and t3on4 == 0 and tpb4 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb4 = 1

        ### box 5 upgrading ###
        ### t2 ###
        if mouse[0] > bx5x and mouse[0] < bx5x +30:
           if mouse[1] > bx5y and mouse[1] < bx5y+30 and zat2 == 0 and t2on5 == 1 and t3on5 == 0 and t2b5 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b5 = 1
        ### t3 ###
        if mouse[0] > bx5x and mouse[0] < bx5x +30:
           if mouse[1] > bx5y and mouse[1] < bx5y+30 and zat3 == 0 and t3on5 == 1 and t2on5 == 0 and t3b5 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b5 = 1
        ### tp ###
        if mouse[0] > bx5x and mouse[0] < bx5x +30:
           if mouse[1] > bx5y and mouse[1] < bx5y+30 and zatp == 0 and tpon5 == 1 and t3on5 == 0 and tpb5 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb5 = 1
        ### box 6 upgrading ###
        ### t2 ###
        if mouse[0] > bx6x and mouse[0] < bx6x +30:
           if mouse[1] > bx6y and mouse[1] < bx6y+30 and zat2 == 0 and t2on6 == 1 and t3on6 == 0 and t2b6 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b6 = 1
        ### t3 ###
        if mouse[0] > bx6x and mouse[0] < bx6x +30:
           if mouse[1] > bx6y and mouse[1] < bx6y+30 and zat3 == 0 and t3on6 == 1 and t2on6 == 0 and t3b6 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b6 = 1
        ### tp ###
        if mouse[0] > bx6x and mouse[0] < bx6x +30:
           if mouse[1] > bx6y and mouse[1] < bx6y+30 and zatp == 0 and tpon6 == 1 and t3on6 == 0 and tpb6 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb6 = 1

        ### box 7 upgrading ###
        ### t2 ###
        if mouse[0] > bx7x and mouse[0] < bx7x +30:
           if mouse[1] > bx7y and mouse[1] < bx7y+30 and zat2 == 0 and t2on7 == 1 and t3on7 == 0 and t2b7 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b7 = 1
        ### t3 ###
        if mouse[0] > bx7x and mouse[0] < bx7x +30:
           if mouse[1] > bx7y and mouse[1] < bx7y+30 and zat3 == 0 and t3on7 == 1 and t2on7 == 0 and t3b7 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b7 = 1
        ### tp ###
        if mouse[0] > bx7x and mouse[0] < bx7x +30:
           if mouse[1] > bx7y and mouse[1] < bx7y+30 and zatp == 0 and tpon7 == 1 and t3on7 == 0 and tpb7 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb7 = 1

        ### box 8 upgrading ###
        ### t2 ###
        if mouse[0] > bx8x and mouse[0] < bx8x +30:
           if mouse[1] > bx8y and mouse[1] < bx8y+30 and zat2 == 0 and t2on8 == 1 and t3on8 == 0 and t2b8 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b8 = 1
        ### t3 ###
        if mouse[0] > bx8x and mouse[0] < bx8x +30:
           if mouse[1] > bx8y and mouse[1] < bx8y+30 and zat3 == 0 and t3on8 == 1 and t2on8 == 0 and t3b8 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b8 = 1
        ### tp ###
        if mouse[0] > bx8x and mouse[0] < bx8x +30:
           if mouse[1] > bx8y and mouse[1] < bx8y+30 and zatp == 0 and tpon8 == 1 and t3on8 == 0 and tpb8 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb8 = 1

        ### box 9 upgrading ###
        ### t2 ###
        if mouse[0] > bx9x and mouse[0] < bx9x +30:
           if mouse[1] > bx9y and mouse[1] < bx9y+30 and zat2 == 0 and t2on9 == 1 and t3on9 == 0 and t2b9 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t2b9 = 1
        ### t3 ###
        if mouse[0] > bx9x and mouse[0] < bx9x +30:
           if mouse[1] > bx9y and mouse[1] < bx9y+30 and zat3 == 0 and t3on9 == 1 and t2on9 == 0 and t3b9 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   t3b9 = 1
        ### tp ###
        if mouse[0] > bx9x and mouse[0] < bx9x +30:
           if mouse[1] > bx9y and mouse[1] < bx9y+30 and zatp == 0 and tpon9 == 1 and t3on9 == 0 and tpb9 == 0:
               if event.type == MOUSEBUTTONDOWN:
                   tpb9 = 1

        ### selling button ###
        if mouse[0] > sbx and mouse[0] < sbx +30:
           if mouse[1] > sby and mouse[1] < sby+30:
               if t2b1==1 and event.type == MOUSEBUTTONDOWN:
                   t2on1 = 0
                   t2b1 = 0
                   money += 3
               if t3b1==1 and event.type == MOUSEBUTTONDOWN:
                   t3on1 = 0
                   t3b1 = 0
                   money += 3
               if tpb1==1 and event.type == MOUSEBUTTONDOWN:
                   tpon1 = 0
                   tpb1 = 0
                   money += 10
               if t2b2==1 and event.type == MOUSEBUTTONDOWN:
                   t2on2 = 0
                   t2b2 = 0
                   money += 3
               if t3b2==1 and event.type == MOUSEBUTTONDOWN:
                   t3on2 = 0
                   t3b2 = 0
                   money += 3
               if tpb2==1 and event.type == MOUSEBUTTONDOWN:
                   tpon2 = 0
                   tpb2 = 0
                   money += 10 
               if t2b3==1 and event.type == MOUSEBUTTONDOWN:
                   t2on3 = 0
                   t2b3 = 0
                   money += 3
               if t3b3==1 and event.type == MOUSEBUTTONDOWN:
                   t3on3 = 0
                   t3b3 = 0
                   money += 3
               if tpb3==1 and event.type == MOUSEBUTTONDOWN:
                   tpon3 = 0
                   tpb3 = 0
                   money += 10 
               if t2b4==1 and event.type == MOUSEBUTTONDOWN:
                   t2on4 = 0
                   t2b4 = 0
                   money += 3
               if t3b4==1 and event.type == MOUSEBUTTONDOWN:
                   t3on4 = 0
                   t3b4 = 0
                   money += 3
               if tpb4==1 and event.type == MOUSEBUTTONDOWN:
                   tpon4 = 0
                   tpb4 = 0
                   money += 10 
               if t2b5==1 and event.type == MOUSEBUTTONDOWN:
                   t2on5 = 0
                   t2b5 = 0
                   money += 3
               if t3b5==1 and event.type == MOUSEBUTTONDOWN:
                   t3on5 = 0
                   t3b5 = 0
                   money += 3
               if tpb5==1 and event.type == MOUSEBUTTONDOWN:
                   tpon5 = 0
                   tpb5 = 0
                   money += 10 
               if t2b6==1 and event.type == MOUSEBUTTONDOWN:
                   t2on6 = 0
                   t2b6 = 0
                   money += 3
               if t3b6==1 and event.type == MOUSEBUTTONDOWN:
                   t3on6 = 0
                   t3b6 = 0
                   money += 3
               if tpb6==1 and event.type == MOUSEBUTTONDOWN:
                   tpon6 = 0
                   tpb6 = 0
                   money += 10 
               if t2b7==1 and event.type == MOUSEBUTTONDOWN:
                   t2on7 = 0
                   t2b7 = 0
                   money += 3
               if t3b7==1 and event.type == MOUSEBUTTONDOWN:
                   t3on7 = 0
                   t3b7 = 0
                   money += 3
               if tpb7==1 and event.type == MOUSEBUTTONDOWN:
                   tpon7 = 0
                   tpb7 = 0
                   money += 10 
               if t2b8==1 and event.type == MOUSEBUTTONDOWN:
                   t2on8 = 0
                   t2b8 = 0
                   money += 3
               if t3b8==1 and event.type == MOUSEBUTTONDOWN:
                   t3on8 = 0
                   t3b8 = 0
                   money += 3
               if tpb8==1 and event.type == MOUSEBUTTONDOWN:
                   tpon8 = 0
                   tpb8 = 0
                   money += 10 
               if t2b9==1 and event.type == MOUSEBUTTONDOWN:
                   t2on9 = 0
                   t2b9 = 0
                   money += 3
               if t3b9==1 and event.type == MOUSEBUTTONDOWN:
                   t3on9 = 0
                   t3b9 = 0
                   money += 3
               if tpb9==1 and event.type == MOUSEBUTTONDOWN:
                   tpon9 = 0
                   tpb9 = 0
                   money += 10 
        ### upgrading button ###
        if mouse[0] > ubx and mouse[0] < ubx +30:
           if mouse[1] > uby and mouse[1] < uby+30 and money>9:
               if t2b1==1 and event.type == MOUSEBUTTONDOWN:
                   t2b1d += 0.25
                   money -= 10
                   t2b1 = 0
               if t3b1==1 and event.type == MOUSEBUTTONDOWN:
                   t3b1d += 0.1
                   money -= 10
                   t3b1 = 0
               if t2b2==1 and event.type == MOUSEBUTTONDOWN:
                   t2b2d += 0.25
                   money -= 10
                   t2b2 = 0
               if t3b2==1 and event.type == MOUSEBUTTONDOWN:
                   t3b2d += 0.1
                   money -= 10
                   t3b2 = 0
               if t2b3==1 and event.type == MOUSEBUTTONDOWN:
                   t2b3d += 0.25
                   money -= 10
                   t2b3 = 0
               if t3b3==1 and event.type == MOUSEBUTTONDOWN:
                   t3b3d += 0.1
                   money -= 10
                   t3b3 = 0
               if t2b4==1 and event.type == MOUSEBUTTONDOWN:
                   t2b4d += 0.25
                   money -= 10
                   t2b4 = 0
               if t3b4==1 and event.type == MOUSEBUTTONDOWN:
                   t3b4d += 0.1
                   money -= 10
                   t3b4 = 0
               if t2b5==1 and event.type == MOUSEBUTTONDOWN:
                   t2b5d += 0.25
                   money -= 10
                   t2b5 = 0
               if t3b5==1 and event.type == MOUSEBUTTONDOWN:
                   t3b5d += 0.1
                   money -= 10
                   t3b5 = 0
               if t2b6==1 and event.type == MOUSEBUTTONDOWN:
                   t2b6d += 0.25
                   money -= 10
                   t2b6 = 0
               if t3b6==1 and event.type == MOUSEBUTTONDOWN:
                   t3b6d += 0.1
                   money -= 10
                   t3b6 = 0
               if t2b7==1 and event.type == MOUSEBUTTONDOWN:
                   t2b7d += 0.25
                   money -= 10
                   t2b7 = 0
               if t3b7==1 and event.type == MOUSEBUTTONDOWN:
                   t3b7d += 0.1
                   money -= 10
                   t3b7 = 0
               if t2b8==1 and event.type == MOUSEBUTTONDOWN:
                   t2b8d += 0.25
                   money -= 10
                   t2b8 = 0
               if t3b8==1 and event.type == MOUSEBUTTONDOWN:
                   t3b8d += 0.1
                   money -= 10
                   t3b8 = 0
               if t2b9==1 and event.type == MOUSEBUTTONDOWN:
                   t2b9d += 0.25
                   money -= 10
                   t2b9 = 0
               if t3b9==1 and event.type == MOUSEBUTTONDOWN:
                   t3b9d += 0.1
                   money -= 10
                   t3b9 = 0
                            
        ### closing window ###
        for event in pygame.event.get():
           if event.type == QUIT:
                pygame.quit()
                sys.exit()

#start()
#endgame()
map1()
