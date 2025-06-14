from projects.block_party.block_party_grid import BlockPartyGrid
from utils.plotter_interface import PlotterInterface
from projects.margin import draw_margin


def create_block_party(plotter: PlotterInterface):
    # 20 for 9x12 w/ fat Prismacolor Marker
    # 15 for A5 .12 pt pen
    # 30-35 for A5 .05 pt pen
    project = BlockPartyGrid(grid_size=18)
    project.create_object_grid(plotter=plotter)
    draw_margin(plotter=plotter, delta=-0.05)


# 9x12 w/ Fat Prismacolor Marker
#    DOC_HEIGHT = 8.5
#    MARGIN_TOP = 0.525
#    MARGIN_BOTTOM = 0.25
#
#    DOC_WIDTH = 11
#    MARGIN_LEFT = 1.1
#    MARGIN_RIGHT = 0.1
