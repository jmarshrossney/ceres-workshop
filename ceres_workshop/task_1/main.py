import numpy as np
from tqdm.autonotebook import tqdm

from ceres_workshop.task_1.fractals import Mandelbrot
from ceres_workshop.task_1.utils import make_gif

def main():

    frames = 10
    centres = np.linspace(-1.4002, -1.4011, frames)
    extents = 3 / np.linspace(1, 4.7, frames)
    resolution = 500

    images = []

    with tqdm(range(1, frames + 1), desc="Generating frames", unit="fr") as prog_bar:
        for c, e in zip(centres, extents):
            m = Mandelbrot(complex(c), e, resolution)
            images.append(m.get_image())

            prog_bar.update()

    make_gif(images, "mandelbrot.gif")


if __name__ == "__main__":
    main()
