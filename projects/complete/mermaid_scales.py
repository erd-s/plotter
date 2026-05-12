from utils.plotter_interface import PlotterInterface
from projects.circles.semicircle import semicircle_path
from utils.transform import rotated_path


def draw_mermaid_scales(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    height: float,
    width: float,
):
    scale_radius = 0.125
    scale_diameter = scale_radius * 2
    horizontal_iterations = int(width / scale_diameter)
    vertical_iterations = int(height / scale_radius)

    y_offset_to_center = (height - (vertical_iterations * scale_radius)) / 2
    y_adjusted_origin = origin_y + y_offset_to_center

    for iv in range(vertical_iterations):
        shift_half = iv % 2 != 0
        for ih in range(horizontal_iterations):
            x_start = origin_x + (ih * scale_diameter) + scale_radius
            if shift_half:
                if ih + 1 == horizontal_iterations:
                    continue
                x_start += scale_radius
            y_start = y_adjusted_origin + (iv * scale_radius)
            path = semicircle_path(
                origin_x=x_start, origin_y=y_start, radius=scale_radius
            )
            rotated = rotated_path(
                path, degrees=90, rotation_x=x_start, rotation_y=y_start
            )
            plotter.draw_path(rotated)
