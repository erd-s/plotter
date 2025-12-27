from utils.plotter_interface import PlotterInterface
from projects.circles.circle import create_circle_v2
from enum import Enum


class Direction(Enum):
    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 3


class ConcentricCircles:
    plotter: PlotterInterface
    center_x: float
    center_y: float
    effective_height: float
    effective_width: float
    effective_start_x: float
    effective_end_x: float
    effective_start_y: float
    effective_end_y: float
    radius: float
    direction: Direction

    def __init__(
        self,
        plotter: PlotterInterface,
        center_x: float,
        center_y: float,
        effective_height: float,
        effective_width: float,
        effective_start_x: float,
        effective_end_x: float,
        effective_start_y: float,
        effective_end_y: float,
        radius: float,
        direction: Direction,
    ):
        self.plotter = plotter
        self.center_x = center_x
        self.center_y = center_y
        self.effective_height = effective_height
        self.effective_width = effective_width
        self.effective_start_x = effective_start_x
        self.effective_end_x = effective_end_x
        self.effective_start_y = effective_start_y
        self.effective_end_y = effective_end_y
        self.radius = radius
        self.direction = direction

    def create_concentric_circles(self):
        circle_distance = self.radius
        radius = self.radius
        origin_x = self.center_x
        origin_y = self.center_y

        out_of_bounds = False

        while not out_of_bounds:
            create_circle_v2(
                plotter=self.plotter,
                center_origin_x=origin_x,
                center_origin_y=origin_y,
                radius=radius,
            )
            radius += circle_distance * 2
            match self.direction:
                case Direction.TOP_LEFT:
                    origin_x -= circle_distance
                    origin_y -= circle_distance
                case Direction.TOP_RIGHT:
                    origin_x += circle_distance
                    origin_y -= circle_distance
                case Direction.BOTTOM_RIGHT:
                    origin_x += circle_distance
                    origin_y += circle_distance
                case Direction.BOTTOM_LEFT:
                    origin_x -= circle_distance
                    origin_y += circle_distance

            circle_start_x = origin_x - radius
            circle_end_x = origin_x + radius
            circle_start_y = origin_y - radius
            circle_end_y = origin_y + radius
            out_of_bounds = (
                circle_start_x < self.effective_start_x + 0.1
                or circle_end_x > self.effective_end_x - 0.1
                or circle_start_y < self.effective_start_y + 0.1
                or circle_end_y > self.effective_end_y - 0.1
            )
