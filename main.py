import random

import pygame
from constans import *
from helpers import *

from Img import *
from display import *

clock = pygame.time.Clock()
pfs = 60


def main():
    wall_1 = Wall(666, 300, 70, 70)
    bg = pygame.image.load(BG).convert()
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    from classes.hero import Hero
    hero_x = HERO_START_X
    hero_y = HERO_Y_START
    pygame.init()
    finish = False
    scroll = 5
    tile = pygame.image.load('img/back/9ba6409e-1370-455f-b50d-2a8d120fdfff.jpg').convert()
    tile = pygame.transform.scale(tile, (WINDOW_WIDTH, WINDOW_HEIGHT))
    b_pos = 0
    t_pos = -WINDOW_HEIGHT
    walls = []
    while not finish:
        if b_pos >= WINDOW_HEIGHT:
            b_pos = -WINDOW_HEIGHT

        if t_pos >= WINDOW_HEIGHT:
            t_pos = -WINDOW_HEIGHT
        b_pos += scroll
        t_pos += scroll
        screen.blit(bg, (0, b_pos))
        screen.blit(tile, (0, t_pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero_x > 0:
            hero_x -= 5
        if keys[pygame.K_RIGHT] and hero_x < WINDOW_WIDTH - HERO_WIDTH:
            hero_x += 5
        if keys[pygame.K_UP] and hero_y > 0:
            hero_y -= 5
        if keys[pygame.K_DOWN] and hero_y < WINDOW_HEIGHT - HERO_HEIGHT:
            hero_y += 5

        # Generate new walls as needed
        if len(walls) == 0 or walls[-1].y_position_w > 100:
            wall_width = random.randint(MIN_WALL_WIDTH, MAX_WALL_WIDTH)
            wall_height = random.randint(MIN_WALL_HEIGHT, MAX_WALL_HEIGHT)
            wall_x = random.randint(0, WINDOW_WIDTH - wall_width)
            wall_y = -wall_height / 2
            walls.append(Wall(wall_width, wall_x, wall_y, wall_height))

        # Move and draw the walls
        for wall in walls:
            wall.y_position_w += scroll
            wall.show()
            if wall.y_position_w > WINDOW_HEIGHT:
                walls.remove(wall)

        my_hero = Hero(hero_x, hero_y, HERO_HEIGHT, HERO_WIDTH)
        my_hero.display_hero()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
