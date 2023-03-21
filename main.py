import pygame
from constans import *
from helpers import *


def main():
    from classes.hero import Hero
    hero_x = HERO_START_X
    hero_y = HERO_Y_START
    pygame.init()
    finish = False
    while not finish:
        screen.fill(SCREEN_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero_x > 0:
            hero_x -= 5
        if keys[pygame.K_RIGHT] and hero_x > 0:
            hero_x += 5
        if keys[pygame.K_UP] and hero_x > 0:
            hero_y -= 5
        if keys[pygame.K_DOWN] and hero_x > 0:
            hero_y += 5
        my_hero = Hero(hero_x, hero_y, HERO_HEIGHT, HERO_WIDTH)
        my_hero.display_hero()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
