import pygame

class Ship():
    def __init__(self,screen):
        '''Inicializa a nave e define sua posição incial'''
        self.screen = screen

        #Carrega a imagem da nave e obtem seu rect
        self.image = pygame.image.load('images/ship.bmp') #Carrega imagem na nave
        self.rect = self.image.get_rect() #Obtem atributos da imagem como se fosse um retangulo (rect). O que torna
                                          #mais simples

        self.screen_rect = screen.get_rect() #obtem atributos do retangulo da tela

        #Inicia a cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx #Configura o centro do retangulo da imagem com o centro do retangulo
                                                    # da tela
        self.rect.bottom = self.screen_rect.bottom #Configura a posição do retantulo com a parte mais inferior da tela

    def blitme(self):
        '''Desenha a espaçonave em sua posição atual'''
        self.screen.blit(self.image,self.rect)