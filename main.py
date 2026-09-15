from utils.plotter_interface.visualizer.visualized_plotter import VisualizedPlotter
from utils.plotter_interface.pen_plotter.pen_plotter import PenPlotter
from utils.plotter_interface.PlotterInterface import PlotterInterface
from projects.weeks_grid.weeks_grid_v2 import WeeksGridV2
from projects.margin import draw_margin

import time
from utils.utils import (
    DOC_WIDTH,
    DOC_HEIGHT,
    center_x,
    center_y,
    effective_height,
    effective_width,
    effective_x_start,
    effective_x_end,
    effective_y_start,
    effective_y_end,
)


def setup_plotter(nd: PlotterInterface):
    nd.interactive()

    if not nd.connect():
        quit()

    print("Current Settings:")
    print(f'Page Size: {DOC_WIDTH}"w x {DOC_HEIGHT}"h')
    print(f"Center: {center_x()}, {center_y()}")
    print(f'Effective Size: {effective_width()}"w x {effective_height()}"h')


def tear_down_plotter(plotter):
    plotter.disconnect()


def run():
    plotter = VisualizedPlotter(
        clip_to_bounds=False,
        x_min=effective_x_start(),
        x_max=effective_x_end(),
        y_min=effective_y_start(),
        y_max=effective_y_end(),
    )

    setup_plotter(plotter)
    start_time = time.perf_counter()
    inset = 0.2
    project = WeeksGridV2(
        weeks=1,
        top_section_lines=10,
        bottom_section_lines=0,
        origin_x=effective_x_start() + inset,
        origin_y=effective_y_start() + inset,
        height=effective_height() - (inset * 2),
        width=effective_width() - (inset * 2),
        column_one_width=1.25,
        padding=0.2,
    )
    project.draw_header_column_top_section(plotter=plotter, draw_grid=False)
    project.draw_top_section(plotter=plotter, draw_grid=False)
    project.draw_header_row_top_section(plotter=plotter)
    project.draw_bottom_section(plotter=plotter, draw_grid=True)
    project.draw_header_column_bottom_section(plotter=plotter, draw_grid=True)
    draw_margin(plotter=plotter)
    end_time = time.perf_counter()
    print(f"Time Elapsed: {end_time - start_time:0.2f} seconds.")

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
