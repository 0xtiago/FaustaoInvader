import sys
from time import sleep
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


def check_events(fi_settings, screen, stats, play_button, ship, aliens, bullets):
    '''Responde aos eventos de pressionamento de teclas e de mouse'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #Captura click do mouse no Play
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(fi_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

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

def check_play_button(fi_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''Inicia um novo jogo quando o jogador clicar em Play'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #Reinicia as configurações do jogo
        fi_settings.initialize_dynamic_settings()

        #Oculta o cursos do mouse
        pygame.mouse.set_visible(False)

        # Reinicia os dados estatisticos do jogo
        stats.reset_stats()
        stats.game_active = True

    # Esvazia a lista de Faustoes e projeteis
    aliens.empty()
    bullets.empty()

    # Cria uma nova frota e centraliza a espaçonave
    create_fleet(fi_settings, screen, ship, aliens)
    ship.center_ship()

def update_screen(fi_settings, screen, stats, ship, aliens, bullets, play_button):
    '''Atualiza as imagens na tela e alterna para a nova tela'''

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(fi_settings.bg_color)
    #Redesenha todos os projeteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)

    # Desenha o botão Play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível
    pygame.display.flip()



def update_bullets(fi_settings, screen, ship, aliens, bullets):
    '''Atualiza a posição dos projeteis e se livra dos projeteis antigos'''
    # Atualiza as posições dos projeteis
    bullets.update()

    #Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(fi_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(fi_settings, screen, ship, aliens, bullets):
    '''Remove qualquer projetil e Faustao que tenham colidido'''
    # Verifica se algum projetil atingiu um Faustao
    # Em caso de afirmativo, livra-se do projetil e do alienigena
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #Destroi os projeteis existentes, aumenta a velocidade e cria uma nova frota
        bullets.empty()
        create_fleet(fi_settings, screen, ship, aliens)

def get_number_aliens_x(fi_settings, alien_width):
    '''Determina o número de alienigenas que cabem em uma linha'''
    available_space_x = fi_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(fi_settings, ship_height, alien_height):
    '''Determina o número de linhas de Faustoes alienigenas que cabem na tela'''
    available_space_y = (fi_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(fi_settings, screen, aliens, alien_number, row_number):
    #Cria um alienigena e o posiciona na linha
    alien = Alien(fi_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(fi_settings, screen, ship, aliens):
    '''Cria uma frota completa de alienigenas'''
    # Cria um alienigena e calcula o numero de alienigenas em uma linha.
    alien = Alien(fi_settings, screen)
    number_aliens_x = get_number_aliens_x(fi_settings, alien.rect.width)
    number_rows = get_number_rows(fi_settings, ship.rect.height, alien.rect.height)

    #Cria frota de alienigenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(fi_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(fi_settings, aliens):
    '''Responde apropriadamente se algum Faustao atingiu uma borda.'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(fi_settings, aliens)
            break

def change_fleet_direction(fi_settings, aliens):
    '''Faz toda a frota de Faustoes descer e mudar sua direção'''
    for alien in aliens.sprites():
        alien.rect.y += fi_settings.fleet_drop_speed
    fi_settings.fleet_direction *= -1


def ship_hit(fi_settings, stats, screen, ship, aliens, bullets):
    '''Responde ao fato de a espaçonave ter sido atingida por um Faustao alienigena'''
    if stats.ships_left > 0:
        #Decrementa ships_left
        stats.ships_left -= 1
        #Esvazia a lista de Faustoes e de projeteis
        aliens.empty()
        bullets.empty()
        #Cria uma nova frota e centraliza a espaçonave
        create_fleet(fi_settings, screen, ship, aliens)
        ship.center_ship()
    else:
        #Faz uma pausa
        sleep(0.5)
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(fi_settings, stats, screen, ship, aliens, bullets):
    '''Verifica se algum Faustao alcançou a parte inferior da tela'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(fi_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(fi_settings, stats, screen, ship, aliens, bullets):
    '''Verifica se a frota esta em uma das bordas e então atualiza as posições de todos os Faustões da
    frota'''
    check_fleet_edges(fi_settings,aliens)
    aliens.update()

    #Verifica se houveram colisões entre Faustao e a espaçonave
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(fi_settings, stats, screen, ship, aliens, bullets)
        #print("Oh loco meu!!!")

    #Verifica se há algum alienigena que atingiu a parte inferior da tela
    check_aliens_bottom(fi_settings, stats, screen, ship, aliens, bullets)
