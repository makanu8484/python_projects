import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen_settings, screen, ship):
        # Create the bullet at ship current position
        super(Bullet, self).__init__()
        self.screen = screen


        # Create a bullet rect at (0, 0)
        self.rect = pygame.Rect(0, 0, screen_settings.bullet_width, screen_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet position
        self.y = float(self.rect.y)

        self.color = screen_settings.bullet_color
        self.speed = screen_settings.bullet_speed


    def update(self):
        # Move the bullet up
        # Update th e position of the bullet
        self.y -= self.speed

        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)