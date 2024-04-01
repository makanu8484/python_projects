import pygame
from pygame.sprite import Group
from settings_game import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    """Create a screen object, start de game"""
    pygame.init()
    screen_settings = Settings()
    screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    """Make a ship"""
    ship = Ship(screen_settings, screen)

    # Make a group to store bullet in.
    bullets = Group()
    aliens = Group()

    """Make the screen visible"""
    screen.fill(screen_settings.background_color)
    ship.draw_location()
    # Make the most recently drawn screen visible.
    pygame.display.flip()
    # Make an alien
    aliens = Alien(screen_settings, screen)
    # Create a fleet of aliens
    gf.create_fleet(screen_settings, screen, aliens)

    while True:
        gf.check_events(screen_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(screen_settings, screen, ship, aliens, bullets)


run_game()
