from matplotlib import transforms
from utils.matplotlibutils import path_from_coordinate_list, coordinate_list_from_path
import itertools


def rotate(path: [(float, float)], degrees: int, rotation_x: float, rotation_y: float):
    mpl_path = path_from_coordinate_list(coordinate_list=path)
    rotation = transforms.Affine2D().rotate_deg_around(rotation_x, rotation_y, degrees)
    mpl_rotated_path = mpl_path.transformed(rotation)
    return coordinate_list_from_path(mpl_rotated_path)


def centered_paths(paths: [[(float, float)]], around_x: float, around_y: float):
    coordinates = list(itertools.chain.from_iterable(paths))
    x_coordinates = []
    y_coordinates = []
    for i, coordinate in enumerate(coordinates):
        x_coordinates.append(coordinate[0])
        y_coordinates.append(coordinate[1])

    min_x: float = min(x_coordinates)
    max_x: float = max(x_coordinates)
    min_y: float = min(y_coordinates)
    max_y: float = max(y_coordinates)

    original_center_x = (min_x + max_x) / 2
    original_center_y = (min_y + max_y) / 2

    tx = around_x - original_center_x
    ty = around_y - original_center_y

    center_paths = []
    for path in paths:
        translation = transforms.Affine2D().translate(tx, ty)
        mpl_path = path_from_coordinate_list(coordinate_list=path)
        mpl_centered_path = mpl_path.transformed(translation)
        coordinate_list = coordinate_list_from_path(mpl_centered_path)
        center_paths.append(coordinate_list)

    return center_paths
