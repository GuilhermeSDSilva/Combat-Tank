import pygame
class SONS:
    def tiro(self):
        self.som_tiro = pygame.mixer.Sound("sound/shoot.wav")
        self.som = self.som_tiro.play()
        return self.som
    def dest(self):
        self.som_destruct = pygame.mixer.Sound("sound/destruct.wav")
        self.som = self.som_destruct.play()
        return self.som
