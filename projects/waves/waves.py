from utils.plotter_interface import PlotterInterface
import numpy as np


class SineWave:

    def create_wave(
        self,
        plotter: PlotterInterface,
        start_x: float,
        end_x: float,
        start_y: float,
        end_y: float,
        y_position: float
    ):
        step = 0.1
        x_list = np.arange(start_x, 5*np.pi, step)
        y_list = np.sin(x_list)

        path = []
        needs_to_move = False
        for i, x in enumerate(x_list):
            y = y_list[i]

            if start_x < x < end_x and start_y < y + y_position < end_y:
                point = [x, y + y_position]
                if needs_to_move:
                    plotter.moveto(x_target=point[0], y_target=point[1])
                    needs_to_move = False

                path.append(point)
                plotter.draw_path(path)
            else:
                if len(path) != 0:
                    plotter.draw_path(path)
                    path = []
                    plotter.penup()
                    needs_to_move = True
