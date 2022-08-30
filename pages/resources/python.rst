======
Python
======

Python 2 reached 'end of life' several years ago.


How to invoke Python
--------------------

On the command line:

.. code-block:: sh

    $ python
    >>> help(math)




Object oriented programming
---------------------------

.. code-block:: python

    class Person:

        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age


As you can see, the child class inherits every method and attribute from its parent.

The real power of OOP is down to the ability to override the parent's methods and attributes.

EXAMPLE


Packaging
---------

A *package* in Python is a collection of *modules* that are grouped together under a single *namespace* - the package name.

This is most easily illustrated with examples.



By 'packaging', I 


Glossary
--------

:Function: A Python function is something that takes ... scope 

:Class: A Python class is a *template for an object*. An *instance* of the class is created by calling the *constructor* ``__init__(self, ...)``.

:Method: A method is a *function that is bound to an object*.

:Attribute: Objects have attributes

:Namespace: Some stuff

:Module: A module is a *collection of function, class and variable definitions, grouped together in a single namespace*.
    ``.py`` files

:Script: A Python script is a ``.py`` file that is intended to be executed as ``python script.py``, as opposed to one that is intended to act solely as a module.
    Note that *scripts are also modules that can be imported!* To stop the script being executed on import, one can wrap the execution in a ``if __name__ == "__main__"`` clause.

:Package: A package is a *collection of modules, grouped together in a single namespace*.

:Library: A library refers to a *collection of packages grouped together in a single namespace*.
    Arguably, this is a redundant term since they are conceptually and functionally identical to packages containing sub-packages.
    Examples of libraries are: NumPy, MatPlotLib, PyTorch...


External resources
------------------

* `Official Python 3 documentation <https://docs.python.org/3/>`_
* `Official Package index <https://pypi.org/>`_
* `Geeks for Geeks Python tutorials <https://www.geeksforgeeks.org/python-programming-language/?ref=shm>`_
