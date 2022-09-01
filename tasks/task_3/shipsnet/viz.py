from typing import Union

import numpy as np
from PIL import Image, ImageFilter
import torch

def array_to_rgb_image(array: Union[np.ndarray, torch.Tensor]) -> Image:

    if isinstance(array, torch.Tensor):
        array = array.detach().numpy()

    assert array.ndim == 3, "Expected array to have 3 dimensions"
    assert array.shape[0] == 3, "Expected first dimension to be RGB channels"

    if array.max() <= 1:
        array *= 255  # rescale to 8 bit pixels

    # 8-bit
    array = array.astype("uint8")

    # Image should have dims (row, col, channel)
    array = array.transpose([1, 2, 0])
                                 
    image = Image.fromarray(array, "RGB")
    return image
