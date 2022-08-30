=========
Main Task
=========

Fix the bugs
------------

.. admonition:: Before you start

    Navigate to the directory ``tasks/fractals/fractals/``

On the last line of ``fractals.py`` there is a commented-out line with ``plt.show()``.
Un-comment this and run the script with ``python fractals.py``.
You should see a couple of rather boring figures appear which look nothing like fractals.
It seems we may have a bug!
Comment the ``plt.show()`` statement out again.

In the file ``tests/test_utils.py`` there are some unit tests, which test some of the functions used to generate the fractal image.
A test fails if one of the conditions in the ``assert`` statements is ``False``.

Into your Conda environment, install the ``pytest`` package:

.. code-block::

    conda install -c conda-forge pytest

Navigate to the ``tests`` directory and run the command ``pytest``.
You should find that there are test failures.

.. note::

    For now, you will need to run ``pytest`` inside the ``tests`` directory for it to work.
    Don't worry - we will fix this soon!

By inspecting the traceback provided by pytest, see if you can spot the bug.

.. hint:: The bug is a typo which affects the mathematical operations!

Once you've fixed the bug and the tests are all passing, uncomment the ``plt.show()`` statement.
The output should look rather more interesting than previously!

Update the ``environment.yml`` file so that it include ``pytest``.
Commit your changes and push to Github.


Open a pull request
-------------------

Now that things are actually working, let's be bold and state our intentions to merge our changes into the ``main`` branch.
Github provides a nice way to do this called a 'pull request' (PR).

Go to your repository on the Github website, and navigate to the ``task-1`` branch.

Click to the 'Actions' tab.
You should see a message that states *"Workflows aren't being run on this forked repository,"* and an option in green below *"I understand my workflows, go ahead and enable them."*
**Click on this green button.**

Now, in the 'Pull Requests' tab, create a PR to merge ``task-1`` into ``main``.
Give your PR a sensible title.

.. important:: Do not merge the pull request!

You should see that a Github 'workflow' starts to run, and that it fails pretty quickly.
Figure out how to open up the workflow logs to see what went wrong.
You should find that the workflow failed during the *Lint* stage.

       
Linting
-------

The code is clearly a total stylistic mess, and this is what the workflow is complaining about.
Rather than fix this manually, let's use some tools to automate this!

Install the ``black`` formatter and the ``flake8`` linter into your Conda environment, and update the ``environment.yml`` file.

.. code-block:: 

    conda install -c conda-forge black flake8

To run black, we simply type (in the directory we care about)

.. code-block::

    black .

You should see that some or all of of the ``.py`` files have been formatted, and look much better!

Next, run

.. code-block::

    flake8 .

Flake8 doesn't seem to approve of the ``from utils import *`` statement! [#f1]_
It's possible to tell ``flake8`` to ignore this, but let us instead be explicit about what we want to import.
Go ahead and do this!

Once you can run ``flake8 .`` in the ``fractals`` directory without any errors, commit your changes and push to GitHub.
With any luck you should find that the *Lint* stage of the workflow completes this time.

                            
Fix the import/execution bug
----------------------------

As things stand, when we run ``fractals.py`` as a script, we generate visualsations of both Mandelbrot and Julia sets.
In order to modify any of the parameters, or plot just one fractal rather than both, we need to dig into ``fractals.py`` and modify the source.
This is pretty poor.
It's generally a much better idea to separate out any parts of the program that function as scripts, from the rest of the code base.

Navigate to the ``fractals/scripts`` directory.
You will notice two scripts called ``mandelbrot.py`` and ``julia.py``.

Run

.. code-block::

    python mandelbrot.py

Oh dear! We got more than we asked for - three plots instead of one!

The reason this occurs is that when a module is imported, it is actually executed in (more or less) the same way as when it is run as a script.

.. code-block:: python
   :linenos:
   :emphasize-lines: 8
   
    from typing import Optional
    import sys

    import matplotlib.pyplot as plt

    sys.path.insert(0, "../")

    from fractals import Mandelbrot


The conventional solution to the above problem is wrap the lines of code which execute the script in the ``if __name__ == "__main__"`` clause.
However, in our case we want to *remove* the ability for ``fractals.py`` to function as a script, since that functionality is now served by the ``mandelbrot.py`` and ``julia.py`` scripts.

Remove the lines at the bottom of ``fractals.py`` that create the figures.

You should now find that running ``python mandelbrot.py`` and ``python julia.py`` work as expected, generating a single plot in both cases.


Make use of OOP
---------------

