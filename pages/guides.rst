======
Guides
======

Python tools
------------

.. rubric:: Getting help

It's well worth knowing from the get-go how to bring up documentation for Python objects.
Generally, you can do this by typing ``help(object)``, but in IPython you can also use ``?``.


.. code-block:: sh

    $ python
    
    >>> import math

    >>> help(math.ceil)
    Help on built-in function ceil in module math:

    ceil(x, /)
        Return the ceiling of x as an Integral.

        This is the smallest integer >= x.

or in IPython

.. code-block:: sh

    $ ipython

    In [1]: import math

    In [2]: math.ceil?
    Signature: math.ceil(x, /)
    Docstring:
    Return the ceiling of x as an Integral.

    This is the smallest integer >= x.
    Type:      builtin_function_or_method



.. rubric:: Testing

Install `PyTest <https://docs.pytest.org/>`_ into your Conda environment

.. code-block::

    conda install pytest

Let's say you have organised your code into a package ``package`` as follows:

.. code-block::

    ├── package
    │   ├── __init__.py
    │   ├── module_1.py
    │   ├── module_2.py
    │   └── tests
    │       ├── __init__.py
    │       ├── test_module_1.py
    │       └── test_module_2.py
    └── pyproject.toml

where ``test_module_1.py`` contains test functions whose names start with ``test_``, e.g.

.. code-block:: python

    # inside test_module_1.py
    from package.module_1 import function, variable

    def test_function():
        result = function()
        assert result is True

    def test_variable():
        assert variable == 42

We can run these tests from anywhere in the tree shown above by simply executing

.. code-block::

    pytest


.. rubric:: Benchmarking

As well as being a Standard Library package, ``timeit`` is a magic method in IPython.

In Ipython or a Jupyter notebook it can be used to measure execution time as follows:

.. code-block:: python

    def my_func():
        """Some function I want to time."""
        ...

    %timeit my_func()

Typically it will run the given source code many times to get an average time.


.. rubric:: Formatting

Install `Black <https://github.com/psf/black>`_ into your Conda environment

.. code-block::

    conda install -c conda-forge black


or

.. code-block::

    python -m pip install black

If you want to format Jupyter notebooks,

.. code-block::

    python -m pip install black[jupyter]


To format your code, just run the following command in the directory containing the files you want to format:

.. code-block::

    black .

You can configure ``black`` (e.g. change the max line length, tell it to ignore directories...) in your ``pyproject.toml`` file.
See the documentation for details.


.. rubric:: Linting

Install `Flake8 <https://flake8.pycqa.org/en/latest/>`_ into your Conda environment

.. code-block::

    conda install flake8

Run it as follows:

.. code-block::

    flake8 .

You may want Flake8 to ignore certain errors that you don't care about.
In this case, you need to create a file ``.flake8`` (in your repository root) to configure Flake8.
See the `documentation <https://flake8.pycqa.org/en/latest/user/configuration.html>`_.



Basic Git workflow
------------------

1. Make a local clone of a remote repository

.. code-block::

    git clone https://github.com/<username>/<repo_name>.git


2. Switch to an existing branch

.. code-block::

    git switch <existing_branch>

3. Create a new branch, based on the current one, and switch to it

.. code-block::

    git checkout -b <new_branch>


4. Inspect the local changes you've made

.. code-block::

    git diff --compact-summary
    git status

5. Add changes to the staging area

.. code-block::

    git add <files>

6. Create a local commit based on staged changes

.. code-block::

    git commit -m "a message about what this commit contains"

7. Push the changes to the remote

.. code-block::

    git push -u origin <new_branch>


8. Merge your branch with the original one (or, alternatively, use a pull request!)

.. code-block::

    git switch <existing_branch>
    git merge <new_branch>


How to create a package
-----------------------

TODO
