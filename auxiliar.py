import pygame

import random

#Definicao da Resolucao
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

#Definicao da frequencia de atualizacao da tela
FPS = 60

###############################################################################
#                              Constantes
###############################################################################

# Definicoes gerais
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Take Aim - Versão Alpha 1.5.0")
clock = pygame.time.Clock()

# Definições de cores
black = (0,0,0)
gray   = (39,40,34)
orange = (253,151,31)
pink   = (249,38,114)  
blue   = (102,217,239)
green  = (166,226,46)
white  = (255,255,255)
life_red = (255, 57, 57)
cinza_normal = (143, 151, 139)

# Constantes matematicas
pi = 3.141592

#Constantes fisicas
g = 9.8 # m/s^2

#Proporçoes
prop_metro = 0.544
prop_px = 17

###############################################################################
#                          Imagens dos projéteis
###############################################################################
P1img = pygame.image.load("figs/Bala_.png")
P2img = pygame.image.load("figs/bolacanhao.png")

###############################################################################
#                          Constantes dos projéteis
###############################################################################
constP1  = (1/2)*0.42*0.171 #1/2 * coeficiente de arrasto* área de secção --> Constante Aerodinâmica da bala Tipo 1
constP2 = (1/2)*0.47*2.1871

###############################################################################
#                          Projéteis pré-definidos
###############################################################################

#P1 = 300, 7, 17, P1img, constP1
#P2 = 500, 25, 25, P2img, constP2




###############################################################################
#                              Funcoes matematicas
###############################################################################

def grau_radiano(valor_grau):
    radiano = valor_grau*(pi/180)
    return radiano

def radiano_grau(valor_radiano):
    grau = valor_radiano*(180/pi)
    return grau

def pixel_metro(valor_pixels):
    v_metro = valor_pixels*(prop_metro/prop_px)
    return v_metro

def metro_pixel(valor_metros):
    v_pixel = valor_metros*(prop_px/prop_metro)
    return v_pixel

###############################################################################
#                                 Texto
###############################################################################

# renderiza o texto
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# apresenta texto na tela
def display_message(text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)

    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
###############################################################################
#                                 Imagens
###############################################################################

fundo1 = pygame.image.load("figs/fundo.png")
chao1 = pygame.image.load("figs/chao.png")

sleeper = pygame.image.load("figs/sleepertest.png")

###############################################################################
#                            Funçoes de desenhar                              #
###############################################################################

def desenha_fundo(img):
    gameDisplay.blit(img, (0,0))

def desenha_chao(img):
    gameDisplay.blit(img, (0,550))


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


#############################################################################
#                           FUNCAO TESTE                                    #
#############################################################################


def jogada(event, jogador, seta, barra, bala):
    
    # botao foi pressionado
    if event.type == pygame.KEYDOWN:
        # esquerda
        if event.key == pygame.K_LEFT:
            jogador.dx = -4
        # direita
        elif event.key == pygame.K_RIGHT:
            jogador.dx = 4

        ###########################################
        # ESCOLHA DO ANGULO E FORCA DE LANCAMENTO #
        ###########################################
        if event.key == pygame.K_f and not jogador.escolheu_angulo and not jogador.escolheu_forca and not bala.lancada :
            jogador.escolhendo_angulo = True

        ####### MOVIMENTO DA SETA #########
        if jogador.escolhendo_angulo:
            if event.key == pygame.K_UP:
                seta.d_angle = -2

            elif event.key == pygame.K_DOWN:
                seta.d_angle = 2
        ###################################    

        if not bala.lancada:
            if event.key == pygame.K_g and jogador.escolhendo_angulo and not jogador.escolheu_forca :
                jogador.escolhendo_angulo = False
                jogador.escolheu_angulo = True
                jogador.empunha_arma()
                jogador.escolhendo_forca = True

            if event.key == pygame.K_h and jogador.empunhou and jogador.escolhendo_forca:
                jogador.escolhendo_forca = False
                jogador.escolheu_forca = True


            if event.key == pygame.K_j and jogador.empunhou:
                jogador.atirar(bala)
                jogador.escolhendo_forca = False
                jogador.escolheu_angulo = False
                jogador.escolheu_forca = False

                jogador.empunhou = False


    # botao foi solto
    if event.type == pygame.KEYUP:
        # esquerda ou direia
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            jogador.dx = 0

        if jogador.escolhendo_angulo and (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
            seta.d_angle = 0

def reset(player, bala, chao, barra, seta):
    player.zerar_dx()
    bala.reset()
    chao.reset()
    barra.reset()
    seta.reset()

'''
# botao foi pressionado
            if event.type == pygame.KEYDOWN:
                # esquerda
                if event.key == pygame.K_LEFT:
                    jogador1.dx = -4
                # direita
                elif event.key == pygame.K_RIGHT:
                    jogador1.dx = 4

                ###########################################
                # ESCOLHA DO ANGULO E FORCA DE LANCAMENTO #
                ###########################################
                if event.key == pygame.K_f and not jogador1.escolheu_angulo and not jogador1.escolheu_forca and not bala1.lancada :
                    jogador1.escolhendo_angulo = True

                ####### MOVIMENTO DA SETA #########
                if jogador1.escolhendo_angulo:
                    if event.key == pygame.K_UP:
                        seta1.d_angle = -2

                    elif event.key == pygame.K_DOWN:
                        seta1.d_angle = 2
                ###################################    

                if event.key == pygame.K_g and jogador1.escolhendo_angulo and not jogador1.escolheu_forca and not bala1.lancada :
                    jogador1.escolhendo_angulo = False
                    jogador1.escolheu_angulo = True
                    jogador1.empunha_arma()
                    jogador1.escolhendo_forca = True

                if event.key == pygame.K_h and jogador1.empunhou and jogador1.escolhendo_forca and not bala1.lancada:
                    jogador1.escolhendo_forca = False
                    jogador1.escolheu_forca = True


                if event.key == pygame.K_j and jogador1.empunhou and not bala1.lancada:
                    bala1.lanca(jogador1.forca_escolhida, -jogador1.angulo_escolhido, jogador1)
                    jogador1.escolhendo_forca = False
                    jogador1.escolheu_angulo = False
                    jogador1.escolheu_forca = False

                if event.key == pygame.K_r:
                    game_start()

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    jogador1.dx = 0

                if jogador1.escolhendo_angulo and (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    seta1.d_angle = 0
'''