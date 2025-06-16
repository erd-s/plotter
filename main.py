from utils.plotter_interface.PlotterInterface import (
    VISUALIZED_PLOTTER,
    PEN_PLOTTER,
    PlotterInterface,
)

import time
from projects.complete.concentric_circles import create_concentric_circles

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
    return nd


def tear_down_plotter(plotter):
    plotter.penup()
    plotter.goto(0, 0)
    plotter.disconnect()


def run():
    plotter_interface = PEN_PLOTTER
    plotter = setup_plotter(plotter_interface)

    try:
        start_time = time.perf_counter()
        create_concentric_circles(plotter)
        end_time = time.perf_counter()
        print(f"Time Elapsed: {end_time - start_time:0.2f} seconds.")

        tear_down_plotter(plotter)
    except Exception as e:
        print(e)
        tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
