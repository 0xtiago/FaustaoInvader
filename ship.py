import pygame

class Ship():
    def __init__(self,fi_settings, screen):
        '''Inicializa a nave e define sua posição incial'''
        self.screen = screen
        self.fi_settings = fi_settings

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

        ##Armazena um valor decimal para o centro da espaçonavw
        self.center = float(self.rect.centerx)

        #Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Atualiza a posição da espaçonave de acrodo com a flag de movimento'''
        #Atualiza o valor do centro da espaçonave, e não do retangulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.fi_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.fi_settings.ship_speed_factor

        #Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''Desenha a espaçonave em sua posição atual'''
        self.screen.blit(self.image,self.rect)