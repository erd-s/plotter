from utils.plotter_interface import PlotterInterface
from projects.circles.circle import (
    circle_path,
    draw_circle,
    draw_filled_circle,
    filled_circle_paths,
)
from utils.transform import rotated_path


def draw_insect_eye(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    initial_radius: float,
    iterations: int,
):
    radius = initial_radius
    distance_to_center = 0
    total_number_of_circles = 0

    for i in range(iterations):
        radius = radius * 0.74 if i != 0 else initial_radius
        print(f"diameter = {radius * 2}")
        circles_to_draw = (6 * i) + i
        circle_center_x = center_x + distance_to_center + radius
        distance_to_center = (
            abs(center_x - circle_center_x) + (radius if i != 0 else 0) + (radius / 10)
        )

        if i == 0:
            draw_circle(
                plotter=plotter,
                center_x=center_x,
                center_y=center_y,
                radius=initial_radius,
            )
            total_number_of_circles += 1
        else:
            for n in range(circles_to_draw):
                path = circle_path(
                    center_x=circle_center_x, center_y=center_y, radius=radius
                )
                rotation_degrees = (360 / circles_to_draw) * n
                rotated_circle_path = rotated_path(
                    path=path,
                    degrees=rotation_degrees,
                    rotation_x=center_x,
                    rotation_y=center_y,
                )
                plotter.draw_path(rotated_circle_path)
                total_number_of_circles += 1

    print(f"total # of circles = {total_number_of_circles}")


def draw_insect_eye_filled(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    initial_radius: float,
    iterations: int,
    pen_width_mm: float,
):
    radius = initial_radius
    distance_to_center = 0
    total_number_of_circles = 0

    for i in range(iterations):
        radius = radius * 0.74 if i != 0 else initial_radius
        print(f"diameter = {radius * 2}")
        circles_to_draw = (6 * i) + i
        circle_center_x = center_x + distance_to_center + radius
        distance_to_center = (
            abs(center_x - circle_center_x) + (radius if i != 0 else 0) + (radius / 10)
        )

        if i == 0:
            draw_filled_circle(
                plotter=plotter,
                center_x=center_x,
                center_y=center_y,
                radius=initial_radius,
                pen_width_mm=pen_width_mm,
            )
            total_number_of_circles += 1
        else:
            for n in range(circles_to_draw):
                paths = filled_circle_paths(
                    center_x=circle_center_x,
                    center_y=center_y,
                    radius=radius,
                    pen_width_mm=pen_width_mm,
                )
                for path in paths:
                    rotation_degrees = (360 / circles_to_draw) * n
                    rotated_circle_path = rotated_path(
                        path=path,
                        degrees=rotation_degrees,
                        rotation_x=center_x,
                        rotation_y=center_y,
                    )
                    plotter.draw_path(rotated_circle_path)
                    total_number_of_circles += 1

    print(f"total # of circles = {total_number_of_circles}")
