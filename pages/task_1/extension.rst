
------------------
Make an animation!
------------------

Install ``jupyterlab`` and ``ipywidgets`` into your conda environment.

--------------
Extension task
--------------

Make a command-line interface that generate Mandelbrot or Julia set plots, either showing a matplotlib figure or saving as a png.
Write a function with the signature ``mandelbrot(midpoint, extent, resolution, cmap)``, which displays a plot of the Mandelbrot set.

Put these functions in a separate folder called ``scripts``

Now turn this into a script that can be called directly from the command line by running

.. code-block:: bash

    python mandelbrot.py ARGS OPTIONS

inside the ``scripts`` directory. In the above, ``ARGS`` and ``OPTIONS`` represent a sequence of arguments and options that specify the midpoint, extent, resolution and colour-map.

**Hint:** The simplest way to do this is using ``sys.argv``, but this is the least best option.
A better option is the ``argparse`` package, which is part of the Standard Library.
However, there are much better parsers out there, e.g. ``click``.

Finally, turn your script into an **entry point** by modifying the ``pyproject.toml`` file to include a ``[project.scripts]`` section. You may need to refer to the `Flit documentation <https://flit.pypa.io/en/latest/index.html>`_.

If you're successful, why not make a CLI tool to visualise Julia sets too!

