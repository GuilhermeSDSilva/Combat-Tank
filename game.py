from player import *
from config import *
from wall import *
from screen import *
from barrier import *
from bullet import *

import sys
import pygame

def game_loop():

    
        
    pygame.init()
    #desnhar tela( está dentro de screen)
    SCREEN = screen
    
    player = pygame.image.load("img/tank.png")
    player = pygame.transform.scale(player, (40, 40)) 
    frente = False
    tras = False
    direita = False
    esquerda = False
    player_x = 100
    player_y = 390
    marcador = 12
    bala_movimento = False
    bala_direcao = marcador
    W_C = Wall_Collision()
    B_C = Barrier_Collision()
    B = Bullet()
    bala = B._init_()
    
    bala_x = player_x
    bala_y = player_y

    while True:
        SCREEN.fill(SCREEN_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    frente = True
                if event.key == pygame.K_s:
                    tras = True
                if event.key == pygame.K_a:
                    if marcador == 1:
                        marcador +=11
                    else:
                        marcador -=1
                if event.key == pygame.K_d:
                    if marcador == 12:
                        marcador -=11
                    else:
                        marcador +=1
                if event.key == pygame.K_z:
                    bala_movimento = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    frente = False
                if event.key == pygame.K_s:
                    tras = False
                if event.key == pygame.K_a:
                    esquerda = False
                if event.key == pygame.K_d:
                    direita = False
        if marcador == 12:
            p = pygame.image.load("img/tank.png")
            player = pygame.transform.scale(p, (40, 40))
        elif marcador == 1:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, -30)
        elif marcador == 2:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, -60)
        elif marcador == 3:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, -90)
        elif marcador == 4:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, -120)
        elif marcador == 5:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, -150)
        elif marcador == 6:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, -180)
        elif marcador == 7:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, 150)
        elif marcador == 8:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, 120)
        elif marcador == 9:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, 90)
        elif marcador == 10:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, 60)
        elif marcador ==11:
            p = pygame.image.load("img/tank.png")
            p = pygame.transform.scale(p, (40, 40))
            player = pygame.transform.rotate(p, 30)
            
        #desenhar paredes (está dentro de wall)      
        draw_wall(SCREEN)
        SCREEN.blit(player, (player_x, player_y))
        SCREEN.blit(bala, (bala_x, bala_y))
        SCREEN.blit(barreira1, (120, 330))
        SCREEN.blit(barreira2, (290, 350))
        SCREEN.blit(barreira3, (450, 200))
        SCREEN.blit(barreira4, (450, 500))
        SCREEN.blit(barreira5, (600, 350))
        SCREEN.blit(barreira6, (710, 330))

        if frente == True:
            if marcador == 3:
                player_x +=1
            elif marcador == 4:
                player_x +=1
                player_y +=0.5
            elif marcador == 5:
                player_x +=0.5
                player_y +=1
            elif marcador == 6:
                player_y += 1
            elif marcador == 7:
                player_x -=0.5
                player_y +=1
            elif marcador == 8:
                player_x -=1
                player_y +=0.5
            elif marcador == 9:
                player_x -=1
            elif marcador == 10:
                player_x -=1
                player_y -=0.5
            elif marcador == 11:
                player_x -=0.5
                player_y -=1
            elif marcador == 12:
                player_y -= 1
            elif marcador == 1:
                player_x +=0.5
                player_y -=1
            elif marcador == 2:
                player_x +=1
                player_y -=0.5

        #chamando a colisão com as paredes
        player_x = W_C.d_e(player_x)
        player_y = W_C.c_b(player_y)
        
        #chamando as colisões com as barreiras
        player_x = B_C.direita_esquerda(player_x,player_y)
        player_y = B_C.cima_baixo(player_x,player_y)

        if bala_movimento == True:
            bala_direcao = bala_direcao
            bala_x = B.moviment_x(bala_x, bala_movimento,bala_direcao)
            bala_y = B.moviment_y(bala_y, bala_movimento,bala_direcao)

        elif bala_movimento == False:
            bala_direcao = marcador
            bala_x = B.position_stopx(marcador, player_x, player_y)
            bala_y = B.position_stopy(marcador, player_x, player_y)

        if (bala_y <=100) and (bala_movimento == True):
            bala_movimento = False
            
        pygame.display.flip()
    pygame.quit()
