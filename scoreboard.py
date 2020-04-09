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

        #Prepara as imagens das pontuações iniciais
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        '''Tranforma a pontuação em uma imagem renderizada'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.fi_settings.bg_color)

        #Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''Transforma a pontuação maxima em uma imagem renderizada'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                 self.fi_settings.bg_color)

        #Centraliza a pontuação axima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        '''Desenha a pontuação na tela'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_level(self):
        '''Transforma o nível em uma linguagem renderizada'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.fi_settings.bg_color)

        #Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
