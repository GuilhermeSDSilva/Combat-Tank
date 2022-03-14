import pygame

class Personagem2:
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

