import pygame
class Bullet:
        
        def _init_(self):
            self.bala = pygame.image.load("img/bala.png")
            self.bala = pygame.transform.scale(self.bala, (3, 3))
            return self.bala

        #definem a posicão da bala em movimento
        def moviment_y(self,ba_y,movi,marc):
                if marc == 12:
                        self.pos_y = ba_y - 3
                        return self.pos_y
                elif marc == 1:
                        self.pos_y = ba_y - 2
                        return self.pos_y
                elif marc == 2:
                        self.pos_y = ba_y - 1
                        return self.pos_y
                elif marc == 3:
                        self.pos_y = ba_y - 0
                        return self.pos_y
                elif marc == 4:
                        self.pos_y = ba_y +1
                        return self.pos_y
                elif marc == 5:
                        self.pos_y = ba_y +2
                        return self.pos_y
                elif marc == 6:
                        self.pos_y = ba_y +3
                        return self.pos_y
                elif marc == 7:
                        self.pos_y = ba_y +2
                        return self.pos_y
                elif marc == 8:
                        self.pos_y = ba_y +1
                        return self.pos_y
                elif marc == 9:
                        self.pos_y = ba_y +0
                        return self.pos_y
                elif marc == 10:
                        self.pos_y = ba_y -1
                        return self.pos_y
                elif marc == 11:
                        self.pos_y = ba_y -2
                        return self.pos_y
                else:
                        self.pos_y = ba_y
                        return self.pos_y
                    
        def moviment_x(self,ba_x,movi,marc):
                if marc == 12:
                        self.pos_x = ba_x + 0
                        return self.pos_x
                elif marc == 1:
                        self.pos_x = ba_x + 1
                        return self.pos_x
                elif marc == 2:
                        self.pos_x = ba_x + 2
                        return self.pos_x
                elif marc == 3:
                        self.pos_x = ba_x + 3
                        return self.pos_x
                elif marc == 4:
                        self.pos_x = ba_x + 2
                        return self.pos_x
                elif marc == 5:
                        self.pos_x = ba_x + 1
                        return self.pos_x
                elif marc == 6:
                        self.pos_x = ba_x + 0
                        return self.pos_x
                elif marc == 7:
                        self.pos_x = ba_x - 1
                        return self.pos_x
                elif marc == 8:
                        self.pos_x = ba_x - 2
                        return self.pos_x
                elif marc == 9:
                        self.pos_x = ba_x - 3
                        return self.pos_x
                elif marc == 10:
                        self.pos_x = ba_x - 2
                        return self.pos_x
                elif marc == 11:
                        self.pos_x = ba_x - 1
                        return self.pos_x
                else:
                        self.pos_x = play_x
                        return self.pos_x

        
        #definem a posicão da bala parada
        def position_stopx(self, marc, play_x, play_y):
                if marc == 12:
                        self.pos_x = play_x + 18
                        return self.pos_x
                elif marc == 1:
                        self.pos_x = play_x + 33
                        return self.pos_x

                elif marc == 2:
                        self.pos_x = play_x + 39
                        return self.pos_x
                elif marc == 3:
                        self.pos_x = play_x + 35
                        return self.pos_x
                elif marc == 4:
                        self.pos_x = play_x + 39
                        return self.pos_x
                elif marc == 5:
                        self.pos_x = play_x + 34
                        return self.pos_x
                elif marc == 6:
                        self.pos_x = play_x + 19
                        return self.pos_x
                elif marc == 7:
                        self.pos_x = play_x + 19
                        return self.pos_x
                elif marc == 8:
                        self.pos_x = play_x + 15
                        return self.pos_x
                elif marc == 9:
                        self.pos_x = play_x + 5
                        return self.pos_x
                elif marc == 10:
                        self.pos_x = play_x + 12
                        return self.pos_x
                elif marc == 11:
                        self.pos_x = play_x + 17
                        return self.pos_x
        def position_stopy(self, marc, play_x, play_y):
                if marc == 12:
                        self.pos_y = play_y + 1
                        return self.pos_y
                elif marc == 1:
                        self.pos_y = play_y + 11
                        return self.pos_y
                elif marc == 2:
                        self.pos_y = play_y + 17
                        return self.pos_y
                elif marc == 3:
                        self.pos_y = play_y + 18
                        return self.pos_y
                elif marc == 4:
                        self.pos_y = play_y + 33
                        return self.pos_y
                elif marc == 5:
                        self.pos_y = play_y + 39
                        return self.pos_y
                elif marc == 6:
                        self.pos_y = play_y + 36
                        return self.pos_y
                elif marc == 7:
                        self.pos_y = play_y + 39
                        return self.pos_y

                elif marc == 8:
                        self.pos_y = play_y + 33
                        return self.pos_y
                elif marc == 9:
                        self.pos_y = play_y + 19
                        return self.pos_y
                elif marc == 10:
                        self.pos_y = play_y + 19
                        return self.pos_y
                elif marc == 11:
                        self.pos_y = play_y + 13
                        return self.pos_y

