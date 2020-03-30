class Settings():
    '''Esta classe é utilizada armazenar todas as configurações do Faustão Invader'''

    def __init__(self):
        '''Inicializando confs'''

        #CONFIGURAÇÕES DA JANELA
        ################################################################################
        ##Configuração do título do jogo
        self.titulo_jogo = "Faustão Invader - v0.1"

        ##Configuração do ícone da janela
        self.icone_jogo = "images/faustao_icon.png"


        #CONFIGURAÇÕES DA TELA
        ################################################################################
        ##Configuração das dimensões da janela em pixels
        self.screen_width = 1200
        self.screen_height = 800
        #self.screen_width = 800
        #self.screen_height = 600

        ##Configuração da cor de fundo da janela
        self.bg_color = (153,204,255) #Alterando cor de fundo.
        #self.bg_color = (230,230,230)


        #CONFIGURAÇÕES DA ESPAÇONAVE
        ################################################################################
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #CONFIGURAÇÕES DOS TIROS
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # CONFIGURAÇÕES DOS FAUSTOES ALIENIGENAS
        ################################################################################
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction igual a 1 representa direita. -1 representa esquerda
        self.fleet_direction = 1