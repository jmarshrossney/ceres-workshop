import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def load_data_from_json(data_dir: str = "data") -> dict:
    """Reads data from json file and returns dict containing the data."""
    data_dir = Path(data_dir)
    data_json = data_dir / "shipsnet.json"
    with data_json.open("r") as file:
        data_dict = json.load(file)
    return data_dict


def _prepare_array(array: np.ndarray) -> np.ndarray:

    if array.max() <= 1:
        array *= 255  # rescale to 8 bit pixels

    return array


def array_to_rgb_image(array: np.ndarray) -> Image:
    """
    Converts numpy array to PIL rgb image.

    Takes a numpy array with shape (3, W, H) and returns an RGB
    Image of W x H pixels, created from this array.

    This image can be displayed using matplotlib.pyplot.imshow.
    """
    assert array.ndim == 3, "Expected array to have 3 dimensions"
    assert array.shape[0] == 3, "Expected first dimension to be RGB channels"

    # 8-bit
    array = array.astype("uint8")

    # Image should have dims (row, col, channel)
    array = array.transpose([1, 2, 0])

    image = Image.fromarray(array, "RGB")
    return image


def array_to_rgb_histogram(
    array: np.ndarray,
    bins: int = 30,
    embed_image: bool = False,
) -> plt.Figure:
    """
    Generates a histogram showing the red, green, blue channels.

    Arguments:
        array (numpy.ndarray):
            Array of shape (3, W, H) containing the pixel intensities
            in the three channels
        bins (int):
            Number of bins in each of the three historgrams
        embed_image (bool):
            If True, the image is also displayed in the corner of the
            plot
    """
    assert array.ndim == 3, "Expected array to have 3 dimensions"
    assert array.shape[0] == 3, "Expected first dimension to be RGB channels"

    r, g, b = [channel.flatten() for channel in array]

    fig, ax = plt.subplots()
    ax.set_xlabel("pixel intensity")
    ax.set_ylabel("count")
    ax.set_xlim(0, 255)
    ax.hist(r, bins=30, color="r", alpha=0.5)
    ax.hist(g, bins=30, color="g", alpha=0.5)
    ax.hist(b, bins=30, color="b", alpha=0.5)

    # Embed image in the top-right (high count + intensity) corner
    if embed_image:
        im = fig.add_axes([0.6, 0.54, 0.33, 0.33])
        im.set_axis_off()
        im.imshow(array)

    return fig


def check_parameters_match(
    parameters_1: list[np.ndarray], parameters_2: list[np.ndarray]
) -> bool:
    """
    Checks if two sets of parameters for an MLPClassifier match.

    Returns True if the parameters match, i.e. if the models are the same.
    Returns False is they differ.
    """
    return all([np.allclose(a, b) for a, b in zip(parameters_1, parameters_2)])
