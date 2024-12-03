from nextdraw import NextDraw
from utils import center_x, center_y


def create_xy(plotter: NextDraw, max_x, max_y):
    plotter.penup()
    plotter.moveto(center_x() - max_x, center_y())
    plotter.pendown()
    plotter.line(max_x * 2, 0)
    plotter.penup()
    plotter.moveto(center_x(), center_y() - max_y)
    plotter.pendown()
    plotter.line(0, max_y * 2)
    plotter.penup()
