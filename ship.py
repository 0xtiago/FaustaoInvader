import pygame

class Ship():
    def __init__(self,screen):
        '''Inicializa a nave e define sua posição incial'''
        self.screen = screen

        #Carrega a imagem da nave e converte no tamanho adequado.
        self.image = pygame.image.load('images/ship4.png')
        self.image = pygame.transform.scale(self.image,(60,48))

        # Obtem atributos da imagem como se fosse um retangulo (rect). O que torna mais simples
        self.rect = self.image.get_rect()

        # obtem atributos do retangulo da tela
        self.screen_rect = screen.get_rect()

        #Inicia a cada nova nave na parte inferior central da tela
        ##Configura o centro do retangulo da imagem com o centro do retangulo da tela
        self.rect.centerx = self.screen_rect.centerx

        ##Configura a posição do retantulo com a parte mais inferior da tela
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Desenha a espaçonave em sua posição atual'''
        self.screen.blit(self.image,self.rect)