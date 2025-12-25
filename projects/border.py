from utils.plotter_interface import PlotterInterface
import itertools


def draw_border(
    plotter: PlotterInterface,
    paths: [[(float, float)]],
    padding: float = 0.1,
    angle: int = 45,
):
    coordinates = list(itertools.chain.from_iterable(paths))
    x_coordinates = []
    y_coordinates = []
    for i, coordinate in enumerate(coordinates):
        if i == 0 or i % 2 == 0:
            x_coordinates.append(coordinate)
        else:
            y_coordinates.append(coordinate)

    min_x: float = min(x_coordinates) - padding
    max_x: float = max(x_coordinates) + padding
    min_y: float = min(y_coordinates) - padding
    max_y: float = max(y_coordinates) + padding

    border_path = [
        [min_x, min_y],
        [max_x, min_y],
        [max_x, max_y],
        [min_x, max_y],
        [min_x, min_y],
    ]

    plotter.draw_path(border_path)
