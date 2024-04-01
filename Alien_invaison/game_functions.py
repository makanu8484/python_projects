import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, screen_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(screen_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(screen_settings, screen, ship, bullets):
    # Fire a bullet if limit not reached yet.
    # Create bullet and add it to the bullet group
    if len(bullets) < screen_settings.bullets_allowed:
        new_bullet = Bullet(screen_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(screen_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen_setting, screen, ship, aliens, bullets):
    screen.fill(screen_setting.background_color)
    ship.draw_location()
    aliens.draw(screen)


def update_bullets(bullets):
    bullets.update()
    # Delete the old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def create_fleet(screen_settings, screen, aliens):
    alien = Alien(screen_settings, screen)
    alien_width = alien.rect.width
    available_space_x = screen_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

     # Create the first row of aliens
    for alien_number in range(number_aliens_x):
         # Create an alien and place it in the row
        alien = Alien(screen_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)



    alien.draw_alien()
    pygame.display.flip()
