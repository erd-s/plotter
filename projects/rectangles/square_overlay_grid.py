import random

from utils.plotter_interface import PlotterInterface

from projects.rectangles.rectangle import create_rectangle
from projects.object_grid import ObjectGrid


class SquareOverlayGrid(ObjectGrid):
    density: int
    total_skips: int = 0
    total_squares: int = 0
    width_ratio: float

    def __init__(self, grid_size: int, density: int, width_ratio: float):
        super().__init__(grid_size=grid_size)
        self.density = density
        self.width_ratio = width_ratio

    def object_logic(self, plotter: PlotterInterface):
        width = self.square_width * self.width_ratio
        density = self.density
        random_constant = random.uniform(0, 100)
        skip = random_constant > density

        if not skip:
            self.total_squares += 1
            create_rectangle(
                plotter=plotter,
                height=width,
                width=width,
                center_x=self.square_center_x,
                center_y=self.square_center_y,
            )
        else:
            self.total_skips += 1
