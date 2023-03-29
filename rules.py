from helpers import *

def rules():
    pygame.display.set_caption("RULES")

    while True:
        menu_back = pygame.image.load(MENU_BACK).convert()
        menu_back = pygame.transform.scale(menu_back, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(menu_back, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

