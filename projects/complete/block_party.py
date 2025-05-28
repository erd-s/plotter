from projects.block_party.block_party_grid import BlockPartyGrid
from nextdraw import NextDraw
from projects.margin import draw_margin


def create_block_party(plotter: NextDraw):
    project = BlockPartyGrid(grid_size=15)
    project.create_object_grid(plotter=plotter)
    draw_margin(plotter=plotter, delta=-0.05)
