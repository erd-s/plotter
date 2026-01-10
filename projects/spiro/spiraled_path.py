from utils.plotter_interface import PlotterInterface
from utils.transform import rotated_path


def draw_spiraled_shape(
    plotter: PlotterInterface,
    shape_path: [(float, float)],
    shape_center_x: float,
    shape_center_y: float,
    degree_interval: int = 5,
    number_to_skip: int = 0,
):
    degree = 0
    iterations = int(360 / degree_interval)
    total_run = 0
    for i in range(iterations):
        if i % (number_to_skip + 1) == 0:
            total_run += 1
            path = rotated_path(
                path=shape_path,
                degrees=degree,
                rotation_x=shape_center_x,
                rotation_y=shape_center_y,
            )
            plotter.draw_path(path)
            degree += degree_interval
