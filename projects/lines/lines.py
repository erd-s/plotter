import random

from nextdraw import NextDraw


def create_lines(
    plotter: NextDraw,
    number_of_lines: int,
    origin_x: float,
    origin_y: float,
    max_height: float,
    max_width: float,
):
    start_x = origin_x
    start_y = origin_y + (max_height / 2)
    iterations = 300

    print(
        f"""
        origin_x: {origin_x}
        origin_y: {origin_y}
        start x: {start_x}
        start y: {start_y}
        max width: {max_width}
        max height: {max_height}
        iterations: {iterations}
        """
    )

    for _ in range(number_of_lines):
        points = [[start_x, start_y]]

        for i in range(iterations):
            previous_x = points[i][0]
            previous_y = points[i][1]

            x = previous_x + (max_width / iterations)
            y = previous_y + random.uniform(max_height / -50, max_height / 50)

            while y < origin_y or y > origin_y + max_height:
                y = previous_y + random.uniform(max_height / -100, max_height / 100)

            if x > (origin_x + max_width):
                break

            points.append([x, y])

        plotter.moveto(points[0][0], points[0][1])
        plotter.pendown()
        plotter.draw_path(points)
