=========
Main Task
=========

------------
Fix the bugs
------------

On the last line of ``mandelbrot.py`` there is a commented-out line with ``plt.show()``.
Un-comment this and run the script.
You should see a rather boring figure appear which looks nothing like a fractal.
It seems we may have a bug...

Comment the ``plt.show()`` statement out again.

In the file ``test_utils.py`` there are some unit tests, which test some of the functions used to generate the fractal image.
A test fails if one of the conditions in the ``assert`` statements is ``False``.

Into your Conda environment, install the ``pytest`` package, and update your ``environment.yml`` file.
Inside the ``task-1`` directory, run the command ``pytest``.
You should find that there are test failures.

By inspecting the traceback provided by pytest, see if you can spot the bug.
Hint: it's a typo which affects the mathematical operations!

Once you've fixed the bug and the tests are all passing, uncomment the ``plt.show()`` statement.
The output should look rather more interesting than previously!

Commit your changes and push to Github.

-------------------
Open a pull request
-------------------

Now that things are actually working, let's be bold and state our intentions to merge our changes into the ``main`` branch.
Github provides a nice way to do this called a 'pull request' (PR).

Go to your repository on the Github website.
TODO: there's a setting which enables workflows on forks. Activate it.

On Github, create a PR to merge ``task-1`` into ``main``.
Give your PR a sensible title.
**Do not merge the PR**.

You should see that a Github 'workflow' starts to run, and that it fails pretty quickly.
Click on the workflow to see what went wrong.
You should find that the workflow failed during the 'Lint' stage.

-------
Linting
-------

The code is clearly a total stylistic mess.

Install the ``black`` formatter and the ``flake8`` linter into your Conda environment, and update the ``environment.yml`` file.

Now try running ``black .`` in the ``task-1`` directory.
You should see that some or all of of the ``.py`` files have been formatted, and look much better!

Next, run ``flake8 .`` and have a look at the output.
It doesn't seem to approve of the ``from mandelbrot import *`` statement!
FOOTNOTE: This is perfectly legit Python code, but generally seen as bad practice since it pollutes the namespace with things that cannot be read off from the import statement.
It's possible to tell ``flake8`` to ignore this, but let us instead be explicit about what we want to import.

Once you can run ``flake8 .`` in the ``task-1`` directory without any errors, commit your changes and push to GitHub.
You should find that the 'Lint' stage of the workflow completes this time.


----------------------------
Fix the import/execution bug
----------------------------

As well as ``mandelbrot.py``, there is another Python script called ``julia.py`` which displays a different type of fractal and, as we have just seen, imports some functions from ``mandelbrot.py``.

Unfortunately, this means that ``mandelbrot.py`` functions as both a script - it is executed with ``python mandelbrot.py`` - and as a module - it is imported by ``julia.py``.
To demonstrate the problem, first uncomment the ``plt.show`` line in both ``mandelbrot.py`` and ``julia.py``, and then run ``python julia.py``.
You should find that the Mandelbrot set appears before the desired Julia set, confirming that ``mandelbrot.py`` was executed when it was imported by ``julia.py``.

The conventional solution to the above problem is wrap the lines of code which execute the script in the ``if __name__ == "__main__"`` clause.

Fix this bug by wrapping the script elements of ``mandelbrot.py`` and ``julia.py`` with the above clause.
You should now find that running ``python julia.py`` doesn't execute ``mandelbrot.py``, and you no longer need to worry about commenting out ``plt.show()``!


---------------
Make use of OOP
---------------

You may have noticed a certain degree of similarity between the ``Mandelbrot`` class in ``mandelbrot.py`` and the ``Julia`` class in ``julia.py``.
In fact, the only way in which these classes differ is in their constructor (``__init__`` method) and in the title they give to the generated figure (``ax.set_title``).

The code would be much neater and easier to maintain if the methods ``get_pixel``, ``get_figure`` and ``get_image`` were shared between both classes.
There's more than one way to achieve this, but we will use **inheritance** here.

Modify the ``Julia`` class so that it inherits from ``Mandelbrot``, and only overrides the constructor (``__init__`` method) and no other methods.

You should also ensure that the visualisations of the Julia set don't have 'Mandelbrot Set' as their title, even though the ``get_figure`` method is inherited from ``Mandelbrot``.

Hint: There are several ways to achieve this.
Consider setting a class attribute, or simply using the name of the class as the title.


----------------
Catch bad inputs
----------------

At the top of ``mandelbrot.py`` we have a constant ``MAX_PIXELS`` defined to be 1000000.
Unless you have a very powerful computer or are willing to wait a very long time to generate images, this is about the maximum resolution you want.
The problem is that there is nothing currently enforcing this limit.

