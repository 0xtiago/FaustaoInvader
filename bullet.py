import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Classe que administra os projeteis disparados pela espaçonave'''

    def __init__(self, fi_settings, screen, ship):
        '''Cria um objeto para o projetil na posição atual da nave'''
        super(Bullet, self).__init__()
        super.screen = screen

        # Cria um retangulo para o projetil em (0,0) e , em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, fi_settings.bullet_width, fi_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena a posição do projetil como valor decimal
        self.y = float(self.rect.y)

        self.color = fi_settings.bullet_color
        self.speed_factor = fi_settings.bullet_speed_factor

    def update(self):
        '''Move o projétil para cima da tela.'''
        # Atualiza a posição decimal do projétil
        self.y -= self.speed_factor
        # Atualiza posição de rect
        self.rect.y = self.y

    def draw_bullet(self):
        '''Desenha o projétil na tela'''
        pygame.draw.rect(self.screen, self.color, self.rect)
