===============
Getting Started
===============


Create a working branch
-----------------------

.. admonition:: Before you start

    Make sure you are on the ``main`` branch of your local clone of the repository, with no un-committed changes (check ``git status``)

Create and checkout a new branch called ``task-2``.

.. code-block:: sh

    git checkout -b task-2

Push this new branch to the remote repository (i.e. to your Github).

.. code-block:: sh

    git push -u origin task-2


.. important::
    The branch must be named ``task-2`` for the tests to run when you make changes and push.


Create a Conda environment
--------------------------

Navigate to ``tasks/task_2/fractals`` and try to run ``python fractals.py``.
You should find that this fails due to being unable to import the required packages, unless you happen to have all of the dependencies installed in your current environment. [#f1]_

Create a Conda environment with Python 3.9 and IPython installed.

.. code-block::

    conda create --name ceres-t2 python=3.9 --yes
    conda activate ceres-t2
    conda install -c conda-forge ipython

By inspecting the code, try to install the required packages.

.. note::
   Some packages such as ``os`` and ``math`` are Standard Library packages and do not require separate installation.

Once you have successfully installed the  there are no more import errors, save your environment specification to a file called ``environment.yml`` in the ``tasks/task_2`` directory, using the following command:

.. code-block::

    conda env export --from-history > environment.yml

Commit ``environment.yml`` and push to GitHub.

.. code-block::

    git add environment.yml
    git commit -m "added environment.yml"
    git push -u origin task-2


.. rubric:: Footnotes

.. [#f1] As we will discuss, this is **not** a good thing!
