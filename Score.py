import pygame


class SCORE:
    def pontuacao(self, plac):
        self.pont = plac + 1
        return self.pont

    def placar1(self, plac_1, tela):
        self.score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
        self.score_text = self.score_font.render('00', True, "blue", "brown")
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = (450, 50)
        self.score_text = self.score_font.render(str(
            plac_1), True, "blue", "brown")
        self.ret = tela.blit(self.score_text, self.score_text_rect)
        return self.ret

    def placar2(self, plac_2, tela):
        self.score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
        self.score_text = self.score_font.render('00', True, "green", "brown")
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = (540, 50)
        self.score_text = self.score_font.render(str(
            plac_2), True, "green", "brown")
        self.ret = tela.blit(self.score_text, self.score_text_rect)
        return self.ret
