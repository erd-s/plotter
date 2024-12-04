import random
import math

from nextdraw import NextDraw
from xy import create_xy
from utils import center_y, center_x

RADIUS_MIN = 1
RADIUS_MAX = 1.5


def create_burst(plotter: NextDraw, number_of_lines):
    print(f"number of lines: {number_of_lines}")

    # baselines
    create_xy(plotter=plotter, max_x=RADIUS_MAX, max_y=RADIUS_MAX)

    # quadrant I
    for i in range(int(number_of_lines / 4)):
        try:
            radius = RADIUS_MAX
            coefficient = radius / ((number_of_lines / 4) + 1)
            x = coefficient * (i + 1)
            y = math.sqrt(abs((radius * radius) - (x * x)))
            print(f"[{center_x()}, {center_y()}] ==> delta [{x}, {y}])")
            plotter.moveto(center_x(), center_y())
            plotter.pendown()
            plotter.line(x, y)
            plotter.penup()
        except Exception as e:
            print(e)

    # x_mult = 1 if i < number_of_lines / 2 else -1
    # y_mult = 1 if not (0.25 * number_of_lines) <= i < (0.75 * number_of_lines) else -1
    # # radius = random.uniform(RANDOM_MIN, RANDOM_MAX)
    # radius = 1.5
    # x = coefficient * i * x_mult
    # y = math.sqrt(abs((radius * radius) - (x * x))) * y_mult
