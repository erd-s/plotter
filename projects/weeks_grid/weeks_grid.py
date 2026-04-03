from projects.grid import draw_grid_v3
from utils.plotter_interface import PlotterInterface
from projects.border.border import draw_border_right


class WeeksGrid:
    weeks: int
    vertical_lines: int
    origin_x: float
    origin_y: float
    height: float
    width: float
    cell_width: float
    padding: float
    column_one_width: float
    cell_height: float
    week_column_width: float
    week_origin_x: float
    shadow_depth: float
    shadow_angle: int = 30

    def __init__(
        self,
        weeks: int,
        vertical_lines: int,
        origin_x: float,
        origin_y: float,
        height: float,
        width: float,
        column_one_width: float = 1,
        padding: float = 0.03,
        with_shadow: bool = False,
    ):
        self.weeks = weeks
        self.vertical_lines = vertical_lines
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.height = height
        self.width = width
        self.padding = padding
        self.column_one_width = column_one_width
        self.cell_height = (height - padding) / (vertical_lines + 1)
        self.week_column_width = (width - (padding * weeks) - column_one_width) / weeks
        self.week_origin_x = origin_x + column_one_width + padding
        self.shadow_depth = self.padding / 10 if with_shadow else 0

    def draw_header_column(self, plotter: PlotterInterface):
        header_origin_x = self.origin_x
        header_origin_y = self.origin_y + self.cell_height + self.padding
        header_height = self.height - self.padding - self.cell_height
        draw_grid_v3(
            plotter=plotter,
            grid_size_horizontal=1,
            grid_size_vertical=self.vertical_lines,
            origin_x=header_origin_x,
            origin_y=header_origin_y,
            height=header_height,
            width=self.column_one_width,
        )
        header_point_a = [header_origin_x, header_origin_y]
        header_point_b = [header_origin_x + self.column_one_width, header_origin_y]
        header_point_c = [
            header_origin_x + self.column_one_width,
            header_origin_y + header_height,
        ]
        header_point_d = [header_origin_x, header_origin_y + header_height]
        header_path = [
            header_point_a,
            header_point_b,
            header_point_c,
            header_point_d,
            header_point_a,
        ]
        draw_border_right(
            plotter=plotter,
            paths=header_path,
            padding=0,
            shadow_depth=self.shadow_depth,
            angle=self.shadow_angle,
        )

    def draw_header_rows(self, plotter: PlotterInterface):
        for w in range(self.weeks):
            header_origin_x = (
                self.week_origin_x + (self.week_column_width * w) + (self.padding * w)
            )
            header_origin_y = self.origin_y
            header_height = self.cell_height
            draw_grid_v3(
                plotter=plotter,
                grid_size_horizontal=7,
                grid_size_vertical=1,
                origin_x=header_origin_x,
                origin_y=self.origin_y,
                height=header_height,
                width=self.week_column_width,
            )
            header_point_a = [header_origin_x, header_origin_y]
            header_point_b = [header_origin_x + self.week_column_width, header_origin_y]
            header_point_c = [
                header_origin_x + self.week_column_width,
                header_origin_y + header_height,
            ]
            header_point_d = [header_origin_x, header_origin_y + header_height]
            header_path = [
                header_point_a,
                header_point_b,
                header_point_c,
                header_point_d,
                header_point_a,
            ]
            draw_border_right(
                plotter=plotter,
                paths=header_path,
                padding=0,
                shadow_depth=self.shadow_depth,
                angle=self.shadow_angle,
            )

    def draw_week_sections(self, plotter: PlotterInterface):
        for w in range(self.weeks):
            week_origin_x = (
                self.week_origin_x + (self.week_column_width * w) + (self.padding * w)
            )
            week_origin_y = self.origin_y + self.cell_height + self.padding
            week_height = self.cell_height * self.vertical_lines
            draw_grid_v3(
                plotter=plotter,
                grid_size_horizontal=7,
                grid_size_vertical=self.vertical_lines,
                origin_x=week_origin_x,
                origin_y=week_origin_y,
                height=week_height,
                width=self.week_column_width,
            )
            week_point_a = [week_origin_x, week_origin_y]
            week_point_b = [week_origin_x + self.week_column_width, week_origin_y]
            week_point_c = [
                week_origin_x + self.week_column_width,
                week_origin_y + week_height,
            ]
            week_point_d = [week_origin_x, week_origin_y + week_height]
            week_path = [
                week_point_a,
                week_point_b,
                week_point_c,
                week_point_d,
                week_point_a,
            ]
            draw_border_right(
                plotter=plotter,
                paths=week_path,
                padding=0,
                shadow_depth=self.shadow_depth,
                angle=self.shadow_angle,
            )
