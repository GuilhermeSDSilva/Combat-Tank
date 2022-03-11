from config import *
from wall import *
from screen import *
from player import *
import sys
import pygame


def game_loop():
    pygame.init()
    #desnhar tela( está dentro de screen)
    SCREEN = screen
    
    while True:
        SCREEN.fill(SCREEN_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                
        #desenhar paredes (está dentro de wall)      
        draw_wall(SCREEN)
        
        SCREEN.blit(personagem, (350, 350))
        
        pygame.display.flip()
    pygame.quit()
