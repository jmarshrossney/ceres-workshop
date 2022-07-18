import argparse

parser = argparse.ArgumentParser(description="Generates a visualisation of the Mandelbrot set")
parser.add_argument(
    "-m",
    "--midpoint",
    type=float,
    nargs=2,
    required=True,
    help="Real and imaginary coordinates of the image centre",
    metavar=("REAL", "IMAG"),
)
parser.add_argument(
    "-x",
    "--extent",
    type=float,
    required=True,
    help="Linear extent of the image",
)
parser.add_argument(
    "-r",
    "--resolution",
    type=int,
    required=True,
    help="Number of pixels on each row or column",
)
parser.add_argument(
    "--cmap",
    type=str,
    required=False,
    default="viridis",
    help="Colour map",
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    required=False,
    help="Optionally save image to this location",
)
