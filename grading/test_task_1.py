"""Grades task 1."""
import inspect
import pathlib

import pytest
from matplotlib.figure import Figure

from .utils import verbose, check_import, check_file, check_dir, temp_dir


@verbose
def test_import_mandelbrot():
    """
    Attempts to import `mandelbrot`.

    This requires installing task 1 as a package. The recommended way to
    achieve this when using conda as a package manager is to
        - First, run `flit init` to create a `pyproject.toml` file
        - Next,run `flit install --symlink` to install into the conda env
    """
    check_import("mandelbrot")


@verbose
def test_module_hierarchy():
    """
    Checks that the requested module hierarchy is adhered to.

    Hint: the requested hierarchy is

        mandelbrot
        ├── fractals.py
        ├── __init__.py
        ├── README.rst
        ├── scripts
        │   ├── __init__.py
        │   ├── julia.py
        │   └── mandelbrot.py
        ├── tests
        │   ├── __init__.py
        │   └── test_utils.py
        └── utils.py
    """
    assert check_dir("mandelbrot")
    assert check_file("mandelbrot", "fractals.py")
    assert check_dir("mandelbrot", "scripts")
    assert check_file("mandelbrot", "scripts", "julia.py")
    assert check_file("mandelbrot", "scripts", "mandelbrot.py")
    assert check_dir("mandelbrot", "tests")
    assert check_file("mandelbrot", "tests", "test_utils.py")
    assert check_file("mandelbrot", "utils.py")


@verbose
def test_import_modules():
    """
    Attempts to import the following modules and submodules:

        - `mandelbrot`
        - `mandelbrot.fractals`
        - `mandelbrot.utils`
        - `mandelbrot.scripts`
        - `mandelbrot.scripts.mandelbrot`
        - `mandelbrot.scripts.julia`
        - `mandelbrot.tests`
        - `mandelbrot.tests.test_utils`
    """
    check_import("mandelbrot")
    check_import("mandelbrot.fractals")
    check_import("mandelbrot.utils")
    check_import("mandelbrot.scripts")
    check_import("mandelbrot.scripts.mandelbrot")
    check_import("mandelbrot.scripts.julia")
    check_import("mandelbrot.tests")
    check_import("mandelbrot.tests.test_utils")


@verbose
def test_utils():
    """
    Runs the tests in `mandelbrot.tests.test_utils`.
    """
    from mandelbrot.tests.test_utils import test_complex_grid, test_quadratic_map, test_get_pixel

    test_complex_grid()
    test_quadratic_map()
    test_get_pixel()


@verbose
def test_too_many_pixels():
    """
    Runs the `complex_grid` function with a too-high resolution.

    This should fail with an AssertionError, and show a helpful
    error message.
    """
    from mandelbrot.utils import complex_grid, MAX_PIXELS

    assert MAX_PIXELS == int(1e6), "`MAX_PIXELS` should not be changed prior to testing"

    # Test that it works normally
    _ = complex_grid(complex(0, 0), 1, resolution=1000)

    with pytest.raises(AssertionError):
        _ = complex_grid(complex(0, 0), 1, resolution=10000)
        _ = complex_grid(complex(0, 0), 1, resolution=1001)  # one above max
