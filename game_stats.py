class GameStats():
    '''Armazena dados estatisticos do Fauustão Invaders'''

    def __init__(self, fi_settings):
        '''Inicializa os dados estatisticos'''
        self.fi_settings = fi_settings
        self.reset_stats()
        #Inicia invasão faustonica em um estado ativo
        self.game_active = False

    def reset_stats(self):
        '''Inicializa os dados estatisticos que podem mudar durante o jogo'''
        self.ships_left = self.fi_settings.ship_limit
        self.score = 0

