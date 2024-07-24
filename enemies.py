import pygame
from player import WIDTH, HEIGHT
import random


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.surf = pygame.transform.scale_by((pygame.image.load("starPixel.png").convert_alpha()), 0.05)
        
        #transparent background
        STAR_WIDTH, STAR_HEIGHT = self.surf.get_size()
        for x in range(STAR_WIDTH):
            for y in range(STAR_HEIGHT):
                if self.surf.get_at((x, y)) == (247, 247, 247, 255):
                    self.surf.set_at((x, y), (247,247,247,0))
                elif self.surf.get_at((x,y)) == (246, 246, 246, 255):
                    self.surf.set_at((x,y), (246, 246, 246, 0))
        
        self.rect = self.surf.get_rect()
        self.rect.x = random.randint(0, WIDTH - STAR_WIDTH)
        self.rect.y = -STAR_HEIGHT
    