"""Grades task 1."""
import inspect
import pathlib

import pytest
from matplotlib.figure import Figure

from .utils import verbose, check_import, check_file, check_dir, temp_dir


@verbose
def grade_import_task_1():
    """
    Attempts to import `ceres_workshop.task_1`.
    """
    check_import("ceres_workshop.task_1")


@verbose
def grade_module_hierarchy():
    """
    Checks that the requested module hierarchy is adhered to.

    Hint: the requested hierarchy is

        ceres_workshop
        ├── __init__.py
        └── task_1
            ├── fractals.py
            ├── __init__.py
            ├── main.py
            └── utils.py
    """
    assert check_dir("ceres_workshop", "task_1")
    assert check_file("ceres_workshop", "task_1", "main.py")
    assert check_file("ceres_workshop", "task_1", "fractals.py")
    assert check_file("ceres_workshop", "task_1", "utils.py")


@verbose
def grade_import_submodules():
    """
    Attempts to import the following submodules:

        - `ceres_workshop.task_1.main`
        - `ceres_workshop.task_1.fractals`
        - `ceres_workshop.task_1.utils`
    """
    check_import("ceres_workshop.task_1.main")
    check_import("ceres_workshop.task_1.fractals")
    check_import("ceres_workshop.task_1.utils")


@verbose
@pytest.mark.timeout(1)
def grade_bad_grid():
    """
    Runs the `complex_grid` function with bad grid parameters.

    This should fail gracefully, raising `GridError` along with
    a helpful error message.
    """
    from ceres_workshop.task_1.utils import complex_grid, GridError

    with pytest.raises(GridError):
        _ = complex_grid(xmin=1, xmax=-1)
        _ = complex_grid(ymin=1, ymax=-1)
        _ = complex_grid(res=0)
        _ = complex_grid(res=10)


@verbose
def grade_mandelbrot():
    """
    Runs the `mandelbrot` function, which should return a matplotlib `Figure`.

    The function is run both with and without explicitly passing a value
    for `cmap`, the colour map for the plot.
    """
    from ceres_workshop.task_1.fractals import mandelbrot

    out = mandelbrot(
        res=0.1,
        xmin=-2.025,
        xmax=0.6,
        ymin=-1.125,
        ymax=1.125,
    )
    assert isinstance(out, Figure)

    out = mandelbrot(
        res=0.1,
        xmin=-2.025,
        xmax=0.6,
        ymin=-1.125,
        ymax=1.125,
        cmap="viridis",
    )
    assert isinstance(out, Figure)


@verbose
def grade_julia():
    """
    Runs the `julia` function, which should return a matplotlib `Figure`.

    As with `mandelbrot`, the function is run both with and without `cmap`.
    """
    from ceres_workshop.task_1.fractals import julia

    out = julia(
        res=0.1,
        xmin=-0.9,
        xmax=0.9,
        ymin=-1.15,
        ymax=1.15,
        re_c=0.36,
        im_c=0.05,
    )
    assert isinstance(out, Figure)

    out = julia(
        res=0.1,
        xmin=-0.9,
        xmax=0.9,
        ymin=-1.15,
        ymax=1.15,
        re_c=0.36,
        im_c=0.05,
        cmap="viridis",
    )
    assert isinstance(out, Figure)


@verbose
def grade_import_main_func():
    """
    Attempts to import the `main` in two ways.

        - `ceres_workshop.task_1.main.main`
        - `ceres_workshop.task_1.main`

    These two functions should be the same!
    """
    from ceres_workshop.task_1.main import main
    from ceres_workshop.task_1 import main as main_from_init

    assert main is main_from_init


@verbose
def grade_main_annotations():
    """
    Inspects the signature of `main` for type annotations.
    """
    from ceres_workshop.task_1.main import main

    signature = inspect.signature(main)
    assert all(
        [
            param.annotation is not inspect._empty
            for param in signature.parameters.values()
        ]
    )


@verbose
def grade_main():
    """
    Calls the `main` function and checks for the expected saved image.
    """
    from ceres_workshop.task_1 import main

    with temp_dir():
        main(
            res=0.1,
            xmin=-2.025,
            xmax=0.6,
            ymin=-1.125,
            ymax=1.125,
            cmap="viridis",
            output="figure.png",
        )
        assert pathlib.Path(
            "figure.png"
        ).exists(), "Expected to find `figure.png` after running `main`, but it doesn't exist"
