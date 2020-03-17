class Settings():
    '''Esta classe é utilizada armazenar todas as configurações do Faustão Invader'''

    def __init__(self):
        '''Inicializando confs'''

        #CONFIGURAÇÕES DA JANELA
        ################################################################################
        ##Configuração do título do jogo
        self.titulo_jogo = "Faustão Invader"

        ##Configuração do ícone da janela
        self.icone_jogo = "images/faustao_icon.png"



        #CONFIGURAÇÕES DA TELA
        ################################################################################
        ##Configuração das dimensões da janela em pixels
        self.screen_width = 1200
        self.screen_height = 800

        ##Configuração da cor de fundo da janela
        self.bg_color = (230,230,230)