You may have noticed a certain degree of similarity between the ``Mandelbrot`` and ``Julia`` classes in ``fractals.py``.
In fact, the only way in which these classes differ is in their constructor (``__init__`` method) and in the title they give to the generated figure (``ax.set_title``).
The code would be much neater and easier to maintain if the methods ``get_pixel``, ``get_figure`` and ``get_image`` were shared between both classes.
There's more than one way to achieve this, but we will use **inheritance** here.

Modify the ``Julia`` class so that it inherits from ``Mandelbrot``.
The class definition should read:

.. code-block:: python

    class Julia(Mandelbrot):
        ...

Remove all of the methods except the constructor (the ``__init__`` method).

Finally, ensure that the visualisations of the Julia set don't have 'Mandelbrot Set' as their title, even though the ``get_figure`` method is inherited from ``Mandelbrot``.

.. tip:: 
    There are several ways to achieve this.
    Consider setting a `class or instance attribute <https://www.geeksforgeeks.org/class-instance-attributes-python/>`_.
    Another option is to just use the name of the class as the title.


Catch bad inputs
----------------

At the top of ``utils.py`` we have a constant ``MAX_PIXELS = 1000000``
Unless you have a very powerful computer or are willing to wait a very long time to generate images, this is about the maximum resolution you want.

The problem is that there is nothing currently enforcing this limit.
The easiest way to handle this scenario safely is to simply stop the executon of the program.

One possible mechanism to do this is to use an ``assert`` statement, which raises ``AssertionError`` if it evaluates to ``False``.
The syntax for ``assert`` is

.. code-block:: python

    assert CONDITION, message

Add an ``assert`` statement in the appropriate location so that if more pixels than ``MAX_PIXELS`` are requested, the program terminates with an error message explaining why.

.. hint:: The number of pixels is ``resolution ** 2``.

.. seealso:: Handling user input: TODO


Installing as a package
-----------------------

.. admonition:: Before you start

    Make sure you are in the ``tasks/fractals`` directory, i.e. the one with the ``pyproject.toml`` file.

The ``fractals`` directory which contains all the ``.py`` files has the structure of a Python package, but so far we have not actually installed it!

`Flit <https://flit.pypa.io/en/latest/>`_ is a simple tool for building Python packages. [#f2]_
Install the ``flit`` package into your Conda environment.

.. code-block:: 

    conda install -c conda-forge flit

Next, install our package into the Conda environment using the following command. [#f3]_

.. code-block::

    flit install --symlink

Update the ``environment.yml`` file.
You will notice that ``flit`` is listed in the ``environment.yml`` file, but not ``fractals``, our own package.
That's because only things installed with ``conda install`` get listed in the ``environment.yml`` file.


Fix the imports
---------------

Now that we have installed ``fractals`` as a package, we can ``import`` it just like any other package!
This means we can finally get rid of those awful ``sys.path.insert(0, "../")`` lines, which were telling Python to look in the parent directory for modules to import.

Take, for example, the test module ``tests/test_utils.py``.
We replace the following code block

.. code-block:: python

    import sys

    sys.path.insert(0, "../")

    from fractals import Mandelbrot
    from utils import complex_grid, quadratic_map

with

.. code-block:: python

    from fractals.fractals import Mandelbrot
    from fractals.utils import quadratic_map

This is much more concise, as well as reducing the change of a name-clash with another package. [#f4]_

This change is more than aesthetic.
Because ``sys.path.insert`` adds paths *relative to your current working directory*, you are forced to execute the script in the same directory as the script.
By installing the code as a package we have the flexibility to run the script from anywhere.
Try running ``pytest`` from a different directory - it should now work.
    
Change all of the statements that import internal modules so that they import from ``fractals``, rather than by relying on the path.



.. rubric:: Footnotes

.. [#f1] This is perfectly legit Python code, but generally seen as bad practice since it pollutes the namespace with things that cannot be read off from the import statement.

.. [#f2] There are other, better options such as Poetry, which also manages dependencies. However, since we're using Conda to manage dependencies, we may as well stick with a packaging tool that is simple and doesn't come with added bells and whistles.

.. [#f3] The reason for adding the ``--symlink`` option is that it allows us to *edit the installed version of the package*. When you install a package (e.g. in a Conda environment), the source code gets saved to a specific location that Python uses to search for packages - this is why you can ``import`` packages that aren't in your current working directory. What the ``--symlink`` option does is it creates a *symbolic link* from the code you're working on, to this special location, *instead of copying it*.

.. [#f4] Consider the case where we want to import a module called ``math.py`` in our current working directory. Would ``import math`` import our own ``math.py`` module, or the Standard Library one? Much better if we could write e.g. ``import mypackage.math``.
