from utils.plotter_interface import PlotterInterface


def draw_rectangle_with_bounds(
    plotter: PlotterInterface,
    height: float,
    width: float,
    center_x: float,
    center_y: float,
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
):
    ax = center_x - (width * 0.5)
    ay = center_y - (height * 0.5)
    bx = ax
    by = center_y + (height * 0.5)
    cx = center_x + (width * 0.5)
    cy = by
    dx = cx
    dy = ay

    points = []
    out_of_bounds = False

    if ax < x_min:
        ax = x_min
        out_of_bounds = True
    if ay < y_min:
        ay = y_min
        out_of_bounds = True

    points.append([ax, ay])

    if bx < x_min:
        bx = x_min
        out_of_bounds = True
    if by > y_max:
        by = y_max
        out_of_bounds = True

    points.append([bx, by])

    if cx > x_max:
        cx = x_max
        out_of_bounds = True
    if cy > y_max:
        cy = y_max
        out_of_bounds = True

    points.append([cx, cy])

    if dx > x_max:
        dx = x_max
        out_of_bounds = True
    if dy < y_min:
        dy = y_min
        out_of_bounds = True
    points.append([dx, dy])

    if ax < x_min:
        ax = x_min
        out_of_bounds = True
    if ay < y_min:
        ay = y_min
        out_of_bounds = True

    points.append([ax, ay])

    if not out_of_bounds:
        plotter.draw_path(points)
    else:
        for i, point in enumerate(points):
            if i + 1 == len(points):
                continue
            xs = point[0]
            ys = point[1]
            xe = points[i + 1][0]
            ye = points[i + 1][1]

            if xs == xe == x_min or xs == xe == x_max:
                continue

            if ys == ye == y_min or ys == ye == y_max:
                continue

            plotter.moveto(xs, ys)
            plotter.lineto(xe, ye)


def draw_rectangle(
    plotter: PlotterInterface,
    height: float,
    width: float,
    center_x: float,
    center_y: float,
):
    ax = center_x - (width * 0.5)
    ay = center_y - (height * 0.5)
    bx = ax
    by = center_y + (height * 0.5)
    cx = center_x + (width * 0.5)
    cy = by
    dx = cx
    dy = ay
    points = [[ax, ay], [bx, by], [cx, cy], [dx, dy], [ax, ay]]
    plotter.draw_path(points)
    print(f"Rectangle width: {width}")
    print(f"Rectangle height: {height}")


def rectangle_path(
    height: float,
    width: float,
    center_x: float,
    center_y: float,
):

    ax = center_x - (width * 0.5)
    ay = center_y - (height * 0.5)
    bx = ax
    by = center_y + (height * 0.5)
    cx = center_x + (width * 0.5)
    cy = by
    dx = cx
    dy = ay

    points = [[ax, ay], [bx, by], [cx, cy], [dx, dy], [ax, ay]]
    return points
