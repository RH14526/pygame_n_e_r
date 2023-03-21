import pygame
from constans import *
from helpers import *


class Hero:
    def __init__(self, x_pos, y_pos, height, width):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.img = pygame.image.load(girl)
        img_aspect_ratio = self.img.get_width() / self.img.get_height()
        if img_aspect_ratio > 1:
            self.width = int(self.height * img_aspect_ratio)
        else:
            self.height = int(self.width / img_aspect_ratio)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def display_hero(self):
        screen.blit(self.img, (self.x_pos, self.y_pos))

    def move_hero(self, button):
        pass

