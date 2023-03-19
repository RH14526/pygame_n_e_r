import pygame
from constans import *

class Car:

    def __init__(self, car_width, x_position_c, y_position_c, car_hieght):
        self.image_path = 'img/car.jpg'
        self.car_width = car_width
        self.x_position_c = x_position_c
        self.y_position_c = y_position_c
        self.car_hieght = car_hieght

