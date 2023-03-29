import random

import pygame
from constans import *
from helpers import *
from Buttens import *
from Img import *

clock = pygame.time.Clock()
pfs = 60


def main():
    from main_menu import main_menu
    bg = pygame.image.load(BG).convert()
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    from classes.hero import Hero
    hero_x = HERO_START_X
    hero_y = HERO_Y_START
    pygame.init()
    finish = False
    hero_scroll = 7
    scroll = 5
    tile = pygame.image.load('img/back/9ba6409e-1370-455f-b50d-2a8d120fdfff.jpg').convert()
    tile = pygame.transform.scale(tile, (WINDOW_WIDTH, WINDOW_HEIGHT))
    b_pos = 0
    t_pos = -WINDOW_HEIGHT
    walls = []
    hearts = 3
    score = 0
    coins = []
    last_collidion = -1
    while not finish:
        # go_back_button = pygame.image.load('img/quit/עותק של ללא כותרת (4).png')
        # go_back_button = pygame.transform.scale(go_back_button, (5, 5))
        # back_font = pygame.font.SysFont("Aharoni", 20)
        # back_button = Button(go_back_button, (100, 400), " ", back_font, PURPLE, BABY_PINK)
        # mouse = pygame.mouse.get_pos()

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
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if back_button.check_for_mouse(mouse):
            #         main_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero_x > 0:
            hero_x -= hero_scroll
        if keys[pygame.K_RIGHT] and hero_x < WINDOW_WIDTH - HERO_WIDTH:
            hero_x += hero_scroll
        if keys[pygame.K_UP] and hero_y > 0:
            hero_y -= hero_scroll
        if keys[pygame.K_DOWN] and hero_y < WINDOW_HEIGHT - HERO_HEIGHT:
            hero_y += hero_scroll

        # Generate new walls as needed
        if len(walls) == 0 or walls[-1].y_position > 100:
            wall_width = random.randint(MIN_WALL_WIDTH, MAX_WALL_WIDTH)
            wall_height = random.randint(MIN_WALL_HEIGHT, MAX_WALL_HEIGHT)
            wall_x = random.randint(0, WINDOW_WIDTH - wall_width)
            wall_y = -wall_height - random.randint(50, 100)
            walls.append(Img(wall_width, wall_x, wall_y, wall_height, WALL))

        # Move and draw the walls
        for wall in walls:
            wall.y_position += scroll
            wall.show()
            if wall.y_position > WINDOW_HEIGHT:
                walls.remove(wall)

        my_hero = Hero(hero_x, hero_y, HERO_HEIGHT, HERO_WIDTH)

        # back_button.update()

        list_of_rects = [b.get_rect() for b in walls]

        for i in range(hearts):
            heart_img = 'img/hearts/heart.png'
            heart = Img(40, 800 + 50 * i, 80, 40, heart_img)
            heart.show()



        rect_index = my_hero.get_rect().collidelist(list_of_rects)
        if last_collidion == -1 and rect_index != -1:
            hearts -= 1
        last_collidion = rect_index





        my_hero.display_hero()

        if hearts == 0:
            print("jshvgdjasg")
            pygame.time.wait(1000)
            print("after_wait")
            end_font = pygame.font.SysFont("Aharoni", 100)
            end_text = end_font.render("GAME_OVER", True, BABY_PINK)
            end_text_rect = end_text.get_rect(center=(500, WINDOW_HEIGHT / 6))
            screen.blit(end_text, end_text_rect)
            pygame.time.wait(3000)
            finish = True

        pygame.display.flip()

    main_menu()


if __name__ == "__main__":
    main()
