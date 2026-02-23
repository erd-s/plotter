from utils.plotter_interface.visualizer.visualized_plotter import VisualizedPlotter
from utils.plotter_interface.pen_plotter.pen_plotter import PenPlotter
from utils.plotter_interface.PlotterInterface import PlotterInterface
from projects.complete.filled_circle_grid import draw_filled_circle_grid_v2

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
    plotter = PenPlotter(
        clip_to_bounds=False,
        x_min=effective_x_start(),
        x_max=effective_x_end(),
        y_min=effective_y_start(),
        y_max=effective_y_end(),
    )

    setup_plotter(plotter)
    start_time = time.perf_counter()
    draw_filled_circle_grid_v2(
        plotter=plotter,
        grid_size_horizontal=10,
        grid_size_vertical=15,
        center_x=center_x(),
        center_y=center_y(),
        width=effective_width() - 1,
        height=effective_height() - 1,
        pen_width_mm=0.5,
    )
    end_time = time.perf_counter()
    print(f"Time Elapsed: {end_time - start_time:0.2f} seconds.")

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
