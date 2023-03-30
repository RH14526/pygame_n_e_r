from helpers import *
import textwrap
import pygame
from Buttens import *


def rules():
    pygame.mixer.init()
    pygame.display.init()
    pygame.display.set_caption("RULES")
    from main_menu import main_menu
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sound = pygame.mixer.Sound('sounds/back_butten.wav')
                pygame.mixer.Sound.play(sound)
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back_button.check_for_mouse(mouse):
                    sound = pygame.mixer.Sound('sounds/back_butten.wav')
                    pygame.mixer.Sound.play(sound)
                    main_menu()
        menu_back = pygame.image.load(MENU_BACK).convert()
        menu_back = pygame.transform.scale(menu_back, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(menu_back, (0, 0))
        RULES_BK = 'img/rules_bk/rules.png'
        rules_bk = pygame.image.load(RULES_BK).convert()
        rules_bk = pygame.transform.scale(rules_bk, (RULES_WIDTH, RULES_HEIGHT))
        screen.blit(rules_bk, (RULES_X_POSITION, RULES_Y_POSITION))
        go_back_button = pygame.image.load('img/go_back_b/go_back_b.png')
        back_font = pygame.font.SysFont("Aharoni", 40)
        go_back_button = Button(go_back_button, (60, 40), " ", back_font, PURPLE, BABY_PINK)
        go_back_button.update()
        massage = "WELCOME TO FASHION CRAZY!" \
                  " In this incredible fashion race game you can buy cool clothes for your game character with coins, which you can get buy claming them while avoiding the obstclys." \
                  "You have 3 harts at the begging of the game, but you lose 1 everytime that you touch the obstacle." \
                  "Be ready, and lets go FASHION FRENZY!"
        lines = textwrap.wrap(massage, width=50)
        for i, line in enumerate(lines):
            font = pygame.font.SysFont("Georgia", 25)
            text = font.render(line, True, PURPLE)
            line_x_pos = X_Y_TEXT[0]
            line_y_pos = X_Y_TEXT[1] + i * 30
            screen.blit(text, (line_x_pos, line_y_pos))

        cap_font = pygame.font.SysFont("Georgia", 50)
        cap_text = cap_font.render("RULES", True, Black)
        screen.blit(cap_text, (410, 140))

        pygame.display.update()


