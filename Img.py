import pygame
from constans import *
global screen
from helpers import *


class Img:

    def __init__(self, img_width, x_position, y_position, img_hieght, image_path):
        self.image_path = image_path
        self.img_width = img_width
        self.x_position = x_position
        self.y_position = y_position
        self.img_height = img_hieght

    def get_image_path(self):
        return self.image_path

    def show(self):
        img = pygame.image.load(self.image_path)
        img = pygame.transform.scale(img, (self.img_width, self.img_height))
        screen.blit(img, (self.x_position, self.y_position))

    def get_rect(self):
        return pygame.Rect(self.x_position, self.y_position, self.img_width, self.img_height)
