from functools import partial
import sys

import numpy as np

sys.path.insert(0, "../")

from fractals import Mandelbrot
from utils import complex_grid, quadratic_map


def test_complex_grid():
    """
    Check that the grid is as expected.
    """

    # Case 1
    centre = complex(0, 0)
    extent = 0.2  # -0.1 -> 0.1
    resolution = 3  # [-0.1, 0, 0.1]
    grid = complex_grid(centre, extent, resolution)
    assert grid.shape == (3, 3)
    x_span = grid.real[0, :]
    y_span = grid.imag[:, 0]
    assert np.allclose(x_span, [-0.1, 0.0, 0.1])
    assert np.allclose(y_span, [-0.1, 0.0, 0.1])

    # Case 2
    centre = complex(1, 0)
    extent = 0.2  # 0.9 -> 1.1
    resolution = 3  # [0.9, 1.0, 1.1]
    grid = complex_grid(centre, extent, resolution)
    assert grid.shape == (3, 3)
    x_span = grid.real[0, :]
    y_span = grid.imag[:, 0]
    assert np.allclose(x_span, [0.9, 1.0, 1.1])
    assert np.allclose(y_span, [-0.1, 0.0, 0.1])


def test_quadratic_map():
    """
    Test the quadratic map f: z -> z^2 + c
    """

    # Case 1
    f = quadratic_map(c=0, z0=0)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 0  # 0
    assert z1 == 0  # 0^2 + 0
    assert z2 == 0  # (0^2 + 0)^2 + 0

    # Case 2
    f = quadratic_map(c=0, z0=1)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 1  # 1
    assert z1 == 1  # 1^2 + 0
    assert z1 == 1  # (1^2 + 0)^2 + 0

    # Case 3
    f = quadratic_map(c=1, z0=0)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 0  # 0
    assert z1 == 1  # 0^2 + 1
    assert z2 == 2  # (0^2 + 1)^2 + 1

    # Case 4
    f = quadratic_map(c=1, z0=1)
    z0 = next(f)
    z1 = next(f)
    z2 = next(f)
    assert z0 == 1  # 1
    assert z1 == 2  # 1^2 + 1
    assert z2 == 5  # (1^2 + 1)^2 + 1


def test_get_pixel():
    """
    Tests some known points in the Mandelbrot set.
    """
    pixel = partial(Mandelbrot.get_pixel, z0=0)

    # Check boundaries
    for c in (complex(-2, 0), complex(2, 0), complex(0, -2), complex(0, 2)):
        assert pixel(c) == 1

    # Check roots of quadratic map with z0 = 0:
    for c in (
        complex(0, 0),
        complex(-1, 0),
        complex(-1.7548776662466927, 0),
        complex(-0.12256116687665362, -0.7448617666197442),
        complex(-0.12256116687665362, +0.7448617666197442),
        complex(-1.9407998065294847, 0),
        complex(-1.3107026413368328, 0),
    ):
        assert pixel(c) == 255

if __name__ == "__main__":
    test_complex_grid()
    test_quadratic_map()
    test_get_pixel()

