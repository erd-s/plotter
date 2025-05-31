from nextdraw import NextDraw
from projects.rectangles.square_overlay_grid import SquareOverlayGrid

def create_collab_overlay(plotter: NextDraw):
    project = SquareOverlayGrid(grid_size=25, density=65, width_ratio=0.5)
    project.create_object_grid(plotter=plotter)