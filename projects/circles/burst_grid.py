from nextdraw import NextDraw

from projects.circles.bursts import create_burst
from projects.circles.circle import create_circle
from projects.object_grid import ObjectGrid


class BurstGrid(ObjectGrid):
    lines_per_quadrant: int

    def __init__(self, lines_per_quadrant: int):
        super().__init__()
        self.lines_per_quadrant = lines_per_quadrant

    def object_logic(self, plotter: NextDraw):
        radius = (self.square_height / 2) * 0.75

        create_burst(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_center_y,
            radius=radius,
            lines_per_quadrant=self.lines_per_quadrant,
        )

        create_circle(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_center_y,
            radius=radius * 0.65,
            steps=30,
        )

        create_circle(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_center_y,
            radius=radius * 0.9,
            steps=30,
        )
