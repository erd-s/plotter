from nextdraw import NextDraw
from utils import (
    setup_plotter,
    tear_down_plotter,
)

from projects.grid import create_grid

def run():
    plotter = setup_plotter(NextDraw())

    # project to run
    create_grid(plotter=plotter, grid_size=20)

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # dry run
    run()
