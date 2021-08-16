import pygame

from auxiliar import *
import math

class barraforca():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 20
        self.h = 100

        self.amplitude = 0

        self.color_out = black
        self.color_in = orange

        self.subindo = True

    def draw(self, jogador):
        self.y = jogador.y - 50

        if jogador.orientacao:
            self.x = jogador.x - 30
    
            pygame.draw.rect(gameDisplay,self.color_in,[self.x, self.y + self.h, self.w, self.amplitude] )
            pygame.draw.rect(gameDisplay, self.color_out, [self.x, self.y, self.w, self.h], 2)
        else:
            self.x = jogador.x + jogador.w + 30 - self.w
            
            pygame.draw.rect(gameDisplay,self.color_in,[self.x, self.y + self.h, self.w, self.amplitude] )
            pygame.draw.rect(gameDisplay, self.color_out, [self.x, self.y, self.w, self.h], 2)

    def movimentar(self):
        if self.subindo:
            self.amplitude  -= 1.5
            if self.amplitude <= -self.h:
                self.subindo = False
        
        elif self.subindo == False:
            self.amplitude +=  1.5
            if self.amplitude >= 0:
                self.subindo = True

    def reset(self):

        self.amplitude = 0

        self.subindo = True