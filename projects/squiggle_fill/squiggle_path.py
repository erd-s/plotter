from utils.plotter_interface import PlotterInterface


def draw_squiggle_rectangle(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    height: float,
    width: float,
    space_between_lines: float,
    reverse: bool = False,
):
    iterations = int(height / space_between_lines)
    actual_space_between_lines = height / iterations

    squiggle_path = []

    for i in range(iterations):
        left = i % 2 == 0 if not reverse else i % 2 != 0
        horizontal_line_start_x = origin_x if left else origin_x + width
        horizontal_line_end_x = origin_x + width if left else origin_x
        horizontal_line_y = origin_y + (i * actual_space_between_lines)
        point_a = [horizontal_line_start_x, horizontal_line_y]
        point_b = [horizontal_line_end_x, horizontal_line_y]
        point_c = [
            horizontal_line_end_x,
            horizontal_line_y + actual_space_between_lines,
        ]

        squiggle_path.append(point_a)
        squiggle_path.append(point_b)
        squiggle_path.append(point_c)

        # draw_final_line
        if i + 1 == iterations:
            last_line_start_x = origin_x if left else origin_x + width
            last_line_point = [
                last_line_start_x,
                horizontal_line_y + actual_space_between_lines,
            ]
            squiggle_path.append(last_line_point)

    plotter.draw_path(squiggle_path)
