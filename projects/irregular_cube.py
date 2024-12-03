import random

from nextdraw import NextDraw
from utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_x_end,
    effective_y_start,
    effective_y_end,
    center_x,
    center_y,
)


def create_cube(plotter: NextDraw, origin_x: float, origin_y: float, width: float):
    # vertices
    start_x_one = random.uniform(0.5, 1) * width * -1
    start_y_one = random.uniform(0, 0.5) * width
    point_one = [start_x_one + origin_x, start_y_one + origin_y]

    start_x_two = random.uniform(0.5, 1) * width * -1
    start_y_two = random.uniform(0, 0.5) * width * -1
    point_two = [start_x_two + origin_x, start_y_two + origin_y]

    start_x_three = random.uniform(0, 0.5) * width * -1
    start_y_three = random.uniform(0.5, 1) * width
    point_three = [start_x_three + origin_x, start_y_three + origin_y]

    start_x_four = random.uniform(0, 0.5) * width * -1
    start_y_four = random.uniform(0.5, 1) * width * -1
    point_four = [start_x_four + origin_x, start_y_four + origin_y]

    start_x_five = random.uniform(0, 0.5) * width
    start_y_five = random.uniform(0, 0.5) * width
    point_five = [start_x_five + origin_x, start_y_five + origin_y]

    start_x_six = random.uniform(0, 0.5) * width
    start_y_six = random.uniform(0, 0.5) * width * -1
    point_six = [start_x_six + origin_x, start_y_six + origin_y]

    start_x_seven = random.uniform(0.5, 1) * width
    start_y_seven = random.uniform(0.5, 1) * width
    point_seven = [start_x_seven + origin_x, start_y_seven + origin_y]

    start_x_eight = random.uniform(0.5, 1) * width
    start_y_eight = random.uniform(0.5, 1) * width * -1
    point_eight = [start_x_eight + origin_x, start_y_eight + origin_y]

    # vertical lines
    plotter.moveto(point_one[0], point_one[1])
    plotter.pendown()
    plotter.lineto(point_two[0], point_two[1])
    plotter.penup()

    plotter.moveto(point_three[0], point_three[1])
    plotter.pendown()
    plotter.lineto(point_four[0], point_four[1])
    plotter.penup()

    plotter.moveto(point_five[0], point_five[1])
    plotter.pendown()
    plotter.lineto(point_six[0], point_six[1])
    plotter.penup()

    plotter.moveto(point_seven[0], point_seven[1])
    plotter.pendown()
    plotter.lineto(point_eight[0], point_eight[1])
    plotter.penup()

    # connect vertices
    plotter.moveto(point_one[0], point_one[1])
    plotter.pendown()
    plotter.lineto(point_three[0], point_three[1])
    plotter.penup()

    plotter.moveto(point_three[0], point_three[1])
    plotter.pendown()
    plotter.lineto(point_seven[0], point_seven[1])
    plotter.penup()

    plotter.moveto(point_one[0], point_one[1])
    plotter.pendown()
    plotter.lineto(point_five[0], point_five[1])
    plotter.penup()

    plotter.moveto(point_five[0], point_five[1])
    plotter.pendown()
    plotter.lineto(point_seven[0], point_seven[1])
    plotter.penup()

    plotter.moveto(point_two[0], point_two[1])
    plotter.pendown()
    plotter.lineto(point_four[0], point_four[1])
    plotter.penup()

    plotter.moveto(point_four[0], point_four[1])
    plotter.pendown()
    plotter.lineto(point_eight[0], point_eight[1])
    plotter.penup()

    plotter.moveto(point_two[0], point_two[1])
    plotter.pendown()
    plotter.lineto(point_six[0], point_six[1])
    plotter.penup()

    plotter.moveto(point_six[0], point_six[1])
    plotter.pendown()
    plotter.lineto(point_eight[0], point_eight[1])
    plotter.penup()
