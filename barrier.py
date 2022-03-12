import pygame
from config import *


barreira1 = pygame.image.load("img/barreira(1).png")
barreira1  = pygame.transform.scale(barreira1, BARR1_SIZE)

barreira2 = pygame.image.load("img/barreira(3).png")
barreira2  = pygame.transform.scale(barreira2, BARR3_SIZE)

barreira3 = pygame.image.load("img/barreira(3).png")
barreira3  = pygame.transform.scale(barreira3, BARR3_SIZE) 

barreira4 = pygame.image.load("img/barreira(3).png")
barreira4  = pygame.transform.scale(barreira4, BARR3_SIZE)

barreira5 = pygame.image.load("img/barreira(3).png")
barreira5  = pygame.transform.scale(barreira5, BARR3_SIZE)

barreira6 = pygame.image.load("img/barreira(1).png")
barreira6 = pygame.transform.rotate(barreira6, 180)
barreira6  = pygame.transform.scale(barreira6, BARR1_SIZE)

