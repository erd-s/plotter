import random

from nextdraw import NextDraw
from utils import center_y, center_x

RANDOM_MIN = -1.75
RANDOM_MAX = 1.75


def create_burst(plotter: NextDraw, number_of_lines):
    x = center_x()
    y = center_y()

    for i in range(number_of_lines):
        plotter.goto(x, y)
        plotter.pendown()
        dest_x = x - (random.uniform(RANDOM_MIN*1000, RANDOM_MAX*1000) / 1000)
        dest_y = y - (random.uniform(RANDOM_MIN*1000, RANDOM_MAX*1000) / 1000)
        plotter.lineto(dest_x, dest_y)
        plotter.penup()
        print(f'{i+1}/{number_of_lines}')
