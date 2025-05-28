import random

from nextdraw import NextDraw

from projects.circles.circle import create_circle
from projects.object_grid import ObjectGrid


class CircleOverlayGrid(ObjectGrid):
    density: int
    total_skips: int = 0
    total_circles: int = 0
    width_ratio: float

    def __init__(self, grid_size: int, density: int, width_ratio: float):
        super().__init__(grid_size=grid_size)
        self.density = density
        self.width_ratio = width_ratio

    def object_logic(self, plotter: NextDraw):
        radius = self.square_width * self.width_ratio
        density = self.density
        random_constant = random.uniform(0, 100)
        skip = random_constant > density

        if not skip:
            self.total_circles += 1
            create_circle(
                plotter=plotter,
                origin_x=self.square_center_x,
                origin_y=self.square_center_y,
                radius=radius,
                steps=15,
            )
        else:
            self.total_skips += 1
