import random

from utils.plotter_interface import PlotterInterface

from projects.circles.bursts import draw_burst
from projects.circles.circle import draw_circle
from projects.object_grid import ObjectGrid


class BurstGrid(ObjectGrid):
    lines_per_quadrant: int

    def __init__(self, lines_per_quadrant: int, grid_size: int):
        super().__init__(grid_size=grid_size)
        self.lines_per_quadrant = lines_per_quadrant

    def object_logic(self, plotter: PlotterInterface):
        radius = (
            (
                self.square_height
                if self.square_height < self.square_width
                else self.square_width
            )
            / 2
        ) * 0.75

        draw_burst(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_center_y,
            radius=radius,
            lines_per_quadrant=random.randint(
                self.lines_per_quadrant - 2, self.lines_per_quadrant + 2
            ),
        )

        inside_circle_radius = random.uniform(radius * 0.4, radius * 0.6)
        print(f'Inside Circle Radius: {inside_circle_radius}"')
        draw_circle(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y,
            radius=inside_circle_radius,
        )

        outside_circle_radius = random.uniform(radius * 0.8, radius * 0.9)
        print(f'Outside Circle Radius: {outside_circle_radius}"')
        draw_circle(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y,
            radius=outside_circle_radius,
        )
