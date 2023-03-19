import pygame
from constans import *
from main import screen


class Hero:
    def __init__(self, x_pos, y_pos, height, width):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.img = pygame.image.load('img/girl.jpg')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def display_hero(self):
        screen.blit(self.img, (self.x_pos, self.y_pos))



