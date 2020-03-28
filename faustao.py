import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Uma classe que representa um unico alienigena da frota'''

    def __init__(self,fi_settings, screen):
        '''Inicializa o alienigena e define sua posição inicial.'''
        super(Alien,self).__init__()
        self.screen = screen
        self.fi_settings = fi_settings

        #Carrega a imagem do Faustão e define seus atributos rect
        self.image = pygame.image.load('images/faustao_alien.png')
        self.rect = self.image.get_rect()

        #Inicia cada novo alienigena proximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição exata do alienigena
        self.x = float(self.rect.x)

    def blitme(self):
        '''Desenha o Faustão em sua posição atual'''
        self.screen.blit(self.image,self.rect)