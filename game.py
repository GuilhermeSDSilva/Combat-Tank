from player import *
from config import *
from wall import *
from screen import *
from barrier import *
from bullet import *
from player2 import *
import sys
import pygame

def game_loop():

    
        
    pygame.init()
    #desnhar tela( está dentro de screen)
    SCREEN = screen
    
    player = pygame.image.load("img/tank(1).png")
    player = pygame.transform.scale(player, (40, 40))
    player2 = pygame.image.load("img/tank(2).png")
    player2 = pygame.transform.scale(player2, (40, 40))
    frente = False
    tras = False
    direita = False
    esquerda = False
    frente2 = False
    tras2 = False
    direita2 = False
    esquerda2 = False
    player_x = 100
    player_y = 390
    player2_x = 930
    player2_y = 390
    marcador = 12
    marcador2 = 12
    bala_movimento = False
    bala2_movimento = False
    bala_direcao = marcador
    bala2_direcao = marcador2
    W_C = Wall_Collision()
    B_C = Barrier_Collision()
    B = Bullet()
    bala = B._init_()
    bala2 = B.bala2()
    P = Personagem()
    P2 = Personagem2()
    bala_x = player_x
    bala_y = player_y
    bala2_x = player2_x
    bala2_y = player2_y

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
                    
                if event.key == pygame.K_UP:
                    frente2 = True
                if event.key == pygame.K_DOWN:
                    tras2 = True
                if event.key == pygame.K_LEFT:
                    if marcador2 == 1:
                        marcador2 +=11
                    else:
                        marcador2 -=1
                if event.key == pygame.K_RIGHT:
                    if marcador2 == 12:
                        marcador2 -=11
                    else:
                        marcador2 +=1
                if event.key == pygame.K_SPACE:
                    bala2_movimento = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    frente = False
                if event.key == pygame.K_s:
                    tras = False
                if event.key == pygame.K_a:
                    esquerda = False
                if event.key == pygame.K_d:
                    direita = False
                if event.key == pygame.K_UP:
                    frente2 = False
                if event.key == pygame.K_DOWN:
                    tras2 = False
                if event.key == pygame.K_LEFT:
                    esquerda2 = False
                if event.key == pygame.K_RIGHT:
                    direita = False
                    
        player = P.sprites(marcador)
        player2 = P2.sprites2(marcador2)

        
        #desenhar paredes (está dentro de wall)      
        draw_wall(SCREEN)
        SCREEN.blit(player, (player_x, player_y))
        SCREEN.blit(bala, (bala_x, bala_y))
        SCREEN.blit(player2, (player2_x, player2_y))
        SCREEN.blit(bala2, (bala2_x, bala2_y))
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
                
        #PLAYER 2 MOVIMENTO
        if frente2 == True:
            if marcador2 == 3:
                player2_x +=1
            elif marcador2 == 4:
                player2_x +=1
                player2_y +=0.5
            elif marcador2 == 5:
                player2_x +=0.5
                player2_y +=1
            elif marcador2 == 6:
                player2_y += 1
            elif marcador2 == 7:
                player2_x -=0.5
                player2_y +=1
            elif marcador2 == 8:
                player2_x -=1
                player2_y +=0.5
            elif marcador2 == 9:
                player2_x -=1
            elif marcador2 == 10:
                player2_x -=1
                player2_y -=0.5
            elif marcador2 == 11:
                player2_x -=0.5
                player2_y -=1
            elif marcador2 == 12:
                player2_y -= 1
            elif marcador2 == 1:
                player2_x +=0.5
                player2_y -=1
            elif marcador2 == 2:
                player2_x +=1
                player2_y -=0.5

        #chamando a colisão com as paredes
        player_x = W_C.d_e(player_x)
        player_y = W_C.c_b(player_y)

        #chamando a colisão com as paredes P2
        player2_x = W_C.d_e(player2_x)
        player2_y = W_C.c_b(player2_y)
        
        #chamando as colisões com as barreiras
        player_x = B_C.direita_esquerda(player_x,player_y)
        player_y = B_C.cima_baixo(player_x,player_y)
        
        #chamando as colisões com as barreiras P2
        player2_x = B_C.direita_esquerda(player2_x,player2_y)
        player2_y = B_C.cima_baixo(player2_x,player2_y)

        #movimentos da bala 
        if bala_movimento == True:
            bala_direcao = bala_direcao
            bala_x = B.moviment_x(bala_x, bala_movimento,bala_direcao)
            bala_y = B.moviment_y(bala_y, bala_movimento,bala_direcao)
        elif bala_movimento == False:
            bala_direcao = marcador
            bala_x = B.position_stopx(marcador, player_x, player_y)
            bala_y = B.position_stopy(marcador, player_x, player_y)

        #movimentos da bala 2    
        if bala2_movimento == True:
            bala2_direcao = bala2_direcao
            bala2_x = B.moviment_x(bala2_x, bala2_movimento,bala2_direcao)
            bala2_y = B.moviment_y(bala2_y, bala2_movimento,bala2_direcao)
        elif bala_movimento == False:
            bala2_direcao = marcador2
            bala2_x = B.position_stopx(marcador2, player2_x, player2_y)
            bala2_y = B.position_stopy(marcador2, player2_x, player2_y)
            
        # colisões da bala P1
        if bala_movimento == True:    
            # parar a bala quando bater nas paredes
            if ((bala_y <=100) or (bala_y >= 700) or (bala_x <= 0) or (bala_x >=1000)) and (bala_movimento == True):
                bala_movimento = False
            # parar a bala quando bater nas barreiras 
            bala_movimento = B.colisao_barreira_direita_esquerda(bala_x,bala_y, bala_movimento)
            bala_movimento = B.colisao_barreira_cima_baixo(bala_x,bala_y, bala_movimento)
            # se a bala do player 1 atinge o player 2
            if (player2_x -10 <=  bala_x < player2_x + 40 ) and (player2_y - 5 <= bala_y <= player2_y + 35 ):
                player2_x = 930
                player2_y = 390

            
        # colisões da bala P2
        if bala2_movimento == True:    
            # parar a bala quando bater nas paredes
            if ((bala2_y <=100) or (bala2_y >= 700) or (bala2_x <= 0) or (bala2_x >=1000)) and (bala2_movimento == True):
                bala2_movimento = False
            # parar a bala quando bater nas barreiras 
            bala2_movimento = B.colisao_barreira_direita_esquerda(bala2_x,bala2_y, bala2_movimento)
            bala2_movimento = B.colisao_barreira_cima_baixo(bala2_x,bala2_y, bala2_movimento)
            # se a bala do player 2 atinge o player 1
            if (player_x -10 <=  bala2_x < player_x + 40 ) and (player_y - 3 <= bala2_y <= player_y + 35 ):
                player_x = 100
                player_y = 390
            
        pygame.display.flip()
    pygame.quit()
