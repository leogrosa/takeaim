import pygame
import math

from auxiliar import grau_radiano, radiano_grau

class fluid():

    def __init__(self, coef_viscosidade, densidade):
        self.coefV = coef_viscosidade
        self.dens = densidade

    def __repr__(self):
        return "Coef Viscosidade: {}, Densidade: {}".format(self.coefV, self.dens)

    def drag_force(self, corpo):
        
        dF_x = self.dens*corpo.const_aero*corpo.vel_x*corpo.vel_x

        dF_y = self.dens*corpo.const_aero*corpo.vel_y*corpo.vel_y

        return dF_x, dF_y
