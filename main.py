from nextdraw import NextDraw
from utils import (
    setup_plotter,
    tear_down_plotter,
)

from projects.bursts import create_burst

def run():
    plotter = setup_plotter(NextDraw())

    # project to run
    create_burst(plotter=plotter, number_of_lines=40)

    tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # dry run
    run()
