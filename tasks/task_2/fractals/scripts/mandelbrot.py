from typing import Optional
import sys

import matplotlib.pyplot as plt

sys.path.insert(0, "../")

from fractals import Mandelbrot

CENTRE = complex(-0.75, 0)
EXTENT = 2.5
RESOLUTION = 500
CMAP = "viridis"
OUTPUT = None

def plot(
        centre: complex,
        extent: float,
        resolution: int,
        cmap: str = "viridis",
        output: Optional[str] = None,
    ) -> None:

    fig = Mandelbrot(centre, extent, resolution).get_figure(cmap)

    if output:
        fig.gca().set_axis_off()  # remove axis
        fig.gca().set_title("")   # remove title
        fig.tight_layout()  # smaller borders
        fig.savefig(output, dpi=300)  # save with 300 dots per inch
    else:
        plt.show()

def main():
    plot(
            centre=CENTRE,
            extent=EXTENT,
            resolution=RESOLUTION,
            cmap=CMAP,
            output=OUTPUT,
    )

if __name__ == "__main__":
    main()
