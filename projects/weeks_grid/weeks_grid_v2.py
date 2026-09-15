from projects.grid import draw_grid_v3
from utils.plotter_interface import PlotterInterface
from projects.border.border import draw_border_right
from projects.text.text import HorizontalText


class WeeksGridV2:
    weeks: int
    top_section_lines: int
    bottom_section_lines: int
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
    space_between_sections: float = 0.3

    def __init__(
        self,
        weeks: int,
        top_section_lines: int,
        bottom_section_lines: int,
        origin_x: float,
        origin_y: float,
        height: float,
        width: float,
        column_one_width: float = 1,
        padding: float = 0.03,
        with_shadow: bool = False,
    ):
        self.weeks = weeks
        self.top_section_lines = top_section_lines
        self.bottom_section_lines = bottom_section_lines
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.height = height - self.space_between_sections
        self.width = width
        self.padding = padding
        self.column_one_width = column_one_width
        self.cell_height = (self.height - padding) / (
            (top_section_lines + bottom_section_lines) + 1
        )
        self.week_column_width = (width - (padding * weeks) - column_one_width) / weeks
        self.week_origin_x = origin_x + column_one_width + padding
        self.shadow_depth = self.padding / 10 if with_shadow else 0

    def draw_header_column_top_section(
        self, plotter: PlotterInterface, draw_grid: bool
    ):
        if draw_grid:
            header_origin_x = self.origin_x
            header_origin_y = self.origin_y + self.cell_height + self.padding
            header_height = self.cell_height * self.top_section_lines
            draw_grid_v3(
                plotter=plotter,
                grid_size_horizontal=1,
                grid_size_vertical=self.top_section_lines,
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
        else:
            # draw lines
            for i in range(self.top_section_lines):
                line_origin_x = self.origin_x
                line_width = self.column_one_width
                line_origin_y = (
                    self.origin_y
                    + (self.cell_height * (i + 1))
                    + self.cell_height
                    + self.padding
                )
                plotter.moveto(line_origin_x, line_origin_y)
                plotter.line(line_width, 0)

    def draw_header_row_top_section(
        self, plotter: PlotterInterface, boxes_per_day: int = 1
    ):
        for w in range(self.weeks):
            for d in range(7):
                text = "s"
                if d == 0:
                    text = "m"
                elif d == 1:
                    text = "t"
                elif d == 2:
                    text = "w"
                elif d == 3:
                    text = "t"
                elif d == 4:
                    text = "f"
                elif d == 5:
                    text = "s"
                elif d == 6:
                    text = "s"

                text_width = 0.1
                text_origin_x = (
                    self.origin_x
                    + self.column_one_width
                    + self.padding
                    + ((self.week_column_width / 7) * d)
                    + (self.week_column_width / 7) / 2
                    - (text_width / 2)
                    + (self.week_column_width * w)
                    + (self.padding * w)
                )
                text_origin_y = self.origin_y + text_width
                text = HorizontalText(
                    plotter=plotter,
                    text=text,
                    origin_x=text_origin_x,
                    origin_y=text_origin_y,
                    width=text_width,
                    height=text_width,
                )
                text.draw_text()

    def draw_top_section(self, plotter: PlotterInterface, draw_grid: bool):
        for w in range(self.weeks):
            week_origin_x = (
                self.week_origin_x + (self.week_column_width * w) + (self.padding * w)
            )
            week_origin_y = self.origin_y + self.cell_height + self.padding
            week_height = self.cell_height * self.top_section_lines

            if draw_grid:
                draw_grid_v3(
                    plotter=plotter,
                    grid_size_horizontal=7,
                    grid_size_vertical=self.top_section_lines,
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
            else:
                # draw lines
                for i in range(self.top_section_lines):
                    for windex in range(7):
                        line_spacing = self.column_one_width * 0.1
                        line_origin_x = (
                            week_origin_x
                            + (line_spacing / 2)
                            + (windex * self.week_column_width / 7)
                        )
                        line_width = (self.week_column_width / 7) - (line_spacing)
                        line_origin_y = week_origin_y + (self.cell_height * (i + 1))
                        plotter.moveto(line_origin_x, line_origin_y)
                        plotter.line(line_width, 0)

    def draw_bottom_section(self, plotter: PlotterInterface, draw_grid: bool):
        if self.bottom_section_lines == 0:
            return

        for w in range(self.weeks):
            week_origin_x = (
                self.week_origin_x + (self.week_column_width * w) + (self.padding * w)
            )
            week_origin_y = (
                self.origin_y
                + self.cell_height
                + self.padding
                + (self.cell_height * self.top_section_lines)
                + self.space_between_sections
            )
            week_height = self.cell_height * self.bottom_section_lines

            if draw_grid:
                draw_grid_v3(
                    plotter=plotter,
                    grid_size_horizontal=7,
                    grid_size_vertical=self.bottom_section_lines,
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
            else:
                # draw lines
                for i in range(self.bottom_section_lines):
                    for windex in range(7):
                        line_spacing = self.column_one_width * 0.1
                        line_origin_x = (
                            week_origin_x
                            + (line_spacing / 2)
                            + (windex * self.week_column_width / 7)
                        )
                        line_width = (self.week_column_width / 7) - line_spacing
                        line_origin_y = week_origin_y + (self.cell_height * (i + 1))
                        plotter.moveto(line_origin_x, line_origin_y)
                        plotter.line(line_width, 0)

    def draw_header_column_bottom_section(
        self, plotter: PlotterInterface, draw_grid: bool
    ):
        if self.bottom_section_lines == 0:
            return

        if draw_grid:
            header_origin_x = self.origin_x
            header_origin_y = (
                self.origin_y
                + self.cell_height
                + self.padding
                + (self.cell_height * self.top_section_lines)
                + self.space_between_sections
            )
            header_height = self.cell_height * self.bottom_section_lines
            draw_grid_v3(
                plotter=plotter,
                grid_size_horizontal=1,
                grid_size_vertical=self.bottom_section_lines,
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
        else:
            # draw lines
            for i in range(self.top_section_lines):
                line_origin_x = self.origin_x
                line_width = self.column_one_width
                line_origin_y = (
                    self.origin_y
                    + (self.cell_height * (i + 1))
                    + self.cell_height
                    + self.padding
                    + (self.cell_height * self.top_section_lines)
                    + self.space_between_sections
                )
                plotter.moveto(line_origin_x, line_origin_y)
                plotter.line(line_width, 0)
