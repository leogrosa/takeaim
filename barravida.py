
import pygame

from auxiliar import *
import math

class barravida():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 50
        self.h = 5

        self.amplitude = 0

        self.color_out = black
        self.color_in = life_red 

    def draw(self, player):
        self.y = player.y - 20
        self.x = player.x - 6

        self.amplitude = player.vida

        if player.vida >= 0:
            pygame.draw.rect(gameDisplay,self.color_in,[self.x, self.y, self.amplitude, self.h] )

        pygame.draw.rect(gameDisplay, self.color_out, [self.x, self.y, self.w, self.h], 2)
