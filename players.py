import pygame

class Personagens:
    def sprites(self, m):
        if m == 12:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            return self.p
        elif m == 1:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -30)
            return self.p
        elif m == 2:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -60)
            return self.p
        elif m == 3:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -90)
            return self.p
        elif m == 4:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -120)
            return self.p
        elif m == 5:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -150)
            return self.p
        elif m == 6:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -180)
            return self.p
        elif m == 7:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 150)
            return self.p
        elif m == 8:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 120)
            return self.p
        elif m == 9:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 90)
            return self.p
        elif m == 10:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 60)
            return self.p
        elif m ==11:
            self.p = pygame.image.load("img/tank(1).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 30)
            return self.p

    def movimentox_frente(self,posx,marc):
        if marc == 3:
            self.posi_x = posx + 1
            return self.posi_x
        elif marc == 4:
            self.posi_x = posx + 1
            return self.posi_x
        elif marc == 5:
            self.posi_x = posx + 0.5
            return self.posi_x
        elif marc == 6:
            self.posi_x = posx
            return self.posi_x
        elif marc == 7:
            self.posi_x = posx - 0.5
            return self.posi_x
        elif marc == 8:
            self.posi_x = posx - 1
            return self.posi_x
        elif marc == 9:
            self.posi_x = posx - 1
            return self.posi_x
        elif marc == 10:
            self.posi_x = posx - 1
            return self.posi_x
        elif marc == 11:
            self.posi_x = posx - 0.5
            return self.posi_x
        elif marc == 12:
            self.posi_x = posx
            return self.posi_x
        elif marc == 1:
            self.posi_x = posx + 0.5
            return self.posi_x
        elif marc == 2:
            self.posi_x = posx + 1
            return self.posi_x                
    def movimentoy_frente(self,posy,marc):
        if marc == 3:
            self.posi_y = posy
            return self.posi_y
        elif marc == 4:
            self.posi_y = posy + 0.5
            return self.posi_y
        elif marc == 5:
            self.posi_y = posy + 1
            return self.posi_y
        elif marc == 6:
            self.posi_y = posy + 1
            return self.posi_y
        elif marc == 7:
            self.posi_y = posy + 1
            return self.posi_y
        elif marc == 8:
            self.posi_y = posy + 0.5
            return self.posi_y
        elif marc == 9:
            self.posi_y = posy
            return self.posi_y
        elif marc == 10:
            self.posi_y = posy - 0.5
            return self.posi_y
        elif marc == 11:
            self.posi_y = posy - 1
            return self.posi_y
        elif marc == 12:
            self.posi_y = posy - 1
            return self.posi_y
        elif marc == 1:
            self.posi_y = posy - 1
            return self.posi_y
        elif marc == 2:
            self.posi_y = posy - 0.5
            return self.posi_y
    def sprites2(self, m):
        if m == 12:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            return self.p
        elif m == 1:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -30)
            return self.p
        elif m == 2:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -60)
            return self.p
        elif m == 3:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -90)
            return self.p
        elif m == 4:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -120)
            return self.p
        elif m == 5:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -150)
            return self.p
        elif m == 6:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, -180)
            return self.p
        elif m == 7:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 150)
            return self.p
        elif m == 8:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 120)
            return self.p
        elif m == 9:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 90)
            return self.p
        elif m == 10:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 60)
            return self.p
        elif m ==11:
            self.p = pygame.image.load("img/tank(2).png")
            self.p = pygame.transform.scale(self.p, (40, 40))
            self.p = pygame.transform.rotate(self.p, 30)
            return self.p

        
    def movimentox_tras(self,posx,marc):
        if marc == 9:
            self.posi_x = posx + 1
            return self.posi_x
        elif marc == 10:
            self.posi_x = posx + 1
            return self.posi_x
        elif marc == 11:
            self.posi_x = posx + 0.5
            return self.posi_x
        elif marc == 12:
            self.posi_x = posx
            return self.posi_x
        elif marc == 1:
            self.posi_x = posx - 0.5
            return self.posi_x
        elif marc == 2:
            self.posi_x = posx - 1
            return self.posi_x
        elif marc == 3:
            self.posi_x = posx - 1
            return self.posi_x
        elif marc == 4:
            self.posi_x = posx - 1
            return self.posi_x
        elif marc == 5:
            self.posi_x = posx - 0.5
            return self.posi_x
        elif marc == 6:
            self.posi_x = posx
            return self.posi_x
        elif marc == 7:
            self.posi_x = posx + 0.5
            return self.posi_x
        elif marc == 8:
            self.posi_x = posx + 1
            return self.posi_x                
    def movimentoy_tras(self,posy,marc):
        if marc == 9:
            self.posi_y = posy
            return self.posi_y
        elif marc == 10:
            self.posi_y = posy + 0.5
            return self.posi_y
        elif marc == 11:
            self.posi_y = posy + 1
            return self.posi_y
        elif marc == 12:
            self.posi_y = posy + 1
            return self.posi_y
        elif marc == 1:
            self.posi_y = posy + 1
            return self.posi_y
        elif marc == 2:
            self.posi_y = posy + 0.5
            return self.posi_y
        elif marc == 3:
            self.posi_y = posy
            return self.posi_y
        elif marc == 4:
            self.posi_y = posy - 0.5
            return self.posi_y
        elif marc == 5:
            self.posi_y = posy - 1
            return self.posi_y
        elif marc == 6:
            self.posi_y = posy - 1
            return self.posi_y
        elif marc == 7:
            self.posi_y = posy - 1
            return self.posi_y
        elif marc == 8:
            self.posi_y = posy - 0.5
            return self.posi_y



