from utils.plotter_interface.PlotterInterface import (
    VISUALIZED_PLOTTER,
    PEN_PLOTTER,
    PlotterInterface,
)

import time
from projects.waves.waves import SineWave
import traceback

import utils


def setup_plotter(nd: PlotterInterface):
    nd.interactive()

    if not nd.connect():
        quit()

    print("Current Settings:")
    print(f'Page Size: {utils.DOC_WIDTH}"w x {utils.DOC_HEIGHT}"h')
    print(f"Center: {utils.center_x()}, {utils.center_y()}")
    print(f'Effective Size: {utils.effective_width()}"w x {utils.effective_height()}"h')
    return nd


def tear_down_plotter(plotter):
    plotter.penup()
    plotter.goto(0, 0)
    plotter.disconnect()


def run():
    plotter_interface = VISUALIZED_PLOTTER
    plotter = setup_plotter(plotter_interface)

    try:
        start_time = time.perf_counter()

        project = SineWave()
        lines = 70
        for i in range(lines):
            project.create_wave(
                plotter=plotter,
                start_x=utils.effective_x_start(),
                end_x=utils.effective_x_end(),
                start_y=utils.effective_x_start(),
                end_y=utils.effective_y_end(),
                y_position=(utils.effective_height() / lines) * i
            )

        end_time = time.perf_counter()
        print(f"Time Elapsed: {end_time - start_time:0.2f} seconds.")
        tear_down_plotter(plotter)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        tear_down_plotter(plotter)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
