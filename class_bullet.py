import pygame
from constants import *


class Bullet(pygame.sprite.Sprite):
    """Class representing the bullet that the ship shoots."""

    def __init__(self, x: float, y: float) -> None:
        """Create a bullet.

        Args:
            x coordinate, y coordinate.

        Returns:
            None
        """
        pygame.sprite.Sprite.__init__(self)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self) -> None:
        """Updates bullet position adding y-axes speed.

        Args:
            None

        Returns:
            None
        """
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
