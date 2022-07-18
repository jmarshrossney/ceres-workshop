import matplotlib.pyplot as plt

from ceres_workshop.task_1.fractals import Julia
from ceres_workshop.task_1.scripts.parser import parser

parser.add_argument(
    "-c",
    "--const",
    type=float,
    nargs=2,
    help="Real and imaginary parts of the additive constant",
    metavar=("REAL", "IMAG"),
)


def main(arg_str=None):
    args = parser.parse_args(arg_str)

    c = complex(args.const[0], args.const[1])
    centre = complex(args.midpoint[0], args.midpoint[1])

    fig = Julia(c, centre, args.extent, args.resolution).get_figure(args.cmap)

    if args.output:
        fig.savefig(args.output)
    else:
        plt.show()


if __name__ == "__main__":
    main()
