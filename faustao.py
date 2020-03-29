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
        self.image = pygame.image.load('images/faustao_alien2.png')
        self.image = pygame.transform.scale(self.image, (43, 62))
        self.rect = self.image.get_rect()

        #Inicia cada novo alienigena proximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição exata do alienigena
        self.x = float(self.rect.x)

    def blitme(self):
        '''Desenha o Faustão em sua posição atual'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''Retorna True se o Faustão estiver na borda da tela'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''Move o aliengiena para a direita ou para a esquerda'''
        self.x += (self.fi_settings.alien_speed_factor * self.fi_settings.fleet_direction)
        self.rect.x = self.x
