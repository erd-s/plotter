import math
import time

from nextdraw import NextDraw
from utils.utils import (
    effective_height,
    effective_width,
    effective_x_start,
    effective_y_start,
    effective_x_end,
    effective_y_end,
)


def run(plotter: NextDraw, zigs: int):
    density_constant = 5
    zig_width = effective_width() / zigs
    zag_height = effective_height() / density_constant
    line_distance = zag_height / density_constant
    start_x = effective_x_start()
    start_y = effective_y_start()
    m = zig_width / zag_height

    print(
        f"""
    Zig Zags:
    zig width: {zig_width}
    zig zag height: {zag_height}
    """
    )

    plotter.moveto(start_x, start_y)
    end = False
    while plotter.current_pos()[1] < effective_y_end() and not end:
        for i in range(zigs):
            current_x = plotter.current_pos()[0]
            current_y = plotter.current_pos()[1]
            y_delta = zag_height if i % 2 == 0 or i == 0 else zag_height * -1

            # Past the bottom
            if current_y + y_delta >= effective_y_end():
                if current_y - effective_y_end() > 0.1:
                    # end
                    print("Ending")
                    plotter.penup()
                    end = True
                    break
                else:
                    if current_x + zig_width >= effective_x_end() - 0.1:
                        # reset to starting x
                        plotter.moveto(
                            effective_x_start(),
                            plotter.current_pos()[1] + line_distance,
                        )
                        break

                    adjusted_y_delta = effective_y_end() - current_y
                    adjusted_x_delta = m * adjusted_y_delta
                    plotter.lineto(current_x + adjusted_x_delta, effective_y_end())

                    x_move = (zig_width - adjusted_x_delta) * 2
                    plotter.move(x_move, 0)

                    plotter.line(adjusted_x_delta, adjusted_y_delta * -1)
                    break
            # The middle
            else:
                if current_x + zig_width >= effective_x_end() - 0.2:
                    plotter.lineto(effective_x_end(), current_y + y_delta)

                    # reset to starting x
                    print("Moving to starting X, moving down one line")
                    plotter.moveto(
                        effective_x_start(),
                        plotter.current_pos()[1] + line_distance,
                    )
                    break

            plotter.line(zig_width, y_delta)

    # top section
    # Above the top
    plotter.moveto(effective_x_start(), effective_y_start())
    for z in range(int(zigs / 2)):
        x_step_distance = zig_width / density_constant

        for i in range(density_constant):
            plotter.move(x_step_distance, 0)
            adjusted_x_delta = zig_width - (x_step_distance * (i + 1))

            adjusted_y_delta = zag_height - ((zag_height / density_constant) * (i + 1))

            # zig down
            plotter.line(adjusted_x_delta, adjusted_y_delta)

            # zag up
            plotter.line(adjusted_x_delta, adjusted_y_delta * - 1)

            # reset
            if i + 1 != density_constant:
                plotter.move((adjusted_x_delta * - 2), 0)

        plotter.move(zig_width, 0)