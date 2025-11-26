from utils.plotter_interface import PlotterInterface
from projects.circles.semicircle import semicircle_path
from utils.transform import rotate


def create_iterative_semicircles(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    radius: float,
    degree_interval: int = 5,
):
    original_path = semicircle_path(origin_x=origin_x, origin_y=origin_y - radius, radius=radius)
    degree = 0

    for _ in range(int(360 / degree_interval)):
        path = rotate(path=original_path, degrees=degree, rotation_x=original_path[0][0], rotation_y=original_path[0][1])
        plotter.draw_path(path)
        degree += degree_interval
