import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #A class to represent a single alien
    def __init__(self, screen_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.screen_settings = screen_settings


        #Load de alian image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Start new alien from the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        # Store th eelien
        self.x = float(self.rect.x)

    def draw_alien(self):
        """Draw the alien at its current location"""

        self.screen.blit(self.image, self.rect)