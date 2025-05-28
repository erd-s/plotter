from nextdraw import NextDraw
import math
from projects.circles.half_circles import create_half_circle
from projects.object_grid import ObjectGrid


class HalfCircleGrid(ObjectGrid):
    half_circles_per_square: int

    def __init__(self, grid_size: int, half_circles_per_square: int):
        super().__init__(grid_size=grid_size)
        self.half_circles_per_square = half_circles_per_square

    def object_logic(self, plotter: NextDraw):
        radius = self.square_width / (self.half_circles_per_square + 1)
        max_circles_vertically = math.floor(self.square_height / radius)

        for v in range(max_circles_vertically):
            for c in range(self.half_circles_per_square + 1):
                x_offset = (self.square_width / -2) + ((c + 1) * radius) - (radius)
                y_offset = (v * radius) + (radius / 1.5)

                create_half_circle(
                    plotter=plotter,
                    origin_x=self.square_center_x + x_offset,
                    origin_y=self.square_center_y - (self.square_height / 2) + y_offset,
                    radius=radius,
                    steps=30,
                )
