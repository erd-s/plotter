from nextdraw import NextDraw


def create_xy(plotter: NextDraw, origin_x, origin_y, height, width):
    plotter.penup()
    plotter.moveto(origin_x - width, origin_y)
    plotter.pendown()
    plotter.line(width, 0)
    plotter.penup()
    plotter.moveto(origin_x, origin_y - height)
    plotter.pendown()
    plotter.line(0, height)
    plotter.penup()
