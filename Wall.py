import pygame
from constans import *
from display import *


class Wall:

    def __init__(self, wall_width, x_position_w, y_position_w, wall_hieght):
        self.image_path = 'img/wall/wall.png'
        self.wall_width = wall_width
        self.x_position_w = x_position_w
        self.y_position_w = y_position_w
        self.wall_height = wall_hieght

    def get_image_path(self):
        return self.image_path

    def show(self):
        img = pygame.image.load(self.image_path)
        img = pygame.transform.scale(img, (self.wall_width, self.wall_height))
        screen.blit(img, (self.x_position_w, self.y_position_w))

