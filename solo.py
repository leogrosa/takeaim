
import pygame
from auxiliar import *
from projetil import *

class solo():

    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = y
        self.img = img
        self.w = width
        self.h = height

        self.TransladouDirEsq = False
        self.TransladouEsqDir = False

        self.dx = 0

        self.ajustando = False

    def update(self, bala):
        
        self.x = self.x + self.dx

        if (bala.saiuX1 or bala.saiuX2) and not self.TransladouDirEsq and not self.TransladouEsqDir:
            self.dx = (-bala.vel_x * (1/FPS))

        if self.TransladouEsqDir or self.TransladouDirEsq:
            self.dx = 0

        ####### CHECA SE TRANSLADOU #############

        if self.dx > 0 and self.x >= 0:
            self.x = 0
            self.TransladouEsqDir = True
            self.TransladouDirEsq = False
            self.dx = 0

        elif self.dx < 0 and self.x < DISPLAY_WIDTH - self.w:
            self.x = DISPLAY_WIDTH - self.w
            self.TransladouDirEsq = True
            self.TransladouEsqDir = False
            self.dx = 0
        ##########################################

        if not self.ajustando and not bala.lancada:
            self.dx = 0

    def reset(self):
        self.TransladouEsqDir, self.TransladouDirEsq  = False, False
        self.dx = 0
        

    def draw(self):
        gameDisplay.blit(self.img, (self.x , self.y))


    def camera_ajustar(self, player):

            self.ajustando = True
                
            if player.ComecouDireita:
                if player.x < 3*DISPLAY_WIDTH/4 - 20:
                    self.dx = 4

                elif player.x > 3*DISPLAY_WIDTH/4 + 20:
                    self.dx = -4
                    

            elif not player.ComecouDireita:
                if player.x < DISPLAY_WIDTH/4 - 20:
                    self.dx = 4

                elif player.x > DISPLAY_WIDTH/4 + 20:
                    self.dx = -4
                        
            
            if self.TransladouDirEsq or self.TransladouEsqDir:
                self.dx = 0

                    

            
        


