from utils.plotter_interface import PlotterInterface
from projects.object_grid_v2 import ObjectGridV2
from projects.polygon.polygon import polygon_paths, draw_polygon_star
from utils.transform import rotate


class PolygonObjectGrid(ObjectGridV2):
    number_of_sides: int

    def __init__(
        self,
        number_of_sides: int,
        grid_size_horizontal: int,
        grid_size_vertical: int,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
    ):
        super().__init__(
            grid_size_horizontal, grid_size_vertical, origin_x, origin_y, width, height
        )
        self.number_of_sides = number_of_sides

    def object_logic(self, plotter: PlotterInterface):
        height = (
            self.square_width
            if self.square_width < self.square_height
            else self.square_height
        ) * 0.9

        draw_polygon_star(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y,
            number_of_sides=self.number_of_sides,
            height=height,
        )
