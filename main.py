import time
import random
import math

import pygame

from auxiliar import *

from projetil import projetil
from fluid import fluid
from player import player
from solo import solo
from arma import arma
from seta import seta
from barraforca import barraforca
from barravida import barravida

pygame.init()

###############################################################################
#                           Tela Inicial
###############################################################################
def game_start():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    intro = False
                    game_loop()

        tela = pygame.image.load("figs/telainicial.png")  
     
        gameDisplay.blit(tela, (0,0))

        pygame.display.update()
        clock.tick(FPS)

###############################################################################
#                           TELA FINAL                                        #
###############################################################################
def tela_final(jogador1, jogador2):
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    intro = False
                    game_start()

        if jogador1.Perdeu:
            tela = pygame.image.load("figs/telafinal2.png")
        elif jogador2.Perdeu:
            tela = pygame.image.load("figs/telafinal1.png")

        gameDisplay.blit(tela, (0,0))

        pygame.display.update()
        clock.tick(FPS)

def game_loop():
    gameExit = False
    gameState = 1

    #Atributos do jogador
    jogador1_img = pygame.image.load("figs/sonic1.png")
    jogador2_img = pygame.image.load("figs/sonic1.png")

    #Setinha
    seta1 = seta()
    
    #declarando jogador
    jogador1 = player(100, 500, jogador1_img, 38, 50, True, False)
    jogador2 = player(2*DISPLAY_WIDTH - 100 - 38, 500, jogador2_img, 38, 50, False, True)

    jogador2.jogando = False

    #Declarando projeteis
    bala1 = projetil(300, 7, 17, P1img, constP1, jogador1, 1)


    #Declarando atmosfera
    atmosfera = fluid(0, 1)

    #Declarando o chao
    chao = solo(0, 550, chao1, DISPLAY_WIDTH*2, 50)

    #Declarando a arma
    arma1 = arma(sleeper, 96, 36, jogador1)
    
    #Declarando a barra de forca
    barra1 = barraforca()

    #declarando a barra de vida
    barradevida1 = barravida()

    

    while not gameExit:

        if gameState == 1:
                
            jogador1.jogando = True
            currentPlayer = jogador1

            for event in pygame.event.get():
                ############ PARA PODER FECHAR ###############
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_start()
                ##############################################
                    

                jogada(event, jogador1, seta1, barra1, bala1)

            if bala1.lancamento_acabou:

                reset(jogador1, bala1, chao, barra1, seta1)

                gameState = 2
                

        elif gameState == 2:
            ############ PARA PODER FECHAR ###############
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_start()
            ##############################################

            #chao.reset()
            
            jogador1.jogando = False
            jogador2.jogando = False

            chao.camera_ajustar(jogador2)

            if (jogador2.x >= 3*DISPLAY_WIDTH/4 - 30  and jogador2.x <= 3*DISPLAY_WIDTH/4 + 30) or chao.TransladouDirEsq or chao.TransladouEsqDir:
                chao.ajustando = False
                gameState = 3
                chao.reset()
                jogador2.x_rodada = jogador2.x
                

        elif gameState == 3:

            #chao.reset()
            jogador2.jogando =  True
            currentPlayer = jogador2

            for event in pygame.event.get():
                ############ PARA PODER FECHAR ###############
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_start()
                ##############################################

                jogada(event, jogador2, seta1, barra1, bala1)

            if bala1.lancamento_acabou:
                reset(jogador2, bala1, chao, barra1, seta1)

                gameState = 4


        elif gameState == 4:
            ############ PARA PODER FECHAR ###############
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_start()
            ##############################################

            #chao.reset()

            jogador1.jogando = False
            jogador2.jogando = False

            chao.camera_ajustar(jogador1)
            
            if (jogador1.x >= DISPLAY_WIDTH/4 - 30 and jogador1.x <= DISPLAY_WIDTH/4 + 30) or chao.TransladouEsqDir or chao.TransladouDirEsq:
                chao.ajustando = False
                gameState = 1
                chao.reset()
                jogador1.x_rodada = jogador1.x
                

        desenha_fundo(fundo1)

        print('{}'.format(barra1.amplitude))
        
        if jogador1.Perdeu or jogador2.Perdeu:
            tela_final(jogador1, jogador2)

        chao.update(bala1)
        chao.draw()  
    
        jogador1.update(bala1, seta1, barra1, chao, gameState)
        jogador2.update(bala1, seta1, barra1, chao, gameState)

        bala1.colision_check(chao, jogador1)
        bala1.colision_check(chao, jogador2)
        
        bala1.update(atmosfera, chao, currentPlayer)

        bala1.draw()

        jogador1.draw(arma1)
        jogador2.draw(arma1)

        barradevida1.draw(jogador1)
        barradevida1.draw(jogador2)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    game_start()

    pygame.quit()
    quit()