import pygame
from constans import *
from display import *


class Wall:

    def __init__(self, img_width, x_position, y_position, img_hieght, image_path):
        self.image_path = image_path
        self.img_width = wall_width
        self.x_position = x_position_w
        self.y_position = y_position_w
        self.img_height = wall_hieght

    def get_image_path(self):
        return self.image_path

    def show(self):
        img = pygame.image.load(self.image_path)
        img = pygame.transform.scale(img, (self.wall_width, self.wall_height))
        screen.blit(img, (self.x_position_w, self.y_position_w))

    def get_rect(self):
        return pygame.Rect(self.x_position_w, self.y_position_w, self.wall_width, self.wall_height)

