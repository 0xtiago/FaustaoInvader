import sys
import pygame
from bullet import Bullet
from faustao import Alien

def check_keydown_events(event, fi_settings, screen, ship, bullets):
    '''Responde ao pressionar tecla'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(fi_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(fi_settings, screen, ship, bullets):
    '''Dispara um projetil se o limite ainda nao foi alcançado'''
    # Cria um novo projétil e o adiciona ao grupo de projeteis
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


def update_screen(fi_settings, screen, ship, aliens, bullets):
    '''Atualiza as imagens na tela e alterna para a nova tela'''

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(fi_settings.bg_color)
    #Redesenha todos os projeteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)

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

def get_number_aliens_x(fi_settings, alien_width):
    '''Determina o número de alienigenas que cabem em uma linha'''
    available_space_x = fi_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(fi_settings, screen, aliens, alien_number):
    #Cria um alienigena e o posiciona na linha
    alien = Alien(fi_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(fi_settings, screen, aliens):
    '''Cria uma frota completa de alienigenas'''
    # Cria um alienigena e calcula o numero de alienigenas em uma linha.
    alien = Alien(fi_settings, screen)
    number_aliens_x = get_number_aliens_x(fi_settings, alien.rect.width)

    #Cria a primeira linha de alienigenas
    for alien_number in range(number_aliens_x):
        create_alien(fi_settings,screen,aliens, alien_number)
