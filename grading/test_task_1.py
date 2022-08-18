"""
Runs a set of tests against task 1, giving the user a score.

These tests can be run locally by executing

.. code-block:: sh

    pytest grading/test_task_1.py -s --tb=no

in the root of the repository.

They should also run upon pushes to the ``task-1`` and ``main`` branches.
"""
import inspect
import random
import string

import pytest

from utils import verbose, check_import, check_file, check_dir, temp_dir, REPO_ROOT


@verbose
def test_module_hierarchy():
    """
    Checks that the requested module hierarchy is adhered to.

    Hint: the requested hierarchy is

        task_1
        ├── fractals.py
        ├── __init__.py
        ├── README.rst
        ├── scripts
        │   ├── __init__.py
        │   ├── julia.py
        │   └── task_1.py
        ├── tests
        │   ├── __init__.py
        │   └── test_utils.py
        └── utils.py
    """
    assert check_dir("task_1")
    assert check_file("task_1", "fractals.py")
    assert check_dir("task_1", "scripts")
    assert check_file("task_1", "scripts", "julia.py")
    assert check_file("task_1", "scripts", "mandelbrot.py")
    assert check_dir("task_1", "tests")
    assert check_file("task_1", "tests", "test_utils.py")
    assert check_file("task_1", "utils.py")


@verbose
def test_import_task_1():
    """
    Attempts to import `task_1` module.

    For this to work we need to install ``task_1`` as a package.

    To make ``task_1`` installable, it is recommended to create a
    ``pyproject.toml`` file in the `task-1` directory. This can be acheived
    using the Flit package. Consult the workshop notes for details!
    """
    check_import("task_1")


@verbose
def test_import_all_modules():
    """
    Attempts to import the following modules and submodules:

    * ``task_1``
    * ``task_1.fractals``
    * ``task_1.utils``
    * ``task_1.scripts``
    * ``task_1.scripts.mandelbrot``
    * ``task_1.scripts.julia``
    * ``task_1.tests``
    * ``task_1.tests.test_utils``
    """
    check_import("task_1")
    check_import("task_1.fractals")
    check_import("task_1.utils")
    check_import("task_1.scripts")
    check_import("task_1.scripts.mandelbrot")
    check_import("task_1.scripts.julia")
    check_import("task_1.tests")
    check_import("task_1.tests.test_utils")


@verbose
def test_utils():
    """
    Runs the tests in `task_1.tests.test_utils`.
    """
    from task_1.tests.test_utils import (
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
    from task_1.utils import complex_grid, MAX_PIXELS

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

    * ``task_1.scripts.mandelbrot.plot``
    * ``task_1.scripts.julia.plot``

    And checks that the type annotations are

    * ``centre: complex``
    * ``extent: float``
    * ``resolution: int``
    * ``cmap: str``
    * ``output: str``
    * ``c_value: complex`` (julia only)
    * Return value: ``None``
    """
    from task_1.scripts.mandelbrot import plot as mandelbrot_plot
    from task_1.scripts.julia import plot as julia_plot

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

    * ``task_1.scripts.mandelbrot.plot``
    * ``task_1.scripts.julia.plot``

    should take a ``cmap`` argument, which is a string corresponding to a
    matplotlib colourmap. This argument should have a default value so that
    we don't have to specify the colourmap every time.
    """
    from matplotlib.cm import get_cmap

    from task_1.scripts.mandelbrot import plot as mandelbrot_plot
    from task_1.scripts.julia import plot as julia_plot

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

    * ``task_1.scripts.mandelbrot.plot``
    * ``task_1.scripts.julia.plot``

    are run the argument ``output`` set to a random string + ``.png``, and
    with a very low resolution to speed things up. The default ``cmap``
    is used.
    """
    from task_1.scripts.mandelbrot import plot as mandelbrot_plot
    from task_1.scripts.julia import plot as julia_plot

    centre = complex(0, 0)
    extent = 1
    resolution = 10
    c_value = complex(0, -1)

    task_1_output = (
        "".join([random.choice(string.ascii_lowercase) for _ in range(5)]) + ".png"
    )
    julia_output = (
        "".join([random.choice(string.ascii_lowercase) for _ in range(5)]) + ".png"
    )

    with temp_dir():
        task_1_plot(
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

    This checks the package directory ``task_1`` for any image files.
    Specifically, it checks for files with any extension corresponding
    to a filetype supported by ``plt.savefig``, as well as ``.gif`` files.

    You can upload larger files such as images to GitHub, but care should
    be taken not to over-do it. An appropriate place to upload images is
    in an `assets` directory in the root of the repository, though the
    most important thing is to avoid uploading extra rubbish along with
    the source code.
    """
    import matplotlib.pyplot as plt

    package_dir = REPO_ROOT / "task-1" / "task_1"
    assert package_dir.is_dir(), f"`{package_dir}` is not a directory"

    matplotlib_supported_filetypes = list(
        plt.gcf().canvas.get_supported_filetypes().keys()
    )
    for suffix in matplotlib_supported_filetypes + ["gif"]:
        files = package_dir.rglob(f"*.{suffix}")
        assert not files, f".{suffix} file(s) found in `{package_dir}`"
