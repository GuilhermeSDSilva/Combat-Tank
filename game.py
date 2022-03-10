from config import *
from wall import *
import sys
import pygame
pygame.init()
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
while True:
    SCREEN.fill(SCREEN_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
    wall(SCREEN)
    
    pygame.display.flip()
pygame.quit()

