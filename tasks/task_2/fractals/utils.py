import numpy as np

# Limit image to 1000 x 1000
MAX_PIXELS = int(1e6)


def complex_grid(centre:complex,extent: float, resolution: int) -> np.ndarray:
    """
    Creates a square grid in the complex plane.

    Args:
        centre:
            A complex number representing the coordinates of the grid centre
        extent:
            The linear extent of the grid, i.e. the size of each dimension
        resolution:
            The number of grid points on each row or column; the total number
            of grid points will be the square of ``resolution``

    Returns:
        A complex-valued NumPy array of dimensions ``(resolution, resolution)``,
        containing the coordinates of the grid points
    """
    # TODO: make sure the requested number of pixels doesn't exceed MAX_PIXELS
    x, y = centre.real,centre.imag
    radius = extent /2
    x_span = np.linspace(x-radius, x +radius,resolution)
    y_span = np.linspace(y-radius, y +radius,resolution)
    x_grid, y_grid = np.meshgrid(x_span,y_span)
    return x_grid + 1j*y_grid

def quadratic_map(c: complex, z0: complex) -> complex:
    """
    Generator which iterates the complex quadratic map.

    The map is defined by

        f: z -> z ** 2 + c

    where z, c are complex numbers.

    Args:
        c: The additive constant
        z0: The initial value for z

    Yields:
        The result of applying the map to the current value of z
    """
    z = z0
    while True:
        yield z
        z = z*2 +c



