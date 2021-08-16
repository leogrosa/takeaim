import math
import pygame

from auxiliar import *

class projetil:

    def __init__(self, massa, w, h, img, const_aero, player, municao):
        self.massa = massa

        self.pos_x = player.x + player.w/2
        self.pos_y = player.y + player.h/2

        self.w = w
        self.h = h

        self.vel_x = 0
        self.vel_y = 0

        self.acel_x = 0
        self.acel_y = 0

        self.Frx = 0
        self.Fry = 0
        
        self.peso = 0

        self.original_img = img #imagem original deve ser preservada
        self.image = self.original_img #self.image será a imagem a cada instante, rotacionada ou não

        self.angle = 90

        self.const_aero = const_aero

        self.saiuX1 = False
        self.saiuX2 = False

        self.saiuY = False

        self.lancada = False

        self.orientacao = True

        self.lancamento_acabou = False

        self.dano_maximo = 0
        self.multiplicador_municao = municao




    def __repr__(self):
        return "M: {} X:{} Y:{} Vx:{} Vy:{} Ax:{} Ay:{} Fx:{} Fy:{} Ang:{}".format(self.massa, self.pos_x, self.pos_y, self.vel_x, self.vel_y, self.acel_x, self.acel_y, self.Frx, self.Fry, self.angle)

    
    
    def lanca(self, player):
        '''
        Faz o lançamento do projétil
        '''

        self.pos_x = player.x+10
        self.pos_y = player.y+10

        self.orientacao = player.orientacao

        if player.orientacao:
            F = player.forca_escolhida
            angulo_lancamento = -player.angulo_escolhido
        else:
            F = -player.forca_escolhida
            angulo_lancamento = player.angulo_escolhido

        vel_inic = metro_pixel((F*0.5)/self.massa)
        self.vel_x = vel_inic*math.cos(grau_radiano(angulo_lancamento))
        self.vel_y = -vel_inic*math.sin(grau_radiano(angulo_lancamento))
        self.peso = self.massa*(metro_pixel(g))


        self.lancada = True



    def draw(self):
        if self.lancada:
            if self.orientacao:
                gameDisplay.blit(self.image, (self.pos_x, self.pos_y))
            else:
                gameDisplay.blit(pygame.transform.flip(self.image, True, False), (self.pos_x, self.pos_y))
                
    
    def colision_check(self, chao, player):

        if self.lancada:
            #colidiu com o chao
            if self.pos_y >= chao.y:
                self.saiuY = True
                #explode()
                if abs(self.pos_x - player.x + player.w/2) < 150: # se a distancia da bala ao jogador for menor que 100 pixels
                    player.vida -= -self.dano_maximo/150 + self.dano_maximo

            #colidiu com o player
            elif not player.jogando:
                if self.orientacao:
                    if (self.pos_x + self.w/2 >= player.x and self.pos_x + self.w/2 <= player.x + player.w) and self.pos_y >= player.y:
                        #explode()
                        player.vida -= self.dano_maximo
                        self.saiuY = True
                else:
                    if (self.pos_x <= player.x + player.w and self.pos_x + self.w/2 >= player.x ) and self.pos_y >= player.y:
                        #explode()
                        player.vida -= self.dano_maximo
                        self.saiuY = True


    def update(self, fluid, solo, currentPlayer):
        '''
        Atualiza a posição, velocidade, angulo, etc do projétil na tela
        '''
        #Saiu em X indo pra direita
        if self.orientacao:
            if self.pos_x >= DISPLAY_WIDTH/2:
                self.saiuX1 = True
            
            if self.saiuX1 and not solo.TransladouDirEsq:
                #Limita a posição
                if not currentPlayer.ComecouDireita:
                    self.pos_x = DISPLAY_WIDTH/2

        #Saiu em X indo pra esquerda
        else:
            if self.pos_x <= DISPLAY_WIDTH/2:
                self.saiuX2 = True
            
            if self.saiuX2 and not solo.TransladouEsqDir:
                #Limita a posição
                if currentPlayer.ComecouDireita:
                    self.pos_x = DISPLAY_WIDTH/2


        ################IREI ALTERAR###################
        #Limita a posição da bala em Y
        if self.pos_y > DISPLAY_HEIGHT:
            self.pos_y = DISPLAY_HEIGHT
            self.saiuY = True

        if self.saiuY:
            self.Frx, self.Fry, self.acel_x, self.acel_y, self.vel_y, self.vel_x = 0, 0, 0, 0, 0, 0
            self.lancamento_acabou = True
        ###############################################

        if not self.saiuY and self.lancada:
            dF_x, dF_y = fluid.drag_force(self)

            #Atualiza as Forças
            if self.orientacao:
                self.Frx = -dF_x
            else:
                self.Frx = dF_x

            self.Fry = self.peso + dF_y

            #Atualiza as acelerações
            self.acel_x = (self.Frx/self.massa)
            self.acel_y = (self.Fry/self.massa) 
            
            #Atualiza as velocidades
            self.vel_x += (self.acel_x*(1/FPS))
            self.vel_y += (self.acel_y * (1/FPS)) 

            
            #Atualiza as posições
            self.pos_x += (self.vel_x * (1/FPS)) 
            self.pos_y += (self.vel_y * (1/FPS))

            #Atualiza o ângulo do projétil
            if self.vel_x != 0:
                angle = -radiano_grau(math.atan(self.vel_y/self.vel_x))
            else:
                angle = 270

            
            self.dano_maximo = (self.massa*(math.sqrt(self.vel_x*self.vel_x + self.vel_y*self.vel_y))*self.multiplicador_municao)*(40/468750)

            self.angle = angle 
            
            #Rotaciona o projétil de acordo com o ângulo
            if self.orientacao:
                self.image = pygame.transform.rotate(self.original_img, self.angle-90)
            else:
                self.image = pygame.transform.rotate(self.original_img, -self.angle-90 )



    def reset(self):
        self.pos_x = 0
        self.pos_y = 0

        self.vel_x = 0
        self.vel_y = 0

        self.acel_x = 0
        self.acel_y = 0

        self.Frx = 0
        self.Fry = 0
        
        self.peso = 0

        self.angle = 90

        self.saiuX1 = False
        self.saiuX2 = False

        self.saiuY = False

        self.lancada = False

        self.orientacao = True

        self.lancamento_acabou = False
        self.dano_maximo = 0