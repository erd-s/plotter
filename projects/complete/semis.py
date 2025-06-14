from utils.plotter_interface import PlotterInterface
from projects.circles.half_circles_grid import HalfCircleGrid
from projects.margin import draw_margin


def run(plotter: PlotterInterface):
    # project to run
    project = HalfCircleGrid(half_circles_per_square=7)
    draw_margin(plotter, delta=-0.5)
    draw_margin(plotter, delta=-0.4)
    draw_margin(plotter, delta=-0.3)
    project.create_object_grid(plotter=plotter)
