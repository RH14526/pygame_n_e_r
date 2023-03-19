import pygame
from constans import *
from main import screen


def add_img(img_path, img_width, img_height, img_y_pos, img_x_pos):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (img_width, img_height))
    screen.blit(img, (img_x_pos, img_y_pos))


