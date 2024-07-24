import pygame
from pygame import RLEACCEL


PLAYER_VEL = 5

WIDTH, HEIGHT = 1000, 800



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.transform.scale_by((pygame.image.load("rocket3.png").convert_alpha()), 0.3)
        
        #transparent background
        PLAYER_WIDTH, PLAYER_HEIGHT = self.surf.get_size()
        for x in range(PLAYER_WIDTH):
            for y in range(PLAYER_HEIGHT):
                if self.surf.get_at((x, y)) == (1, 1, 1, 255):
                    self.surf.set_at((x, y), (1,1,1,0))
        
        self.rect = self.surf.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.bottom = HEIGHT / 2


    def update(self, keys):
        #change x position
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_VEL, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_VEL, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -PLAYER_VEL)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, PLAYER_VEL)
        
        #keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

#add here: flames shooting from behind
#add here: animation of rocket moving