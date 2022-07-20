from pathlib import Path
from warning import warn

from PIL import Image


def make_gif(images: list[Image.Image], output: str, duration: int) -> None:
    """
    Creates a GIF from a sequence of images.

    Args:
        images:
            A list of PIL Images
        output:
            The name of or path to the output GIF file, including
            a ``.gif`` extension
        duration:
            The duration of each frame of the GIF, in milliseconds
    """

    if Path(output).exists():
        warn(f"`{output}` already exists and will be overridden!")

    first, *rest = images
    first.save(
        output,
        format="GIF",
        append_images=rest,
        save_all=True,
        duration=duration,
        loop=0,
    )
