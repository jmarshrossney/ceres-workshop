import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from PIL import Image

from utils import *





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

    def __init__(self, centre: complex, extent:float, resolution:int) -> None:
        self.grid=complex_grid(centre,extent,resolution)
        self.pixels=np.vectorize(self.get_pixel)(self.grid,0)

    @staticmethod
    def get_pixel(c:complex, z0 : complex) -> int:
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

    def get_figure(self,cmap: str ="viridis")->plt.Figure:
        """
        Creates a matplotlib Figure visualising the Mandelbrot set.

        Args:
            cmap:
                The colour map used to colour pixels. For available colours
                see matplotlib documentation on colourmaps
        """
        grid_min, grid_max= self.grid.min(),self.grid.max()
        fig, ax = plt.subplots()

        ax.imshow(self.pixels,
            cmap=cmap,
        extent=(grid_min.real,grid_max.real,grid_min.imag,grid_max.imag),
            origin="lower")

        ax.set_title("Mandelbrot Set")
        ax.set_xlabel("Real axis")
        ax.set_ylabel("Imaginary axis")
        fig.tight_layout()

        return fig

    def get_image(self, cmap:str = "viridis") -> Image.Image:
        """
        Creates a PIL (pillow) Image visualising the Mandelbrot set
        """
        cmap = get_cmap(cmap)
        image_array = np.uint8(cmap(self.pixels / 255) * 255)
        return Image.fromarray(image_array)


class Julia:
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

    def __init__(self,c_value:complex,centre:complex,extent:float,resolution:int) -> None:
        self.grid = complex_grid(centre, extent, resolution)
        self.pixels = np.vectorize(self.get_pixel)(c_value, self.grid)

    @staticmethod
    def get_pixel(c:complex, z0: complex) -> int:
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

    def get_figure(self,cmap:str = "viridis_r")->plt.Figure:
        """
        Creates a matplotlib Figure visualising the Mandelbrot set.

        Args:
            cmap:
                The colour map used to colour pixels. For available colours
                see matplotlib documentation on colourmaps
        """
        grid_min, grid_max= self.grid.min(),self.grid.max()
        fig, ax = plt.subplots()

        ax.imshow(self.pixels,
            cmap=cmap,
        extent=(grid_min.real,grid_max.real,grid_min.imag,grid_max.imag),
            origin="lower")

        ax.set_title("Julia Set")
        ax.set_xlabel("Real axis")
        ax.set_ylabel("Imaginary axis")
        fig.tight_layout()

        return fig

    def get_image(self, cmap: str = "viridis_r") -> Image.Image:
        """
        Creates a PIL (pillow) Image visualising the Mandelbrot set
        """
        cmap = get_cmap(cmap)
        image_array = np.uint8(cmap(self.pixels / 255) * 255)
        return Image.fromarray(image_array)


# Mandelbrot
centre= complex(-0.75,0)
extent= 2.5
resolution= 500

Mandelbrot(centre,extent,resolution).get_figure()


# Julia
c_value = complex(0, -1)
centre = complex(0, 0)
extent = 1.0
resolution = 500

Julia(c_value, centre, extent, resolution).get_figure()

#plt.show()
