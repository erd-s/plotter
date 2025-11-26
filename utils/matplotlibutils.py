from matplotlib.patches import Patch
from matplotlib.path import Path
from numpy import ndarray, array


def path_from_patch(patch: Patch):
    path = patch.get_path().vertices
    transform = patch.get_patch_transform()
    path_transformed = transform.transform(path).flat
    x_points = []
    y_points = []
    for i, p in enumerate(path_transformed):
        if i % 2 == 0:
            x_points.append(p)
        else:
            y_points.append(p)

    path_points = []
    for i, x in enumerate(x_points):
        path_points.append([x, y_points[i]])

    return path_points


def joined_coordinate_list(x_points: ndarray, y_points: ndarray):
    x = []
    for x_point in x_points:
        x.append(x_point)

    y = []
    for y_point in y_points:
        y.append(y_point)

    path_points = []
    for i, x in enumerate(x):
        path_points.append([x, y[i]])

    return path_points


def path_from_coordinate_list(coordinate_list: [(float, float)]):
    n2_array = array(coordinate_list, dtype=float)
    return Path(vertices=n2_array)


def coordinate_list_from_path(path: Path):
    coordinate_list = []
    for arr in path.iter_segments():
        x = arr[0][0]
        y = arr[0][1]
        coordinate_list.append([x, y])
    return coordinate_list
