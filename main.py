import pygame

from classes.Hero import *
from constans import *


global screen

hero = (HERO_START_X, HERO_Y_START, HERO_HEIGHT, HERO_WIDTH)


def main():
    pygame.init()
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    finish = False
    while not finish:
        screen.fill(SCREEN_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        hero.display_hero()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
