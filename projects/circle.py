from nextdraw import NextDraw
import math


def create_circle(
    plotter: NextDraw,
    origin_x: float,
    origin_y: float,
    radius: float,
    steps: int,
    offset_x: float = 0,
    offset_y: float = 0,
):
    path_points = []

    print(
        f"""
    Drawing Circle
    Origin: {origin_x}, {origin_y}
    Radius: {radius}
    Steps: {steps}
    """
    )

    # quadrant I
    print("\nQuadrant I")
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = math.sqrt((radius * radius) - (x * x))
        path_points.append([x + origin_x + offset_x, y + origin_y + offset_y])
        print(f"[{x + origin_x + offset_x}, {y + origin_y + offset_y}]")

    # quadrant II
    print("\nQuadrant II")
    x_list = []
    y_list = []
    for i in range(steps + 1):
        x = path_points[i][0]
        x_length = (radius / steps) * i
        y = origin_y - math.sqrt((radius * radius) - (x_length * x_length)) + offset_y
        x_list.insert(0, x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        print(f"[{x}, {y}]")
        path_points.append([x, y])

    # quadrant III
    print("\nQuadrant III")
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = origin_y - math.sqrt((radius * radius) - (x * x)) + offset_y
        path_points.append([origin_x - x + offset_x, y])
        print(f"[{origin_x - x - radius}, {y}]")

    #
    # quadrant IV
    print("\nQuadrant IV")
    x_list = []
    y_list = []
    reversed_plot_points = list(reversed(path_points))
    for i in range(steps + 1):
        x = reversed_plot_points[i][0]
        y = path_points[i][1]
        x_list.append(x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        print(f"[{x}, {y}]")
        path_points.append([x, y])

    plotter.draw_path(path_points)
