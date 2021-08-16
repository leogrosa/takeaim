import math
import pygame

from auxiliar import *

class player():

    def __init__(self, x, y, img, width, height, orientation, Direita):
        self.x = x
        self.y = y

        self.dx = 0
        self.dy = 0
        
        self.w  = width
        self.h = height

        self.img = img

        self.escolhendo_angulo = False
        self.escolheu_angulo = False

        self.escolhendo_forca = False
        self.escolheu_forca = False

        self.empunhou = False

        self.angulo_escolhido = 0
        self.forca_escolhida = 0

        self.orientacao = orientation #True para direita, False para esquerda.

        self.jogando = True

        self.x_rodada = 0

        self.ComecouDireita = Direita #True para direita, False para esquerda.

        self.naTela = True

        self.DeltaX = 0

        self.vida = 50
        self.Perdeu = False

    def __repr__(self):
        return "X: {} Y:{}  W:{} H:{}".format(self.x, self.y, self.w, self.h)

    def update(self, bala, seta, barra, chao, gs):

        if self.vida <= 0:
            self.Perdeu = True
            self.vida = 0

        if self.jogando and not self.escolhendo_angulo and not self.escolhendo_forca and not bala.lancada:

            if self.dx > 0:
                self.orientacao = True
            elif self.dx < 0:
                self.orientacao = False
                
            if not chao.ajustando and (gs == 1 or  gs == 3):
                
                if self.x_rodada >= 0 and self.x_rodada <= DISPLAY_WIDTH/2:
                    if self.x <= 2:
                        self.x = 2

                    if self.x >= DISPLAY_WIDTH/2 -2 - self.w:
                        self.x = DISPLAY_WIDTH/2 -2 - self.w

                elif self.x_rodada >= DISPLAY_WIDTH/2  and self.x_rodada <= DISPLAY_WIDTH:
                    if self.x <= DISPLAY_WIDTH/2 + 2:
                        self.x = DISPLAY_WIDTH/2 + 2
                    
                    if self.x >= DISPLAY_WIDTH - 2 - self.w:
                        self.x = DISPLAY_WIDTH  - 2 - self.w
                    

                if self.x <= chao.x:
                    self.x = chao.x
                elif self.x >= chao.x + chao.w:
                    self.x = chao.x + chao.w

        
        
        self.DeltaX = chao.dx

        if not bala.lancada and not self.escolhendo_angulo and not self.escolhendo_forca:
            self.x += self.dx 
            
        self.x += self.DeltaX


        self.escolhe_angulo(seta)
        self.escolhe_forca(barra)
    
    def is_naTela(self):

        if self.x >= 0 and self.x <= DISPLAY_WIDTH - self.w:
            self.naTela = True
        else:
            self.naTela = False


    def draw(self, arma):
        if self.orientacao:
            gameDisplay.blit(self.img, (self.x, self.y))
        else:
            gameDisplay.blit(pygame.transform.flip(self.img, True, False), (self.x, self.y))

        if self.empunhou:
            arma.draw(self)

    def zerar_dx(self):
        self.dx = 0


    def empunha_arma(self):
        self.empunhou = True

    def atirar(self, bala):
         bala.lanca(self)


    def escolhe_angulo(self, seta):
   
        if self.escolhendo_angulo:
            seta.draw(self)
            seta.update()

        if self.escolheu_angulo:
            seta.draw(self)

        self.angulo_escolhido = seta.angle


    def escolhe_forca(self, barra):
        if self.escolhendo_forca:
            barra.draw(self)
            barra.movimentar()

        if self.escolheu_forca:
            barra.draw(self)

        self.forca_escolhida = (-barra.amplitude)*295 + 1500


        





        