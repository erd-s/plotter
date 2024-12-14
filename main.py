from nextdraw import NextDraw

from projects.grid import create_grid
from projects.circles.burst_grid import BurstGrid
from projects.margin import draw_margin

from utils import (
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
    plotter = setup_plotter(NextDraw())

    # project to run
    # draw_margin(plotter)
    # create_grid(plotter=plotter, grid_size=5)
    project = BurstGrid(lines_per_quadrant=6)
    project.create_object_grid(plotter=plotter, grid_size=6)

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
