from utils.plotter_interface import PlotterInterface
from numpy import tan, pi
from utils.transform import rotated_path


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
    paths_to_draw = []
    for path in paths:
        paths_to_draw.append(path[0])

    # close path
    paths_to_draw.append(paths_to_draw[0])
    plotter.draw_path(paths_to_draw)


def draw_filled_polygon(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    number_of_sides: int,
    height: float,
    pen_width_mm: float,
):
    pen_width_in = (pen_width_mm * 0.039) * 0.7
    iterations = int(height / pen_width_in) + 1
    for i in range(iterations):
        paths = polygon_paths(
            center_x=center_x,
            center_y=center_y,
            number_of_sides=number_of_sides,
            height=height - (i * pen_width_in),
        )
        paths_to_draw = []
        for path in paths:
            paths_to_draw.append(path[0])

        # close path
        paths_to_draw.append(paths_to_draw[0])
        plotter.draw_path(paths_to_draw)


def polygon_paths(
    center_x: float, center_y: float, number_of_sides: int, height: float
):
    vertex_angle = 360 / number_of_sides
    angle_radians = vertex_angle * (pi / 180) / 2
    base_length = 2 * (height / 2 * tan(angle_radians))

    paths = []
    for i in range(number_of_sides):
        rotation_angle = i * -vertex_angle
        y = center_y + height / 2
        x_start = center_x - base_length / 2
        x_end = center_x + base_length / 2
        path = [[x_start, y], [x_end, y]]
        rotated_polygon_path = rotated_path(
            path=path, degrees=rotation_angle, rotation_x=center_x, rotation_y=center_y
        )
        paths.append(rotated_polygon_path)

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

    lines_per_side = 5

    for ns in range(number_of_sides):
        rotation_angle = ns * vertex_angle

        for i in range(lines_per_side):
            y_end = center_y + height / 2
            x_end = center_x - (base_length / 2) + ((base_length / lines_per_side) * i)
            path = [[center_x, center_y], [x_end, y_end]]
            rotated_polygon_path = rotated_path(
                path=path,
                degrees=rotation_angle,
                rotation_x=center_x,
                rotation_y=center_y,
            )
            plotter.draw_path(rotated_polygon_path)
