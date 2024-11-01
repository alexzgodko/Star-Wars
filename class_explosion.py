import pygame
from constants import *


class Explosion(pygame.sprite.Sprite):
    """Class representing an animation of explosion when the bullet collides with the meteor."""

    def __init__(self, center, size, explosion_anim):
        """Create the explosion.

        Args:
            center: Position of the explosion center
            size: lg - for collision of the bullet with the meteor
                  sm - for collision of the spaceship with the meteor
            explosion_anim: Array with pictures for explosion animation

        Returns:
            None
        """
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        pass  # implementation is in main
