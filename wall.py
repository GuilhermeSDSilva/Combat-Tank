import pygame
from config import *

def draw_wall(screen):
    wall_up = pygame.draw.rect(screen, WALL_COLOR, (WALL_UP_POSITION,WALL_UP_SIZE))
    wall_down = pygame.draw.rect(screen, WALL_COLOR, (WALL_DOWN_POSITION,WALL_UP_SIZE))
    wall_right = pygame.draw.rect(screen, WALL_COLOR, (WALL_RIGHT_POSITION,WALL_RIGHT_SIZE))
    wall_left = pygame.draw.rect(screen, WALL_COLOR, (WALL_LEFT_POSITION,WALL_RIGHT_SIZE))
      
       
class Wall_Collision:
    def d_e(self,pos_x):
        #se o player for muito para a esquerda
        if pos_x <=13:
            self.ant_x = pos_x +1
            return self.ant_x
        #se o player for muito para a direita
        elif pos_x >= 950:
            self.ant_x = pos_x -1
            return self.ant_x
        else:
            self.ant_x = pos_x
            return self.ant_x
        
    def c_b(self,pos_y):
        #se o player for muito para cima
        if pos_y <=113:
            self.ant_y = pos_y +1
            return self.ant_y
        # se o player for muito para baixo
        elif pos_y >= 650:
            self.ant_y = pos_y -1
            return self.ant_y
        else:
            self.ant_y = pos_y
            return self.ant_y 
