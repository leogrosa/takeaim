import pygame
import math
from auxiliar import *

class seta():
    def __init__(self):
        
        self.subindo = True
        self.angle = 0
        self.d_angle = 0

    def draw(self, jogador):

            if self.angle <= -90:
                self.angle =  -90
            if self.angle >= 0:
                self.angle = 0

            if jogador.orientacao:
                pygame.draw.line(gameDisplay, gray, ((jogador.x+jogador.w/2), (jogador.y+jogador.h/2)), ((jogador.x+jogador.w/2) + 80*math.cos(grau_radiano(self.angle)), (jogador.y+jogador.h/2) + 80*math.sin(grau_radiano(self.angle))), 2)
            else:
                pygame.draw.line(gameDisplay, gray, ((jogador.x+jogador.w/2), (jogador.y+jogador.h/2)), ((jogador.x+jogador.w/2) - 80*math.cos(grau_radiano(self.angle)), (jogador.y+jogador.h/2) + 80*math.sin(grau_radiano(self.angle))), 2)

    def movimentar(self, jogador):
            if self.subindo:
                self.angle  -= 1
                if self.angle == -90:
                    self.subindo = False
            
            elif self.subindo == False:
                self.angle +=  1
                if self.angle == 0:
                    self.subindo = True

    def update(self):
        self.angle += self.d_angle

    def reset(self):
        self.subindo = True
        self.angle = 0
        self.d_angle = 0