Add an ``assert`` statement in the appropriate location so that if more pixels than ``MAX_PIXELS`` are requested, the program terminates with an error message explaining why.

We could go much further with trying to catch every possible bad input.
However, this can be incredibly time consuming, so it is often sufficient to manually catch errors in just the following situations:

* When the program would otherwise fail silently, i.e. produce a bad output without alerting the user
* When the program would otherwise execute with unintended and irreversible consequences, such as overwriting some data
* When the program would otherwise run for a long period of time before crashing, wasting a lot of time in the process
* When the program would into an exception with an ambiguous or complicated traceback, i.e. from which it would be hard to pinpoint the cause of the error


----------------------
Turn it into a package
----------------------

First, create a directory inside ``task-1`` called ``task_1``, and move all of the ``.py`` files into it (but not the README or the environment file).
This will be our package.

Install the ``flit`` package into your Conda environment, and update the ``environment.yml`` file.
This is a simple tool for building Python packages, which we are now going to use to turn our code into a package.

In the ``task-1`` directory, generate a ``pyproject.toml`` using ``flit``, naming the package ``task_1`` (as in the directory into which we put our source code).

.. warning::

    Don't enter your real email address when prompted, unless you want to receive spam!

Flit requires us to specify the package version and docstring inside an ``__init__.py`` module in the root of the package.
Inside ``task_1`` directory, create a file ``__init__.py`` containing the following lines:

.. code-block:: python
   :linenos:

    """Visualisations of the Mandelbrot set and associated Julia sets"""
    __version__ = "0.1.0"
    
Now let's install our package into the Conda environment using ``flit``: in the same directory as the ``pyproject.toml`` file, run

.. code-block::

    flit install --symlink


--------------------
Restructure the code
--------------------

We have created a package, but its structure is still pretty mish-mash.

You should re-organise this code in order to have the following structure:

.. code-block::

    task-1
    ├── environment.yml
    ├── pyproject.toml
    ├── README.rst
    └── task_1
        ├── fractals.py
        ├── __init__.py
        ├── scripts
        │   ├── __init__.py
        │   ├── julia.py
        │   └── mandelbrot.py
        ├── tests
        │   ├── __init__.py
        │   └── test_utils.py
        └── utils.py


``fractals.py``
    A module containing ``Mandelbrot`` and ``Julia`` classes.
    This should do nothing when executed as a script using ``python fractals.py``

``utils.py``
    A module containing assorted other functions

``scripts/mandelbrot.py``
    A script containing a function called ``plot`` which has the signature shown below.
    It should create a visualisation of the Mandelbrot set according to the provided arguments.
    If ``cmap`` is not provided, it should default to ``"viridis"``.
    If ``output`` is provided, the visualisation should be saved as a ``png`` with a file-name given by ``output``, and *should not be displayed using* ``plt.show``.
    If ``output`` is not provided, the visualisation should be displayed with ``plt.show``.
    At the top of the script, some global constants should be defined which specify values for ``centre``, ``extent``, ``resolution``, ``cmap`` and ``output``.
    When the file is run as a script, the ``plot`` function should be called by passing these global variables into as arguments..
    When the file imported as a module, nothing should happen.

.. code-block:: python

    # scripts/mandelbrot.py

    def plot(
        centre: complex,
        extent: float,
        resolution: int,
        cmap: str,  # add a default value here
        output,  # add a type hint and default value here
    ) -> None:
        ...

``scripts/julia.py``
    A script which functions almost exactly like ``scripts/mandelbrot.py``, except the signature for the plot function has an additional ``complex`` argument ``c_value``, which is the first argument (i.e. before ``centre``).

All might seem rather pedantic, and in many ways it is.
The real point here is to logically separate the modular elements of the source code from the code which purely relates to execution (and from the tests).
This can make larger projects much more flexible and scalable.

During this process you will need to adjust several of the ``import`` statements, to be able to import other modules within the package.
Since the scripts and test modules need to import modules from a different directory, this poses an issue; we can't just do ``import utils`` from inside ``test_utils.py``, since ``utils.py`` is in a different directory.
The more experienced among you might be thinking of using ``sys.path.insert(0, "../")`` to tell Python to look for modules in the parent directory, but this is a pretty hacky and brittle solution.
By packaging up our code we have a better solution:

.. code-block:: python

    from task_1.utils import complex_grid, quadratic_map

Use ``flake8`` and ``pytest`` to check that everything is in order, other than perhaps that the scripts are unable to import things from the parent directory.

Also, what are these ``__init__.py`` modules for?
Try

.. code-block:: python

    >>> import task_1
    >>> task_1.__version__
    '0.1.0'
    

------------------------------
Merge with the ``main`` branch
------------------------------

Once the continuous integration is successfully passing, you're ready to merge your PR with the main branch.
Go ahead and do this!
