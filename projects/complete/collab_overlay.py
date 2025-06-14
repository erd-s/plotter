from utils.plotter_interface import PlotterInterface
from projects.rectangles.square_overlay_grid import SquareOverlayGrid


def create_collab_overlay(plotter: PlotterInterface):
    project = SquareOverlayGrid(grid_size=25, density=65, width_ratio=0.5)
    project.create_object_grid(plotter=plotter)
