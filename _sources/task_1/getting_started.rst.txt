===============
Getting Started
===============

-----------------------
Create a working branch
-----------------------

Starting from the ``main`` branch of your local clone of the repository, create and checkout a new branch called ``task-1``.
This is the branch you are going to work on, before finally merging back into ``main`` when you're happy with everything.

Push this new branch to the remote repository (i.e. to your Github).

.. important::
    The branch must be named ``task-1`` for the tests to run when you make changes and push.


--------------------
Get the code running
--------------------

Navigate to the ``task-1`` directory and try to run ``python mandelbrot.py``.
You should find that this fails due to being unable to import the required packages, unless you happen to have all of the dependencies installed in your current environment. [#f1]_

Create a Conda environment with Python 3.9 and IPython installed.
By inspecting the code, try to install the required packages.

.. note::
   Some packages such as ``os`` and ``math`` are Standard Library packages and do not require separate installation.

Once you have successfully installed the  there are no more import errors, save your environment specification to a file called ``environment.yml`` in the ``task-1`` directory, by usng the ``conda env export`` command with the ``--from-history`` option.

Commit ``environment.yml`` and push to GitHub.


.. rubric:: Footnotes

.. [#f1] As we will discuss, this is **not** a good thing!
