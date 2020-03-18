import sys
import pygame

def check_events(ship):
    '''Responde aos eventos de pressionamento de teclas e de mouse'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move a nave para a direita
                ship.rect.centerx += 1

def update_screen(fi_settings,screen,ship):
    '''Atualiza as imagens na tela e alterna para a nova tela'''

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(fi_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()