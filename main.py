from nextdraw import NextDraw

import time

from projects.complete import *
from projects.spiro.petal import create_spiro_petal

from utils.utils import (
    DOC_WIDTH,
    DOC_HEIGHT,
    center_x,
    center_y,
    effective_height,
    effective_width,
    vertical_margin,
    horizontal_margin,
)


def setup_plotter(nd: NextDraw):
    nd.interactive()

    if not nd.connect():
        quit()

    nd.options.pen_rate_lower = 5

    print("Current Settings:")
    print(f'Page Size: {DOC_WIDTH}"w x {DOC_HEIGHT}"h')
    print(f'Horizontal Margin: {horizontal_margin()}"')
    print(f'Vertical Margin: {vertical_margin()}":')
    print(f"Center: {center_x()}, {center_y()}")
    print(f'Effective Size: {effective_width()}"w x {effective_height()}"h')
    return nd


def tear_down_plotter(plotter):
    plotter.penup()
    plotter.goto(0, 0)
    plotter.disconnect()


def run():
    plotter = setup_plotter(NextDraw())

    try:
        start_time = time.perf_counter()
        create_spiro_petal(plotter=plotter, steps=50)
        end_time = time.perf_counter()

        print(f"Time Elapsed: {end_time - start_time:0.2f} seconds.")

        tear_down_plotter(plotter)
    except:
        tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
