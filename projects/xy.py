from nextdraw import NextDraw


def create_xy(plotter: NextDraw, origin_x, origin_y, height, width):
    print(
        f"""
    Creating XY
    Origin: [{origin_x}, {origin_y}]
    Height: {height}
    Width: {width}
    """
    )
    # draw x axis
    plotter.penup()
    x_axis_x_start = origin_x - (width / 2)
    x_axis_y_start = origin_y
    plotter.moveto(x_axis_x_start, x_axis_y_start)
    plotter.pendown()
    x_axis_x_end = origin_x + (width / 2)
    x_axis_y_end = origin_y
    plotter.lineto(x_axis_x_end, x_axis_y_end)

    # draw y axis
    plotter.penup()
    y_axis_x_start = origin_x
    y_axis_y_start = origin_y - (height / 2)
    plotter.moveto(y_axis_x_start, y_axis_y_start)
    plotter.pendown()
    y_axis_x_end = origin_x
    y_axis_y_end = origin_y + (height / 2)
    plotter.lineto(y_axis_x_end, y_axis_y_end)
    plotter.penup()
