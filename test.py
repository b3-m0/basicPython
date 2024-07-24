import pygame
from pygame import RLEACCEL
pygame.init()

#declare variables
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test", "#1")


pic = pygame.image.load("starPixel.png").convert_alpha()

# Manually adjust the alpha channel
width, height = pic.get_size()
for x in range(width):
    for y in range(height):
        if pic.get_at((x, y)) == (247, 247, 247,255):
            pic.set_at((x, y), (247,247,247,0))

#debug: print color value at top left corner
print(pic.get_at((20,20)))


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break
        
        WIN.fill((255,0,0))
        WIN.blit(pic, (0,0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

