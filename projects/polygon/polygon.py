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
    vertex_angle = 360 / number_of_sides
    angle_radians = vertex_angle * (pi / 180) / 2
    base_length = 2 * (height * tan(angle_radians))

    for i in range(number_of_sides):
        rotation_angle = i * vertex_angle
        y = center_y + height
        x_start = center_x - base_length / 2
        x_end = center_x + base_length / 2
        path = [[x_start, y], [x_end, y]]
        rotated_path = rotate(
            path=path, degrees=rotation_angle, rotation_x=center_x, rotation_y=center_y
        )
        plotter.draw_path(rotated_path)
