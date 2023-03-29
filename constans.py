################## game #######################
import pygame.font

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650
SCREEN_COLOR = (154, 205, 50)
HERO_START_X = 450
HERO_Y_START = 490
HERO_WIDTH = 40
HERO_HEIGHT = 40
girl = 'img/girl/girl.png'
BG = 'img/back/9ba6409e-1370-455f-b50d-2a8d120fdfff.jpg'
BG_HEIGHT = 326
WALL_Y_START = 0
MAX_WALL_WIDTH = 400
MIN_WALL_WIDTH = 100
MAX_WALL_HEIGHT = 100
MIN_WALL_HEIGHT = 50
WALL = 'img/wall/wall.png'
MIN_WALL_X = 0
MIN_WALL_Y = 0

##################### closet ##############################

SHORTS = 'img/girl_clothes/3.png'
TOP = 'img/girl_clothes/4.png'
TOP_CLOTHERS_X_START = HERO_START_X
TOP_WIDTH = HERO_WIDTH
TOP_HEIGHT = HERO_HEIGHT / 2
TOP_CLOTHERS_Y_START = HERO_Y_START + TOP_HEIGHT + 17
BOTTOM_X = HERO_START_X
BOTTOB_WIDTH = HERO_WIDTH
BOTTOM_HEIGHT = HERO_HEIGHT / 2
BOTTOM_Y = HERO_Y_START + (BOTTOM_HEIGHT * 2) + 15
COIN = 'img/coins/עותק של ללא כותרת (3).png'
#############menu#######################################

MENU_BACK = 'img/manu_back/happy-father-s-day-celebration-wooden-background-with-various-accessories_1302-4596.jpg'
TEMP_BUTTON = pygame.image.load('img/play/עיצוב ללא שם.png')
PURPLE = (128, 0, 128)
WHITE = (250, 240, 240)
BABY_PINK = (255, 193, 203)
PINK = (255, 105, 180)
MENU_FONT = 'Aharoni'
BUTTON_FONT_SIZE = 40
MENU_FONT_SIZE = 70
BUTTONS_SIZE = (400, 125)
BUTTON_POS = (500, 280)
MENU_POS = (500, WINDOW_HEIGHT / 6)
RULES_X_POSITION = 150
RULES_WIDTH = 700
RULES_Y_POSITION = 90
RULES_HEIGHT = 500
X_Y_TEXT = [225, 250]
Black = (0, 0, 0)
