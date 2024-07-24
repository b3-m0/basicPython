import pygame
from pygame.locals import RLEACCEL
import time
import random
from player import (
    Player,
    WIDTH,
    HEIGHT
)
from enemies import Star


pygame.font.init()
pygame.init()


#declare variables
STAR_VEL = 5


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale_by(pygame.image.load("spaceBG.jpg"), 2.2)

FONT = pygame.font.SysFont("mononoki", 30)




#DECLARE FUNCTIONS >.<
def draw(elapsed_time, stars):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white") # {} is to directly use the variable, 1 means anti-aliasing
    WIN.blit(time_text, (10,10))

    #where to draw rect, color, label the rect we want to draw
    WIN.blit(player.surf, player.rect)
    
    for star in stars:
        WIN.blit(star.surf, star.rect)
   

    pygame.display.update()  



#instantiate player
player = Player()


#main function
def main():
    run = True

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    tenclock = pygame.time.Clock()

    star_add_increment = 5000 #ms
    star_count = 0 #count til 2000...when to add the next star

    stars = [] #create empty list of enemies
    hit = False

    #ADD here: background music


    while run:
        star_count += clock.tick(60) #fps value, run max 60 times per second, return # of ms since last clock.tick
        elapsed_time = time.time() - start_time #current time - start time

        if star_count > star_add_increment:
            for _ in range(3):
                star = Star()
                stars.append(star) #add more stars...total of 3

                star_count = 0

            if tenclock.tick(10):
                star_add_increment = max(2000, star_add_increment - 5)
                star_count = 0 # reset star count
            #ADD HERE: "level up" text/animation
            #ADD HERE: if statement...if star_add_increment == 2000, then "win game" and unlimited game begins
            #EDIT THIS: every 5 seconds, after 10 seconds has passed then subtract 5, etc etc until every 1 second


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #ADD here: are you sure you want to quit game?
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    #ADD here: pause menu: quit, resume, menu
                    break

        #gives dictionary of keys pressed by user
        keys = pygame.key.get_pressed()
        player.update(keys)


        #delete passed stars or stars that hit Player
        for star in stars[:]:
            star.rect.y += STAR_VEL
            if star.rect.y > HEIGHT:
                stars.remove(star)
            elif star.rect.y + star.rect.height >= player.rect.y and star.rect.colliderect(player.rect):
                stars.remove(star)
                hit = True
                break

        if hit:
            #ADD HERE: take to a new screen with -level acheived -you win or lost (if acheived all levels)
            lost_text = FONT.render("You Lost", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        
        draw(elapsed_time, stars)
        
    
    pygame.quit()

#call main function
if __name__ == "__main__":
    main()