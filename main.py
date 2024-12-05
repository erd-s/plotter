from nextdraw import NextDraw
from utils import center_y, center_x

from projects.irregular_cube import create_cube
from projects.irregular_cube_grid import create_irregular_cube_grid
from projects.circle import create_circle

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
    create_circle(
        plotter=plotter, origin_x=center_x(), origin_y=center_y(), radius=1.25, steps=5
    )

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
