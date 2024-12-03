from nextdraw import NextDraw
from utils import setup_plotter, tear_down_plotter, center_y, center_x

from projects.irregular_cube import create_cube
from projects.xy import create_xy


def run():
    plotter = setup_plotter(NextDraw())

    # project to run
    # create_xy(plotter=plotter, max_x=1, max_y=1)
    create_cube(plotter=plotter, origin_x=center_x(), origin_y=center_y(), width=1)

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # dry run
    run()
