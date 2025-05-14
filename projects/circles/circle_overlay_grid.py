import random

from nextdraw import NextDraw

from projects.circles.circle import create_circle
from projects.object_grid import ObjectGrid


class CircleOverlayGrid(ObjectGrid):
    density: int
    total_skips: int = 0
    total_circles: int = 0

    def __init__(self, density: int):
        super().__init__()
        self.density = density

    def object_logic(self, plotter: NextDraw):
        radius = self.square_width / 3.3
        density = 60
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
