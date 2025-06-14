from utils.plotter_interface import PlotterInterface

from projects.irregular_cubes.irregular_cube import create_cube
from projects.object_grid import ObjectGrid


class IrregularCubeGrid(ObjectGrid):
    def object_logic(self, plotter: PlotterInterface):
        create_cube(
            plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_center_y,
            width=self.square_width * 0.35,
            height=self.square_height * 0.35,
        )
