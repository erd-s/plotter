from nextdraw import NextDraw

from projects.lines.lines import create_lines
from projects.object_grid import ObjectGrid


class LinesGrid(ObjectGrid):
    number_of_lines: int

    def __init__(self, number_of_lines):
        super().__init__()
        self.number_of_lines = number_of_lines

    def object_logic(self, plotter: NextDraw):
        create_lines(
            plotter=plotter,
            number_of_lines=self.number_of_lines,
            origin_x=self.square_center_x - (self.square_width / 2),
            origin_y=self.square_center_y - (self.square_height / 2),
            max_height=self.square_height,
            max_width=self.square_width,
        )
