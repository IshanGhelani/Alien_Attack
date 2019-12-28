import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        """# Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top"""

        # Load the bullet image and get its rect.
        self.image = pygame.image.load('images/1234.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.y -= self.speed_factor

        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
