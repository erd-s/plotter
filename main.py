from utils.plotter_interface.visualizer.visualized_plotter import VisualizedPlotter
from utils.plotter_interface.pen_plotter.pen_plotter import PenPlotter
from utils.plotter_interface.PlotterInterface import PlotterInterface
from projects.complete.ifs.bottom_page_layout import draw_bottom_page_layout
from projects.complete.ifs.page_title import draw_page_title_right, draw_page_title_left
from projects.circles.circle_lines import create_lined_circle

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

# TODO: Fix clip to bounds for non 5.8 x 8.3 sizes, crashes on create_concentric_circles_v2


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
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x(),
        center_origin_y=center_y(),
        radius=1,
        line_interval=0.06,
        angle=0,
    )
    end_time = time.perf_counter()
    print(f"Time Elapsed: {end_time - start_time:0.2f} seconds.")

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
