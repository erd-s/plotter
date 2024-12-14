import random

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
            lines_per_quadrant=random.randint(self.lines_per_quadrant - 2, self.lines_per_quadrant + 2),
        )

        inside_circle_radius = random.uniform(radius * 0.4, radius * 0.6)
        create_circle(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_center_y,
            radius=inside_circle_radius,
            steps=30,
        )

        outside_circle_radius = random.uniform(radius * 0.8, radius * 0.9)
        create_circle(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_center_y,
            radius=outside_circle_radius,
            steps=30,
        )
