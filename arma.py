
import pygame
import math

from auxiliar import *

class arma():
    
    def __init__(self, img, w, h, player):
        self.originalImg = img


        self.x = player.x + player.w/4
        self.y = player.y + player.h/4

        self.w = w
        self.h = h
        self.img = self.originalImg


        self.angle = 0

        self.rect = self.img.get_rect()

      

    def draw(self, player):
        self.img = rot_center(self.originalImg, -player.angulo_escolhido)
        
        self.y = player.y - 70 
        
        if player.orientacao:
            self.x = player.x - 40
            gameDisplay.blit(self.img, (self.x, self.y))
        else:
            self.x = player.x - player.w - 40 
            gameDisplay.blit(pygame.transform.flip(self.img, True, False), (self.x, self.y))
