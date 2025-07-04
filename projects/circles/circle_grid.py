from utils.plotter_interface import PlotterInterface

from projects.circles.circle import create_circle
from projects.object_grid import ObjectGrid


class CircleGrid(ObjectGrid):
    circles_per_square: int

    def __init__(self, grid_size: int, circles_per_square: int):
        super().__init__(grid_size=grid_size)
        self.circles_per_square = circles_per_square

    def object_logic(self, plotter: PlotterInterface):
        for c in range(self.circles_per_square):
            radius = self.square_width / (self.circles_per_square + 1)
            x_offset = (self.square_width / -2) + ((c + 1) * radius)
            y_offset = 0

            create_circle(
                plotter=plotter,
                origin_x=self.square_center_x + x_offset,
                origin_y=self.square_center_y + y_offset,
                radius=radius,
            )
