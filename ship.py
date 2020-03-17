import pygame

class Ship():
    def __init__(self,screen):
        '''Inicializa a nave e define sua posição incial'''
        self.screen = screen

        #Carrega a imagem da nave e obtem seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Inicia a cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Desenha a espaçonave em sua posição atual'''
        self.screen.blit(self.image,self.rect)