import pygame
from constans import *


class Wall:

    def __init__(self, image_path, wall_width, x_position_w, y_position_w, wall_hieght):
        self.image_path = 'img/wall.jpg'
        self.wall_width = wall_width
        self.x_position_w = x_position_w
        self.y_position_w = y_position_w
        self.wall_height = wall_hieght

