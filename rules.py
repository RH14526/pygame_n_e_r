from helpers import *


def rules():
    pygame.display.set_caption("RULES")
    while True:
        menu_back = pygame.image.load(MENU_BACK).convert()
        menu_back = pygame.transform.scale(menu_back, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(menu_back, (0, 0))
        RULES_BK = 'img/RULES_BK/rules_bk.png'
        rules_bk = pygame.image.load(RULES_BK).convert()
        rules_bk = pygame.transform.scale(rules_bk, (RULES_WIDTH, RULES_HEIGHT))
        screen.blit(rules_bk, (RULES_X_POSITION, RULES_Y_POSITION))
        menu_mouse_pos = pygame.mouse.get_pos()

