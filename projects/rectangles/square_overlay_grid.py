import random

from nextdraw import NextDraw

from projects.rectangles.rectangle import create_rectangle
from projects.object_grid import ObjectGrid


class SquareOverlayGrid(ObjectGrid):
    density: int
    total_skips: int = 0
    total_squares: int = 0

    def __init__(self, density: int):
        super().__init__()
        self.density = density

    def object_logic(self, plotter: NextDraw):
        width = self.square_width / 3.75
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
