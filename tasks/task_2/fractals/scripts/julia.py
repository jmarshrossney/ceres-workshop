from typing import Optional

import matplotlib.pyplot as plt

from fractals.fractals import Julia

C_VALUE = complex(0, -1)
CENTRE = complex(0, 0)
EXTENT = 1.0
RESOLUTION = 500
CMAP = "viridis_r"
OUTPUT = None

def plot(
        c_value: complex,
        centre: complex,
        extent: float,
        resolution: int,
        cmap: str = "viridis",
        output: Optional[str] = None,
    ) -> None:

    # TODO: Create the figure here:
    # fig = ...

    if output:
        fig.gca().set_axis_off()  # remove axis
        fig.gca().set_title("")   # remove title
        fig.tight_layout()  # smaller borders
        fig.savefig(output, dpi=300)  # save with 300 dots per inch
    else:
        plt.show()

def main():
    plot(
            c_value=C_VALUE,
            centre=CENTRE,
            extent=EXTENT,
            resolution=RESOLUTION,
            cmap=CMAP,
            output=OUTPUT,
    )

if __name__ == "__main__":
    main()
