========
Glossary
========

:Function: A Python function is something that takes some inputs, or *arguments*, and returns something. 

:Class: A Python class is a *template for an object*. An *instance* of the class is created by calling the *constructor* ``__init__(self, ...)``.

:Method: A method is (to first approximation) a *function that is bound to an object*.

:Attribute: Objects have attributes, which are just other objects that can be accessed using the syntax ``object.attribute``, or ``getattr(object, attribute)``.

:Namespace: A namespace is a *scope* in which a certain set of keys can be used to access a corresponding set of objects.

:Module: A module is a *collection of function, class and variable definitions, grouped together in a single namespace*.
    ``.py`` files

:Script: A Python script is a ``.py`` file that is intended to be executed as ``python script.py``, as opposed to one that is intended to act solely as a module.
    Note that *scripts are also modules that can be imported!* To stop the script being executed on import, one can wrap the execution in a ``if __name__ == "__main__"`` clause.

:Package: A package is a *collection of modules, grouped together in a single namespace*.

:Library: A library refers to a *collection of packages grouped together in a single namespace*.
    Arguably, this is a redundant term since they are conceptually and functionally identical to packages containing sub-packages.
    Examples of libraries are: NumPy, MatPlotLib, PyTorch...


