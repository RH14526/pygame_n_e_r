import random
from constans import *


def extreme(x_position_item, y_position_item, item_width, item_height, x_position_item2, y_position_item2):
    while x_position_item == x_position_item2 and y_position_item == y_position_item2:
        x_position_item = random.randint(0, WINDOW_WIDTH - item_width)
        y_position_item = random.randint(0, WINDOW_HEIGHT - item_height)
    return [x_position_item, y_position_item]

