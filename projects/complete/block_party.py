from projects.block_party.block_party_grid import BlockPartyGrid
from utils.plotter_interface import PlotterInterface
from projects.margin import draw_margin
from config import DOC_HEIGHT, DOC_WIDTH


def draw_block_party(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    width: float,
    height: float,
):
    # 20 for 9x12 w/ fat Prismacolor Marker
    # 15 for A5 .12 pt pen
    # 30-35 for A5 .05 pt pen
    # grid_size = 18 if DOC_HEIGHT == 8.27 else 30
    project = BlockPartyGrid(
        grid_size_horizontal=18,
        grid_size_vertical=25,
        origin_x=origin_x,
        origin_y=origin_y,
        width=width,
        height=height,
    )
    project.draw_object_grid(plotter=plotter)
    draw_margin(plotter=plotter, delta=-0.05)
