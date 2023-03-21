import pygame
from constans import *
from helpers import *


def main():
    from classes.hero import Hero

    my_hero = Hero(HERO_START_X, HERO_Y_START, HERO_HEIGHT, HERO_WIDTH)
    pygame.init()
    finish = False
    while not finish:
        screen.fill(SCREEN_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                pass
        my_hero.display_hero()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
