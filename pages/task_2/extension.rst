===============
Extension Tasks
===============

.. tip:: You may find it useful to check out `this repository <https://github.com/marshrossney/mandelbrot>`_ if you get stuck.

                          
Explore the Mandelbrot set
--------------------------

Install ``jupyterlab`` and ``ipywidgets`` into your conda environment.

.. code-block::

    conda install -c conda-forge jupyterlab ipywidgets


Create a subdirectory inside ``task_2`` called ``notebooks``.
Inside this directory, create a Jupyter notebook containing visualisations of the Mandelbrot or Julia sets that you particularly like, along with the parameters used to generate the image.
Each cell can call the ``plot`` functions inside the scripts.

.. tip:: 
    You may have to type ``%matplotlib inline`` at the top of the notebook so that the
    visualisations are displayed

Modify the ``.gitignore`` so that ``.ipynb_checkpoints`` directories are not commited to git.

Once you're happy with the visualisations, commit this to Github.
Make sure you include ``.gitignore`` an d the updated ``environment.yml`` file too.

Usually we would want to clear the notebook before doing this, but in this case we would like to be able to view the images in the notebook from our browser.


Make the scripts configurable
-----------------------------

At the moment, the behaviour of the scripts ``mandelbrot.py`` and ``julia.py`` are completely determined by variables hard-coded into the scripts.
Ideally they would be configurable, i.e. we should be able to control the behaviour at the point of execution, by passing different arguments to the script.

The task is to extend these scripts so that they can be called directly from the command line by running

.. code-block:: sh

    python mandelbrot.py ARGS OPTIONS

inside the ``scripts`` directory. In the above, ``ARGS`` and ``OPTIONS`` represent a sequence of arguments and options that specify the midpoint, extent, resolution, colour-map and output file.

**Hint:** The simplest way to do this is using ``sys.argv``, but this is the least best option.
A better option is the `Argparse <https://docs.python.org/3/library/argparse.html>`_ package, which is part of the Standard Library.
However, there are much better parsers out there, e.g. `Click <https://click.palletsprojects.com>`_.

Finally, turn your script into an **entry point** by modifying the ``pyproject.toml`` file to include a ``[project.scripts]`` section.
Name the entry point something easy to type, e.g. ``mandel``.
You may need to refer to the `Flit documentation <https://flit.pypa.io>`_.

Now you should be able to run the scripts from any directory by running e.g. ``mandel ARGS OPTIONS``.

If you're successful, why not make a CLI tool to visualise Julia sets too!


                  
Make an animation!
------------------

The code snippet below contains a function that creates and saves a GIF from a sequence of images.

.. code-block:: python
   :linenos:

    from distutils.util import strtobool
    from pathlib import Path
    from sys import exit
    from warnings import warn

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

        Warns:
            If the output file already exists a warning is raised and
            the user is prompted to either continue or abort
        """
        
        if Path(output).exists():
            warn(f"`{output}` already exists and will be overridden!")
            if not strtobool(input("Continue? [y/N] >")):
                exit(0)

        first, *rest = images
        first.save(
            output,
            format="GIF",
            append_images=rest,
            save_all=True,
            duration=duration,
            loop=0,
        )

Use it to create an animation of the Mandelbrot set.

I suggest trying to produce the following animation:

* Centred on the so-called *Feigenbaum point*, ``centre = -1.401155189``
* 500x500 pixels, ``resolution = 500`` (but use fewer to test!)
* 100 frames, ``n_frames = 100``
* An extent that starts at ``extent = 1.5`` and for each frame decreases by a factor of ``pow(delta, 3 / n_frames)`` where ``delta = 4.669201609`` is the *Feigenbaum delta* parameter, and 3 is a number related to how far we want to zoom in

