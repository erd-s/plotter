from utils.plotter_interface import PlotterInterface
from projects.circles.circle import create_circle
from projects.object_grid import ObjectGrid
from enum import Enum
import random


class Direction(Enum):
    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 3


class ConcentricCirclesGrid(ObjectGrid):
    def object_logic(self, plotter: PlotterInterface):
        orientation = (
            "portrait" if self.square_height > self.square_width else "landscape"
        )

        starting_radius = (
            self.square_height if orientation == "portrait" else self.square_width
        ) / 60

        current_radius = starting_radius
        origin_x = self.square_center_x
        origin_y = self.square_center_y

        print(f"Concentric circle center origin: {origin_x}, {origin_y}")
        while (
            current_radius < self.square_height
            if orientation == "portrait"
            else self.square_width
        ):
            create_circle(
                plotter=plotter,
                origin_x=origin_x,
                origin_y=origin_y,
                radius=current_radius,
            )

            multiplicative_growth = current_radius * 0.03
            static_growth = (
                self.square_height if orientation == "portrait" else self.square_width
            ) / 60
            current_radius += (
                multiplicative_growth
                if multiplicative_growth > static_growth
                else static_growth
            )
