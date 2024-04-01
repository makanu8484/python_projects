import pygame

class Ship():

    def __init__(self, screen_settings, screen):
        self.screen = screen
        self.screen_settings = screen_settings

        #Load the image of the ship"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position the ship at bottom center of the screen

        self.rect.centerx= self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship center
        self.center = float(self.rect.centerx)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position based on the movement flag."""
        # update the ship center value,
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.screen_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.screen_settings.ship_speed_factor


        # Update rec object from self.center.
        self.rect.centerx = self.center



    def draw_location(self):
        self.screen.blit(self.image, self.rect)


