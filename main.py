from nextdraw import NextDraw

import time

from projects.complete import semis
from utils.text.text import create_text_svg

from utils.positioning import (
    DOC_WIDTH,
    DOC_HEIGHT,
    MARGIN,
    center_x,
    center_y,
    effective_height,
    effective_width,
)


def setup_plotter(nd: NextDraw):
    nd.interactive()

    if not nd.connect():
        quit()

    nd.options.pen_rate_lower = 5

    print("Current Settings:")
    print(f'Page Size: {DOC_WIDTH}"w x {DOC_HEIGHT}"h')
    print(f'Margin: {MARGIN}"')
    print(f"Center: {center_x()}, {center_y()}")
    print(f'Effective Size: {effective_width()}"w x {effective_height()}"h')
    return nd


def tear_down_plotter(plotter):
    plotter.penup()
    plotter.goto(0, 0)
    plotter.disconnect()


def run():
    # run svg plotter
    svg_plotter = NextDraw()
    path = create_text_svg(text="02-02-2025")
    svg_plotter.plot_setup(path)
    svg_plotter.plot_run()

    # run interactive plotter
    try:
        interactive_plotter = setup_plotter(NextDraw())
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        tear_down_plotter(interactive_plotter)
    except:
        tear_down_plotter(interactive_plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
