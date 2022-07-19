=================
Task 1: Fractals!
=================

Fractals are really cool. In this task you will make some visualisations of some well-known fractals such as the one below.

< img >

This is meant to be fun, and perhaps even pique your interest in the maths behind these amazing patterns, but the primary purpose is to get familiar with the structure of a Python project and some key developer tools. There is no need to care about the maths unless you really want to!


----------
Setting up
----------

* Make a conda env
* Install required packages
* Install this package
* Output conda task_1.yml

----------------
Fix the code
----------------

The code is clearly a total mess and badly in need of organising and refactoring.
However, before diving in to that it's generally a good idea to get the code working!

...

-----------------
Get Organised
-----------------

Shoving everything in one `.py` file is not a scalable approach to writing code.
It's far better to adopt a **modular** structure in independent components are logically organised into packages and modules (see notes).

Anticipating that we will eventually want to merge all three tasks into one project, it seems like a good idea to separate tasks into their own subdirectories.

----------------
Catching errors
-----------------

Assert statement if too many pixels
Warn user that file being overridden

------------------
Make an animation!
------------------



--------------
Extension task
--------------

Make a command-line interface that generate Mandelbrot or Julia set plots, either showing a matplotlib figure or saving as a png.
Write a function with the signature `mandelbrot(midpoint, extent, resolution, cmap)`, which displays a plot of the Mandelbrot set.

Put these functions in a separate folder called `scripts`

Now turn this into a script that can be called directly from the command line by running

.. code-block:: bash

    python mandelbrot.py ARGS OPTIONS

inside the `scripts` directory. In the above, `ARGS` and `OPTIONS` represent a sequence of arguments and options that specify the midpoint, extent, resolution and colour-map.

**Hint:** The simplest way to do this is using `sys.argv`, but this is the least best option.
A better option is the `argparse` package, which is part of the Standard Library.
However, there are much better parsers out there, e.g. `click`.

Finally, turn your script into an **entry point** by modifying the `pyproject.toml` file to include a `[project.scripts]` section. You may need to refer to the Flit documentation `here <...>`_.

If you're successful, why not make a CLI tool to visualise Julia sets too!

