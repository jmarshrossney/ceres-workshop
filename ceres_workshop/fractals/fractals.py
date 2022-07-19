r"""
Module containing classes which visualise fractals in the complex plane.

The fractals implemented here are based on the complex quadratic map

.. math::

    z_n \mapsto z_{n+1} = z_n^2 + c \qquad z_0, c \in \mathbb{C} \, .

It can be shown that if :math:`z_n > 2` for any :math:`n`, then the map
will diverge, i.e. :math:`z_n \to \infty` as :math:`n \to \infty`.
    
The **Mandelbrot set** is a subset of :math:`\mathbb{C}` comprising complex
numbers :math:`c` for which the quadratic map remains finite for the
starting value of :math:`z_0 = 0`.

Similarly, **Julia sets** are subsets of :math:`\mathbb{C}` comprising
complex numbers :math:`z_0` for which the quadratic map remains finite
for some specific value of :math:`c`.

A two-dimensional visualisation of these sets uses a colour map to indicate
the number of iterations of the map required for :math:`z_n > 2`. Here an
8-bit representation is used, i.e. 256 different colours.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from PIL import Image
from tqdm.autonotebook import tqdm

from .utils import complex_grid, quadratic_map

FEIGENBAUM_DELTA = 4.669201609
FEIGENBAUM_POINT = -1.401155189

class Mandelbrot:
    r"""
    Class which generates visualisations of the Mandelbrot set.

    Args:
        centre:
            A complex number representing the coordinates of the centre
            of the image
        extent:
            The linear extent of the image, i.e. the size of each dimension
            in the complex plane
        resolution:
            The number of pixels on each row or column; the total number of
            pixels will be the square of ``resolution``
    """

    def __init__(
        self, centre: complex, extent: float, resolution: int
    ) -> None:
        self.grid = complex_grid(centre, extent, resolution)
        self.pixels = np.vectorize(self.get_pixel)(self.grid, 0)

    @staticmethod
    def get_pixel(c: complex, z0: complex) -> int:
        """
        Computes a single 8-bit pixel.

        Args:
            c: The additive constant
            z0: The initial value for z

        Returns:
            Integer between 0 and 255

        See Also: ``ceres_workshop.task_1.utils.quadratic_map``
        """
        for n, z in zip(range(256), quadratic_map(c, z0)):
            if abs(z) >= 2:
                break
        return n

    def get_figure(self, cmap: str = "viridis") -> plt.Figure:
        """
        Creates a matplotlib Figure visualising the Mandelbrot set.

        Args:
            cmap:
                The colour map used to colour pixels. For available colours
                see matplotlib documentation on colourmaps
        """
        grid_min, grid_max = self.grid.min(), self.grid.max()
        fig, ax = plt.subplots()

        ax.imshow(
            self.pixels,
            cmap=cmap,
            extent=(
                grid_min.real,
                grid_max.real,
                grid_min.imag,
                grid_max.imag,
            ),
            origin="lower",
        )

        ax.set_title(f"{type(self).__name__} Set")
        ax.set_xlabel("Real axis")
        ax.set_ylabel("Imaginary axis")
        fig.tight_layout()

        return fig

    def get_image(self, cmap: str = "viridis") -> Image.Image:
        """
        Creates a PIL (pillow) Image visualising the Mandelbrot set
        """
        cmap = get_cmap(cmap)
        image_array = np.uint8(cmap(self.pixels / 255) * 255)
        return Image.fromarray(image_array)


class Julia(Mandelbrot):
    """
    Class which generates visualisations of Julia sets.

    Args:
        c_value:
            The value of the complex additive constant in the quadratic map
        centre:
            A complex number representing the coordinates of the centre
            of the image
        extent:
            The linear extent of the image, i.e. the size of each dimension
            in the complex plane
        resolution:
            The number of pixels on each row or column; the total number of
            pixels will be the square of ``resolution``
    """

    def __init__(
        self,
        c_value: complex,
        centre: complex,
        extent: float,
        resolution: int,
    ) -> None:
        self.grid = complex_grid(centre, extent, resolution)
        self.pixels = np.vectorize(self.get_pixel)(c_value, self.grid)
