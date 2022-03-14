import pygame
class Bullet:
        
        def _init_(self):
            self.bala = pygame.image.load("img/bala(1).png")
            self.bala = pygame.transform.scale(self.bala, (3, 3))
            return self.bala
        def bala2(self):
            self.bala = pygame.image.load("img/bala(2).png")
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
                

        def colisao_barreira_direita_esquerda(self, pos_x,pos_y, mov):
                #barreira 1
                if (170 <= pos_x <=173) and (298 <= pos_y <= 480):
                        self.marc = False
                        return self.marc
                elif (224 <= pos_x <=227) and (298 <= pos_y <= 480):
                        self.marc = False
                        return self.marc
                #barreira 2
                elif (254 <= pos_x <=257) and (350 <= pos_y <= 420):
                        self.marc = False
                        return self.marc
                elif (366 <= pos_x <=369) and (350 <= pos_y <= 420):
                        self.marc = False
                        return self.marc
                #barreira 3
                elif (414 <= pos_x <=417) and (200 <= pos_y <= 270):
                        self.marc = False
                        return self.marc
                elif (525 <= pos_x <=528) and (200 <= pos_y <= 270):
                        self.marc = False
                        return self.marc
                #barreira 4
                elif (414 <= pos_x <=417) and (500 <= pos_y <= 570):
                        self.marc = False
                        return self.marc
                elif (525 <= pos_x <=528) and (500 <= pos_y <= 570):
                        self.marc = False
                        return self.marc
                # barreira 5
                elif (564 <= pos_x <=567) and (350 <= pos_y <= 420):
                        self.marc = False
                        return self.marc
                elif (676 <= pos_x <=679) and (350 <= pos_y <= 420):
                        self.marc = False
                        return self.marc
                #barreira 6
                elif (720 <= pos_x <=723) and (298 <= pos_y <= 480):
                        self.marc = False
                        return self.marc
                elif (770 <= pos_x <=773) and (298 <= pos_y <= 480):
                        self.marc = False
                        return self.marc
                else:
                        self.marc = mov
                        return self.marc
                
        def colisao_barreira_cima_baixo(self, pos_x,pos_y,mov):
                #barreira 1
                if (155 <= pos_x <=228) and (298 <= pos_y <= 301):
                        self.marc = False
                        return self.marc
                elif (155 <= pos_x <=228) and (477 <= pos_y <= 480):
                        self.marc = False
                        return self.marc
                #barreira 2
                elif (254 <= pos_x <=369) and (355 <= pos_y <= 358):
                        self.marc = False
                        return self.marc
                elif (254 <= pos_x <=369) and (420 <= pos_y <= 423):
                        self.marc = False
                        return self.marc
                #barreira 3
                elif (414 <= pos_x <=528) and (205 <= pos_y <= 208):
                        self.marc = False
                        return self.marc
                elif (414 <= pos_x <=528) and (270 <= pos_y <= 273):
                        self.marc = False
                        return self.marc
                #barreira 4
                elif (414 <= pos_x <=528) and (500 <= pos_y <= 503):
                        self.marc = False
                        return self.marc
                elif (414 <= pos_x <=528) and (570 <= pos_y <= 573):
                        self.marc = False
                        return self.marc
                        # barreira 5
                elif (564 <= pos_x <=679) and (350 <= pos_y <= 353):
                        self.marc = False
                        return self.marc
                elif (564 <= pos_x <=679) and (420 <= pos_y <= 423):
                        self.marc = False
                        return self.marc
                # barreira 6
                elif (709 <= pos_x <=782) and (298 <= pos_y <= 301):
                        self.marc = False
                        return self.marc
                elif (709 <= pos_x <=782) and (477 <= pos_y <= 480):
                        self.marc = False
                        return self.marc
        
                else:
                        self.marc = mov
                        return self.marc
