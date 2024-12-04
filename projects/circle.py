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
    reversed_path_points = list(reversed(path_points))
    for i in range(steps + 1):
        x = reversed_path_points[i][0]
        y = (reversed_path_points[i][1] * -1) + origin_y + radius
        point = [x, y]
        path_points.append(point)
        print(f'{point}')

    #
    # # quadrant III
    print('\nQuadrant III')
    reversed_path_points = list(reversed(path_points))
    x_list = []
    y_list = []
    for i in range(steps + 1):
        x = (reversed_path_points[i][0]) - math.sqrt(radius)
        y = (reversed_path_points[i][1])
        x_list.insert(0, x)
        y_list.append(y)

    for i in range(len(x_list)):
        point = [x_list[i], y_list[i]]
        path_points.append(point)
        print(f'{point}')

    # # quadrant IV
    # for i in range(steps + 1):
    #     x = path_points[i][0]
    #     y = path_points[i][1]
    #     path_points.append([x, y])

    # plotter.draw_path(path_points)
