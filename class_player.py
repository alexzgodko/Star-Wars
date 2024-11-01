import pygame
from constants import *


class Player(pygame.sprite.Sprite):
    """Class representing a spaceship in the bottom of the screen."""

    def __init__(self):
        """Create a ship in the center at the bottom of the screen. 
           It can move left to right of the screen and shoot bullets at asteroids.

        Args:
            None

        Returns:
            None        
        """

        pygame.sprite.Sprite.__init__(self)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100
        self.last_update = pygame.time.get_ticks()

    def update(self):
        """Updates the asteroid's x-position depending on which key is pressed.

        Args:
            None

        Returns:
            None
        """

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        pass  # implementatin is in main
