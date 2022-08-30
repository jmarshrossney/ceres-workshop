============
Useful tools
============


Timing with Timeit
------------------

As well as being a Standard Library package, ``timeit`` is a magic method in IPython.

In Ipython or a Jupyter notebook it can be used to measure execution time as follows:

.. code-block:: python

    def my_func():
        """Some function I want to time."""
        ...

    %timeit my_func()

Typically it will run the given source code many times to get an average time.


Formatting with Black
---------------------

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


Linting with Flake8
-------------------

Install `Flake8 <https://flake8.pycqa.org/en/latest/>`_ into your Conda environment

.. code-block::

    conda install flake8

Run it as follows:

.. code-block::

    flake8 .

You may want Flake8 to ignore certain errors that you don't care about.
In this case, you need to create a file ``.flake8`` (in your repository root) to configure Flake8.
See the `documentation <https://flake8.pycqa.org/en/latest/user/configuration.html>`_.


Testing with PyTest
-------------------

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


