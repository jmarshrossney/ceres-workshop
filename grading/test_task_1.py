"""
Runs a set of tests against task 1, giving the user a score.

These tests can be run locally by executing

.. code_block:: bash

    pytest grading/test_task_1.py -s --tb=no

in the root of the repository.

They should also run upon pushes to the ``task-1`` and ``main`` branches.
"""
import inspect
import pathlib
import random
import string

import pytest
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.cm import get_cmap

from .utils import verbose, check_import, check_file, check_dir, temp_dir, REPO_ROOT


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
def test_import_mandelbrot():
    """
    Attempts to import `mandelbrot` module.

    For this to work we need to install ``mandelbrot`` as a package.

    To make ``mandelbrot`` installable, it is recommended to create a
    ``pyproject.toml`` file in the `task-1` directory. This can be acheived
    using the Flit package. Consult the workshop notes for details!
    """
    check_import("mandelbrot")


@verbose
def test_import_all_modules():
    """
    Attempts to import the following modules and submodules:

    * ``mandelbrot``
    * ``mandelbrot.fractals``
    * ``mandelbrot.utils``
    * ``mandelbrot.scripts``
    * ``mandelbrot.scripts.mandelbrot``
    * ``mandelbrot.scripts.julia``
    * ``mandelbrot.tests``
    * ``mandelbrot.tests.test_utils``
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
    from mandelbrot.tests.test_utils import (
        test_complex_grid,
        test_quadratic_map,
        test_get_pixel,
    )

    test_complex_grid()
    test_quadratic_map()
    test_get_pixel()


@verbose
def test_too_many_pixels():
    """
    Runs the `complex_grid` function with a too-high resolution.

    This should fail with an ``AssertionError``, and show a helpful
    error message.
    """
    from mandelbrot.utils import complex_grid, MAX_PIXELS

    assert MAX_PIXELS == int(1e6), "Please set `MAX_PIXELS = int(1e6)`"

    # Test that it works normally
    _ = complex_grid(complex(0, 0), 1, resolution=1000)

    with pytest.raises(AssertionError):
        _ = complex_grid(complex(0, 0), 1, resolution=10000)

    with pytest.raises(AssertionError):
        _ = complex_grid(complex(0, 0), 1, resolution=1001)  # one above max


@verbose
def test_script_annotations():
    """
    Inspects the signatures of `plot` functions for type annotations.

    Specifically, inspects the signatures of the following functions:

    * ``mandelbrot.scripts.mandelbrot.plot``
    * ``mandelbrot.scripts.julia.plot``

    And checks that the type annotations are

    * ``centre: complex``
    * ``extent: float``
    * ``resolution: int``
    * ``cmap: str``
    * ``output: str``
    * ``c_value: complex`` (julia only)
    * Return value: ``None``
    """
    from mandelbrot.scripts.mandelbrot import plot as mandelbrot_plot
    from mandelbrot.scripts.julia import plot as julia_plot

    for plot in (mandelbrot_plot, julia_plot):

        signature = inspect.signature(plot)
        parameters = signature.parameters
        assert all(
            [param.annotation is not inspect._empty for param in parameters.values()]
        ), f"One or more of the arguments to `{plot.__module__}.{plot.__name__}` does not have a type annotation"

        assert parameters["centre"].annotation is complex
        assert parameters["extent"].annotation is float
        assert parameters["resolution"].annotation is int
        assert parameters["cmap"].annotation is str
        assert parameters["output"].annotation is str
        if "c_value" in parameters:
            assert parameters["c_value"].annotation is complex

        assert (
            signature.return_value is not inspect._empty
        ), "Don't forget to annotate the return value!"
        assert signature.return_value is None, "Return value should be `None`"


@verbose
def test_default_cmap():
    """
    Checks that the `plot` functions have a default colourmap.

    The functions

    * ``mandelbrot.scripts.mandelbrot.plot``
    * ``mandelbrot.scripts.julia.plot``

    should take a ``cmap`` argument, which is a string corresponding to a
    matplotlib colourmap. This argument should have a default value so that
    we don't have to specify the colourmap every time.
    """
    from mandelbrot.scripts.mandelbrot import plot as mandelbrot_plot
    from mandelbrot.scripts.julia import plot as julia_plot

    for plot in (mandelbrot_plot, julia_plot):

        signature = inspect.signature(plot)
        parameters = signature.parameters
        assert (
            parameters["cmap"].default is not inspect._empty
        ), "The `cmap` argument in `{plot.__module__}.{plot.__name__}` doesn't have a default value"

        # Check it's a valid cmap
        get_cmap(parameters["cmap"].default)


@verbose
def test_plot_scripts():
    """
    Runs plotting scripts and checks for a saved PNG image.

    The functions

    * ``mandelbrot.scripts.mandelbrot.plot``
    * ``mandelbrot.scripts.julia.plot``

    are run the argument ``output`` set to a random string + ``.png``, and
    with a very low resolution to speed things up. The default ``cmap``
    is used.
    """
    from mandelbrot.scripts.mandelbrot import plot as mandelbrot_plot
    from mandelbrot.scripts.julia import plot as julia_plot

    centre = complex(0, 0)
    extent = 1
    resolution = 10
    c_value = complex(0, -1)

    mandelbrot_output = "".join(
        random.choice(string.ascii_lowercase) for _ in range(5)
    ) = ".png"
    julia_output = "".join(
        random.choice(string.ascii_lowercase) for _ in range(5)
    ) = ".png"

    with temp_dir():
        mandelbrot_plot(
            centre=centre,
            extent=extent,
            resolution=resolution,
            output=mandelbrot_output,
        )
        check_file(mandelbrot_output)

        julia_plot(
            c_value=c_value,
            centre=centre,
            extent=extent,
            resolution=resolution,
            output=julia_output,
        )
        check_file(julia_output)


@verbose
def test_no_plots_or_gifs():
    """
    Checks that plots and gifs aren't being uploaded to GitHub.

    This checks the package directory ``mandelbrot`` for any image files.
    Specifically, it checks for files with any extension corresponding
    to a filetype supported by ``plt.savefig``, as well as ``.gif`` files.

    You can upload larger files such as images to GitHub, but care should
    be taken not to over-do it. An appropriate place to upload images is
    in an `assets` directory in the root of the repository, though the
    most important thing is to avoid uploading extra rubbish along with
    the source code.
    """
    package_dir = ROOT_DIR / "task-1" / "mandelbrot"
    assert package_dir.is_dir(), f"`{package_dir}` is not a directory"

    matplotlib_supported_filetypes = list(
        plt.gcf().canvas.get_supported_filetypes().keys()
    )
    for suffix in matplotlib_supported_filetypes + ["gif"]:
        files = package_dir.rglob(f"*.{suffix}")
        assert not files, f".{suffix} file(s) found in `{package_dir}`"
