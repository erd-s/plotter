import math

from utils.plotter_interface import PlotterInterface


def draw_burst(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    radius: float,
    lines_per_quadrant: int,
):
    path_points = []

    print(
        f"""
    Drawing Burst
    Origin: {origin_x}, {origin_y}
    Radius: {radius}
    Lines Per Quadrant: {lines_per_quadrant}
    """
    )

    # quadrant I
    for i in range(lines_per_quadrant):
        x = (radius / lines_per_quadrant) * i
        y = math.sqrt(abs((radius * radius) - (x * x)))
        path_points.append([x + origin_x, y + origin_y])

    # quadrant II
    x_list = []
    y_list = []
    for i in range(lines_per_quadrant):
        x = path_points[i][0]
        x_length = (radius / lines_per_quadrant) * i
        y = origin_y - math.sqrt(abs((radius * radius) - (x_length * x_length)))

        x_list.insert(0, x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        path_points.append([x, y])

    # quadrant III
    for i in range(lines_per_quadrant):
        x = (radius / lines_per_quadrant) * i
        y = origin_y - math.sqrt(abs((radius * radius) - (x * x)))
        path_points.append([origin_x - x, y])

    # quadrant IV
    x_list = []
    y_list = []
    reversed_plot_points = list(reversed(path_points))
    for i in range(lines_per_quadrant):
        x = reversed_plot_points[i][0]
        y = path_points[i][1]
        x_list.append(x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        path_points.append([x, y])

    # remove duplicate points:
    path_points_uniques = []
    path_points_uniques = [
        point for point in path_points if point not in path_points_uniques
    ]
    for point in path_points_uniques:
        x = point[0]
        y = point[1]

        plotter.moveto(x, y)
        plotter.pendown()
        plotter.lineto(origin_x, origin_y)
        plotter.penup()
