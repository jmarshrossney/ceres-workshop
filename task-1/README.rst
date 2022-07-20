!()[../assets/dendrite.png)

=================
Task 1: Fractals!
=================

Fractals are really cool. In this task you will make some visualisations of some well-known fractals such as the one above.

This is meant to be fun, and perhaps even pique your interest in the maths behind these amazing patterns, but the main aim here is to become familiar with the structure of a Python project, some common design patterns, and some key developer tools. There is no need to care about the maths unless you really want to!

Remember, you can bring up the documentation for any Python object using `help(object)` or, if you're using IPython, just `object?`.

---------------
Getting started
---------------

The first thing you should do is fork this repository and set up a local clone to work on.
You should be on the `main` branch; if not, switch to it.

Next, create a new branch called `task-1`.
This is the branch you are going to work on, before finally merging back into `main` when you're happy with everything.

Push this new branch to the remote repository (i.e. to Github) using `git push`.

Have a look at the [workshop notes on git and GitHub](https://marshrossney.github.io/ceres-workshop/git-and-github) for help with any of these steps.

--------------------
Get the code running
--------------------

Navigate to the `task-1` directory and try to run `python mandelbrot.py`.
You will probably find that this fails due to being unable to import the required packages (unless you happen to have all of the dependencies installed in your current environment).

Create a Conda environment with Python 3.9 and IPython installed.
By inspecting the code, try to install the required packages.
Note that some of them are Standard Library packages and do not require separate installation.

Once there are no more import errors, save your environment specification to a file called `environment.yml` in the `task-1` directory, by usng the `conda env export` command with the `--from-history` option.

Commit `environment.yml` and push to GitHub.

------------
Fix the bugs
------------

On the last line of `mandelbrot.py` there is a commented-out line with `plt.show()`.
Un-comment this and run the script.
You should see a rather boring figure appear which looks nothing like a fractal.
It seems we may have a bug...

Comment the `plt.show()` statement out again.

In the file `test_utils.py` there are some unit tests, which test some of the functions used to generate the fractal image.
A test fails if one of the conditions in the `assert` statements is `False`.

Into your Conda environment, install the `pytest` package, and update your `environment.yml` file.
Inside the `task-1` directory, run the command `pytest`.
You should find that there are test failures.

By inspecting the traceback provided by pytest, see if you can spot the bug.
Hint: it's a typo which affects the mathematical operations!

Once you've fixed the bug and the tests are all passing, uncomment the `plt.show()` statement.
The output should look rather more interesting than previously!

Commit your changes and push to Github.

-------------------
Open a pull request
-------------------

Now that things are actually working, let's be bold and state our intentions to merge our changes into the `main` branch.
Github provides a nice way to do this called a 'pull request' (PR).

Go to your repository on the Github website.
TODO: there's a setting which enables workflows on forks. Activate it.

On Github, create a PR to merge `task-1` into `main`.
Give your PR a sensible title.
**Do not merge the PR**.

You should see that a Github 'workflow' starts to run, and that it fails pretty quickly.
Click on the workflow to see what went wrong.

-------------
Get Organised
-------------

Shoving everything in one `.py` file is not a scalable approach to writing code.
It's far better to adopt a **modular** structure where independent components are logically organised into packages and modules.

------------------
Creating a package
------------------

-------------------
Catching bad inputs
-------------------

Assert statement if too many pixels
Warn user that file being overridden

----------------
Type annotations
----------------

------------------
Make an animation!
------------------

Install `jupyterlab` and `ipywidgets` into your conda environment.

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

---------
Footnotes
---------

.. note::
    :title: A note on complex numbers

    Don't be alarmed by the presence of `complex` in the code.
    In Python, `complex` objects support most of the same operations as `float`s do.
    Given two `float`s `x` and `y`, a complex number `z` can be created `z = complex(x, y)`.
    If you're not familiar with complex numbers, just think of them as coordinates z = (x, y) in a two-dimensional plane.

