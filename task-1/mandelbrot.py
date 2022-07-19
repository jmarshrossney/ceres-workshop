import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from PIL import Image


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






class Mandelbrot:
    """
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

    def __init__(self, centre, extent, resolution):  # TODO: add type annotations
        self.grid=complex_grid(centre,extent,resolution)
        self.pixels=np.vectorize(self.get_pixel)(self.grid,0)

    @staticmethod
    def get_pixel(c, z0):  # TODO: add type annotations
        """
        Computes a single 8-bit pixel.

        Args:
            c: The additive constant
            z0: The initial value for z

        Returns:
            Integer between 0 and 255
        """
        for n, z in zip(range(256), quadratic_map(c, z0)):
            if abs(z) >= 2:break
        return n

    def get_figure(self,cmap:str)->plt.Figure:
        """
        Creates a matplotlib Figure visualising the Mandelbrot set.

        Args:
            cmap:
                The colour map used to colour pixels. For available colours
                see matplotlib documentation on colourmaps
        """
        # TODO: it would be nice if we could fall back on a default value
        # for the colourmap if no cmap argument is provided

        grid_min, grid_max= self.grid.min(),self.grid.max()
        fig, ax = plt.subplots()

        ax.imshow(self.pixels,
            cmap=cmap,
        extent=(grid_min.real,grid_max.real,grid_min.imag,grid_max.imag),
            origin="lower")

        ax.set_title(f"{type(self).__name__} Set")
        ax.set_xlabel("Real axis")
        ax.set_ylabel("Imaginary axis")
        fig.tight_layout()

        return fig

    def get_image(self, cmap: str) -> Image.Image:
        """
        Creates a PIL (pillow) Image visualising the Mandelbrot set
        """
        cmap = get_cmap(cmap)
        image_array = np.uint8(cmap(self.pixels / 255) * 255)
        return Image.fromarray(image_array)


centre= complex(-0.75,0)
extent= 2.5
resolution= 500
cmap= "viridis"
save =False

mandelbrot=Mandelbrot(centre,extent,resolution)
fig=mandelbrot.get_figure(cmap)
plt.show()
