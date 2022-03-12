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

class Barrier_Collision:
    #todas as colisões pela esquerda
    def direita_esquerda(self, pos_x,pos_y):
        #barreira 1
        if (170 <= pos_x <=173) and (298 <= pos_y <= 480):
            self.ant_x = pos_x -1
            return self.ant_x
        elif (224 <= pos_x <=227) and (298 <= pos_y <= 480):
            self.ant_x = pos_x +1
            return self.ant_x
        #barreira 2
        elif (254 <= pos_x <=257) and (350 <= pos_y <= 420):
            self.ant_x = pos_x -1
            return self.ant_x
        elif (366 <= pos_x <=369) and (350 <= pos_y <= 420):
            self.ant_x = pos_x +1
            return self.ant_x
        #barreira 3
        elif (414 <= pos_x <=417) and (200 <= pos_y <= 270):
            self.ant_x = pos_x -1
            return self.ant_x
        elif (525 <= pos_x <=528) and (200 <= pos_y <= 270):
            self.ant_x = pos_x +1
            return self.ant_x
        #barreira 4
        elif (414 <= pos_x <=417) and (500 <= pos_y <= 570):
            self.ant_x = pos_x -1
            return self.ant_x
        elif (525 <= pos_x <=528) and (500 <= pos_y <= 570):
            self.ant_x = pos_x +1
            return self.ant_x
        # barreira 5
        elif (564 <= pos_x <=567) and (350 <= pos_y <= 420):
            self.ant_x = pos_x -1
            return self.ant_x
        elif (676 <= pos_x <=679) and (350 <= pos_y <= 420):
            self.ant_x = pos_x +1
            return self.ant_x
        #barreira 6
        elif (724 <= pos_x <=727) and (298 <= pos_y <= 480):
            self.ant_x = pos_x -1
            return self.ant_x
        elif (770 <= pos_x <=773) and (298 <= pos_y <= 480):
            self.ant_x = pos_x +1
            return self.ant_x
        else:
            self.ant_x = pos_x
            return self.ant_x
