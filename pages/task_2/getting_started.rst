===============
Getting Started
===============


Create a working branch
-----------------------

.. admonition:: Before you start

    Make sure you are on the ``main`` branch of your local clone of the repository

Create and checkout a new branch called ``task-1``.
You can do this by either following the instructions for branch creation on Github Desktop, or by executing the following command in your terminal:

.. code-block:: sh

    git checkout -b task-1

This is the branch you are going to work on, before finally merging back into ``main`` when you're happy with everything.

Push this new branch to the remote repository (i.e. to your Github).
The relevant terminal command is

.. code-block:: sh

    git push -u origin task-1


.. important::
    The branch must be named ``task-1`` for the tests to run when you make changes and push.


Create a Conda environment
--------------------------

Navigate to ``tasks/fractals/fractals`` and try to run ``python fractals.py``.
You should find that this fails due to being unable to import the required packages, unless you happen to have all of the dependencies installed in your current environment. [#f1]_

Create a Conda environment with Python 3.9 and IPython installed.

.. code-block::

    conda create --name ceres-t1 python=3.9 --yes
    conda activate ceres-t1
    conda install -c conda-forge ipython

By inspecting the code, try to install the required packages.

.. note::
   Some packages such as ``os`` and ``math`` are Standard Library packages and do not require separate installation.

.. seealso:: :ref:`conda`

Once you have successfully installed the  there are no more import errors, save your environment specification to a file called ``environment.yml`` in the ``tasks/fractals`` directory, using the following command:

.. code-block::

    conda env export --from-history > environment.yml

Commit ``environment.yml`` and push to GitHub.

.. code-block::

    git add environment.yml
    git commit -m "added environment.yml"
    git push -u origin task-1


.. rubric:: Footnotes

.. [#f1] As we will discuss, this is **not** a good thing!
