import matplotlib.pyplot as plt

from ceres_workshop.fractals.fractals import Mandelbrot
from ceres_workshop.fractals.scripts.parser import parser


def mandelbrot(
    midpoint: complex, extent: float, resolution: int, cmap: str, output: str
) -> None:
    fig = Mandelbrot(
        complex(midpoint[0], midpoint[1]),
        extent,
        resolution,
    ).get_figure(cmap)

    if output:
        fig.savefig(output)
    else:
        plt.show()


def main(arg_str=None):
    args = parser.parse_args(arg_str)
    mandelbrot(**vars(args))


if __name__ == "__main__":
    main()
