from projects.circles.circle_overlay_grid import CircleOverlayGrid
from projects.rectangles.square_overlay_grid import SquareOverlayGrid
from utils.plotter_interface import PlotterInterface


def draw_circle_square_overlay_grid(plotter: PlotterInterface):
    grid_size = 25
    density = 60
    width_ratio = 1 / 2.5

    project = SquareOverlayGrid(density=density, width_ratio=width_ratio)
    project.draw_object_grid(plotter=plotter)
    print(
        f"Square Density: {round((project.total_squares / (project.total_squares + project.total_skips)), 2) * 100}%"
        f"Total Squares: {project.total_squares} of {grid_size * grid_size}"
    )

    project = CircleOverlayGrid(
        density=density, width_ratio=width_ratio, grid_size=grid_size
    )
    project.draw_object_grid(plotter=plotter)
    print(
        f"Circle Density: {round((project.total_circles / (project.total_circles + project.total_skips)), 2) * 100}%"
        f"Total Circles: {project.total_circles} of {grid_size * grid_size}"
    )
