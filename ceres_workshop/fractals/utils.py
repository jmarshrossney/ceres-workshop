"""
Module containing assorted utils.
"""
from pathlib import Path
from warnings import warn

import numpy as np
import sympy
from PIL import Image

# Limit image to 1000 x 1000
MAX_PIXELS = int(1e6)


def complex_grid(
    centre: complex,
    extent: float,
    resolution: int,
) -> np.ndarray:
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
    assert (
        resolution ** 2 <= MAX_PIXELS
    ), f"Maximum number of pixels exceeded: {resolution}^2 > {MAX_PIXELS}"
    x, y = centre.real, centre.imag
    radius = extent / 2
    x_span = np.linspace(x - radius, x + radius, resolution)
    y_span = np.linspace(y - radius, y + radius, resolution)
    x_grid, y_grid = np.meshgrid(x_span, y_span)
    return x_grid + 1j * y_grid


def quadratic_map(c: complex, z0: complex) -> complex:
    """
    Generator which iterates the complex quadratic map.

    The map is defined by

    .. math::

        z_n \mapsto z_{n+1} = z_n^2 + c \qquad z_0, c \in \mathbb{C}

    Args:
        c: The additive constant :math:`c`
        z0: The initial value :math:`z_0`

    Yields:
        The result of applying the map to the current value of z
    """
    z = z0
    while True:
        yield z
        z = z ** 2 + c


def make_gif(
    images: list[Image.Image], output: str, duration: int = 100
) -> None:
    """
    Creates a GIF from a sequence of images.

    Args:
        images:
            A list of PIL Images
        output:
            The name of or path to the output GIF file
        duration:
            The duration of each frame of the GIF, in milliseconds
    """

    if Path(output).exists():
        warn(f"`{output}` already exists and will be overridden!")

    first, *rest = images
    first.save(
        output,
        format="GIF",
        append_images=rest,
        save_all=True,
        duration=duration,
        loop=0,
    )


def get_quadratic_map_roots(n: int) -> list[complex]:
    r"""
    Uses SymPy to compute complex roots of the quadratic map.

    We compute the roots of the polynomial :math:`f_n(c)`, where
    
    .. math::

        f_1 &= c \\
        f_2 &= c^2 + c \\
        f_3 &= (c^2 + c)^2 + c \\
        \vdots

    i.e. those values :math:`\{r_n\}` for which :math:`f_n(r_n) = 0`.

    Args:
        n: Number of iterations of the map, i.e. the polynomial order
    """
    assert isinstance(n, int), "n should be an integer"
    assert n >= 1, "n should be 1 or greater"
    c = sympy.var("c")
    z = sympy.Poly(c)  # z_1 = c
    for _ in range(1, n):
        z = sympy.Poly(z ** 2 + c)  # z_n

    roots = z.nroots()
    return [complex(root) for root in roots]
