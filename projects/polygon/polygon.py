from utils.plotter_interface import PlotterInterface
from numpy import tan, pi
from utils.transform import rotate


def draw_polygon(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    number_of_sides: int,
    height: float,
):
    paths = polygon_paths(
        center_x=center_x,
        center_y=center_y,
        number_of_sides=number_of_sides,
        height=height,
    )
    for path in paths:
        plotter.draw_path(path)


def polygon_paths(
    center_x: float, center_y: float, number_of_sides: int, height: float
):
    vertex_angle = 360 / number_of_sides
    angle_radians = vertex_angle * (pi / 180) / 2
    base_length = 2 * (height / 2 * tan(angle_radians))

    paths = []
    for i in range(number_of_sides):
        rotation_angle = i * vertex_angle
        y = center_y + height / 2
        x_start = center_x - base_length / 2
        x_end = center_x + base_length / 2
        path = [[x_start, y], [x_end, y]]
        rotated_path = rotate(
            path=path, degrees=rotation_angle, rotation_x=center_x, rotation_y=center_y
        )
        paths.append(rotated_path)

    return paths


def draw_polygon_star(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    number_of_sides: int,
    height: float,
):
    vertex_angle = 360 / number_of_sides
    angle_radians = vertex_angle * (pi / 180) / 2
    base_length = 2 * (height / 2 * tan(angle_radians))

    lines_per_side = round(height / 0.75)

    for ns in range(number_of_sides):
        rotation_angle = ns * vertex_angle

        for i in range(lines_per_side):
            y_end = center_y + height / 2
            x_end = center_x - (base_length / 2) + ((base_length / lines_per_side) * i)
            path = [[center_x, center_y], [x_end, y_end]]
            rotated_path = rotate(
                path=path,
                degrees=rotation_angle,
                rotation_x=center_x,
                rotation_y=center_y,
            )
            plotter.draw_path(rotated_path)
