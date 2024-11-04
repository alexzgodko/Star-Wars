import pygame
from constants import *
from typing import Literal
import vars


class Explosion(pygame.sprite.Sprite):
    """Class representing an animation of explosion when the bullet collides with the meteor."""

    def __init__(self, center: float, size: Literal['lg', 'sm'], explosion_anim: dict) -> None:
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

    def update(self) -> None:
        """Displays animation frames sequentially based on elapsed time.

        Args:
            None

        Returns:
            None
        """

        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(vars.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = vars.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
