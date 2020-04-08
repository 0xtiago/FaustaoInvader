import pygame.font

class Scoreboard():
    '''Uma classe para mostrar informações sobre pontuação'''

    def __init__(self, fi_settings, screen, stats):
        '''Inicializa os atributos da pontuação'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.fi_settings = fi_settings
        self.stats = stats

        #Configurações de fonte para as informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepara a imagem da pontuação inciial
        self.prep_score()

    def prep_score(self):
        '''Tranforma a pontuação em uma imagem renderizada'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.fi_settings.bg_color)

        #Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''Desenha a pontuação na tela'''
        self.screen.blit(self.score_image, self.score_rect)