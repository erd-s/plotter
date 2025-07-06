from matplotlib.patches import Patch


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
