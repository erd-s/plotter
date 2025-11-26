from matplotlib import transforms
from utils.matplotlibutils import path_from_coordinate_list, coordinate_list_from_path


def rotate(path: [(float, float)], degrees: int, rotation_point: (int, int)):
    mpl_path = path_from_coordinate_list(coordinate_list=path)
    rotation = transforms.Affine2D().rotate_deg_around(
        rotation_point[0], rotation_point[1], degrees
    )
    mpl_rotated_path = mpl_path.transformed(rotation)
    return coordinate_list_from_path(mpl_rotated_path)
