from nextdraw import NextDraw
import math


def create_circle(
    plotter: NextDraw, origin_x: float, origin_y: float, radius: float, steps: int
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
    print('\nQuadrant I')
    for i in range(steps + 1):
        x = ((radius / steps) * i)
        y = (math.sqrt((radius * radius) - (x * x)))
        path_points.append([x + origin_x - radius, y + origin_y - radius])
        print(f'[{x + origin_x - radius}, {y + origin_y - radius}]')


    # quadrant II
    print('\nQuadrant II')
    x_list = []
    y_list = []
    for i in range(steps + 1):
        x = path_points[i][0]
        x_length = (radius / steps) * i
        y = origin_y - math.sqrt((radius * radius) - (x_length * x_length)) - radius
        x_list.insert(0, x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        print(f'[{x}, {y}]')
        path_points.append([x, y])

    # quadrant III
    print('\nQuadrant III')
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = origin_y - math.sqrt((radius * radius) - (x * x)) - radius

        path_points.append([origin_x - x - radius, y])
        print(f'[{origin_x - x - radius}, {y}]')

    #
    # quadrant IV
    print('\nQuadrant IV')
    for i in range(steps + 1):
        x = 0
        y = 0
        point = [x, y]
        print(f'{point}')

    # plotter.draw_path(path_points)
