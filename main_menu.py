import sys
import pygame
from constans import *
from Buttens import *
from play import *
from helpers import *
from rules import *


def main_menu():
    pygame.font.init()
    pygame.display.set_caption('menu')

    while True:
        menu_back = pygame.image.load(MENU_BACK).convert()
        menu_back = pygame.transform.scale(menu_back, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(menu_back, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_font = pygame.font.SysFont("Aharoni", 100)
        menu_text = menu_font.render("MENU", True, BABY_PINK)
        menu_rect = menu_text.get_rect(center=(500, WINDOW_HEIGHT / 6))
        extra_font = pygame.font.SysFont("Aharoni", 110)
        extra_menu_text = extra_font.render("MENU", True, PINK)
        extra_menu_rect = extra_menu_text.get_rect(center=(500, WINDOW_HEIGHT / 6))

        play_font = pygame.font.SysFont("Aharoni", 40)
        play_button = Button(TEMP_BUTTON, BUTTON_POS, "PLAY", play_font, PURPLE, BABY_PINK)

        wardrobe_font = pygame.font.SysFont("Aharoni", 40)
        wardrobe_button = Button(TEMP_BUTTON, (BUTTON_POS[0], BUTTON_POS[1] + 130), "WARDROBE", wardrobe_font, PURPLE, BABY_PINK)

        rules_font = pygame.font.SysFont("Aharoni", 40)
        rules_button = Button(TEMP_BUTTON, (BUTTON_POS[0], BUTTON_POS[1] + 260), "RULES", rules_font, PURPLE, BABY_PINK)

        screen.blit(extra_menu_text, extra_menu_rect)
        screen.blit(menu_text, menu_rect)

        for button in [play_button, wardrobe_button, rules_button]:
            button.change_color(menu_mouse_pos)
            button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_mouse(menu_mouse_pos):
                    main()
                if wardrobe_button.check_for_mouse(menu_mouse_pos):
                    pass
                if rules_button.check_for_mouse(menu_mouse_pos):
                    rules()

        pygame.display.update()


main_menu()
