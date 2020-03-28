import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, fi_settings, screen, ship, bullets):
    '''Responde ao pressionar tecla'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Cria um novo projétil e o adiciona ao grupo de projeteis
        if len(bullets) < fi_settings.bullets_allowed:
            new_bullet = Bullet(fi_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event,ship):
    '''Responde ao soltar tecla'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(fi_settings, screen, ship, bullets):
    '''Responde aos eventos de pressionamento de teclas e de mouse'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #Movimentando nave quando KEYDOWN, ou seja, pressionado.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, fi_settings, screen, ship, bullets)
        elif event.type == pygame.K_LEFT:
             check_keyup_events(event, ship)

        #Parando nave quando a tecla não estiver mais pressionada.
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(fi_settings, screen, ship, bullets):
    '''Atualiza as imagens na tela e alterna para a nova tela'''

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(fi_settings.bg_color)
    #Redesenha todos os projeteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(bullets):
    '''Atualiza a posição dos projeteis e se livra dos projeteis antigos'''
    # Atualiza as posições dos projeteis
    bullets.update()

    #Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)