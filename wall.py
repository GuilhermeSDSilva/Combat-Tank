import pygame
from config import *
def draw_wall(screen):
    wall_up = pygame.draw.rect(screen, WALL_COLOR, (WALL_UP_POSITION,WALL_UP_SIZE))
    wall_down = pygame.draw.rect(screen, WALL_COLOR, (WALL_DOWN_POSITION,WALL_UP_SIZE))
    wall_right = pygame.draw.rect(screen, WALL_COLOR, (WALL_RIGHT_POSITION,WALL_RIGHT_SIZE))
    wall_left = pygame.draw.rect(screen, WALL_COLOR, (WALL_LEFT_POSITION,WALL_RIGHT_SIZE))
    
