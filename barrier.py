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
        elif (720 <= pos_x <=723) and (298 <= pos_y <= 480):
            self.ant_x = pos_x -1
            return self.ant_x
        elif (770 <= pos_x <=773) and (298 <= pos_y <= 480):
            self.ant_x = pos_x +1
            return self.ant_x
        else:
            self.ant_x = pos_x
            return self.ant_x

    def cima_baixo(self, pos_x,pos_y):
        #barreira 1
        if (155 <= pos_x <=228) and (298 <= pos_y <= 301):
            self.ant_y = pos_y -1
            return self.ant_y
        elif (155 <= pos_x <=228) and (477 <= pos_y <= 480):
            self.ant_y = pos_y +1
            return self.ant_y
        #barreira 2
        elif (254 <= pos_x <=369) and (355 <= pos_y <= 358):
            self.ant_y = pos_y -1
            return self.ant_y
        elif (254 <= pos_x <=369) and (420 <= pos_y <= 423):
            self.ant_y = pos_y +1
            return self.ant_y
        #barreira 3
        elif (414 <= pos_x <=528) and (205 <= pos_y <= 208):
            self.ant_y = pos_y -1
            return self.ant_y
        elif (414 <= pos_x <=528) and (270 <= pos_y <= 273):
            self.ant_y = pos_y +1
            return self.ant_y
        #barreira 4
        elif (414 <= pos_x <=528) and (500 <= pos_y <= 503):
            self.ant_y = pos_y -1
            return self.ant_y
        elif (414 <= pos_x <=528) and (570 <= pos_y <= 573):
            self.ant_y = pos_y +1
            return self.ant_y
        # barreira 5
        elif (564 <= pos_x <=679) and (350 <= pos_y <= 353):
            self.ant_y = pos_y -1
            return self.ant_y
        elif (564 <= pos_x <=679) and (420 <= pos_y <= 423):
            self.ant_y = pos_y +1
            return self.ant_y
        # barreira 6
        elif (709 <= pos_x <=782) and (298 <= pos_y <= 301):
            self.ant_y = pos_y -1
            return self.ant_y
        elif (709 <= pos_x <=782) and (477 <= pos_y <= 480):
            self.ant_y = pos_y +1
            return self.ant_y
        else:
            self.ant_y = pos_y
            return self.ant_y
        
