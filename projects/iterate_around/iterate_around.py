from utils.plotter_interface import PlotterInterface
from utils.transform import rotate


def iterate_around(
    plotter: PlotterInterface, original_path: [(float, float)], degree_interval: int
):
    degree = 0

    for _ in range(int(360 / degree_interval)):
        path = rotate(
            path=original_path,
            degrees=degree,
            rotation_x=original_path[0][0],
            rotation_y=original_path[0][1],
        )
        plotter.draw_path(path)
        degree += degree_interval
