.. figure:: ../assets/penguins.png

    Artwork by @allison_horst

================
Warm-up exercise
================

Check that your Conda installation is working correctly by running the following commands:

.. code-block::
    
    conda create --name test python=3.9
    conda activate test

If this has worked you should be able to type ``conda info`` and see that the 'active environment' is ``test``.

.. important:: Double check that you've successfully activated the environment before proceeding!

Let's install a couple of packages from the ``conda-forge`` channel

.. code-block::

    conda install -c conda-forge ipython seaborn

If this all works, you should find that you can run Interactive Python in the terminal be typing ``ipython``.
Your terminal should now show a prompt that looks something (though not exactly) like this:

.. code-block::

    $ ipython
    Python 3.9.13 | packaged by conda-forge | (main, May 27 2022, 16:58:50)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 8.4.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]
    
Enter the following commands one-by-one:

.. code-block:: python

    In [1]: import seaborn, matplotlib.pyplot as plt

    In [2]: df = seaborn.load_dataset("penguins")
    
    In [3]: seaborn.pairplot(df, hue="species")

    In [4]: plt.show()


You should see a nice-looking figure appear. [#f1]_
Wow, that was pretty easy...

Let's dig into this just a little. Back in IPython:

.. code-block:: 

    In [5]: type(df)  # what did we just load...?
    Out[5]: pandas.core.frame.DataFrame  # a pandas DataFrame!

    In [6]: df.info()  # I'd like a bit more information, please..
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 344 entries, 0 to 343
    Data columns (total 7 columns):
     #   Column             Non-Null Count  Dtype
    ---  ------             --------------  -----
     0   species            344 non-null    object
     1   island             344 non-null    object
     2   bill_length_mm     342 non-null    float64
     3   bill_depth_mm      342 non-null    float64
     4   flipper_length_mm  342 non-null    float64
     5   body_mass_g        342 non-null    float64
     6   sex                333 non-null    object
    dtypes: float64(4), object(3)
    memory usage: 18.9+ KB

    In [7]: seaborn.pairplot?  # tell me about this 'pairplot'
    Signature:
    seaborn.pairplot(
        data,
        *,
        hue=None,
        ...


Press ``q`` to close the ``pairplot`` help page, and CTRL-D to close IPython.

Hopefully you've seen how easy it can be to not only perform complicated tasks in Python, but to also inspect and interrogate Python objects (without even needing to open your browser).

Let's clean up after ourselves and delete this Conda environment

.. code-block::

    conda deactivate
    conda env remove --name test

.. rubric:: Footnotes

.. [#f1] As well as ``penguins``, there are other datasets that you can access directly through ``seaborn``.
    You can browse through them `here <https://github.com/mwaskom/seaborn-data>`_.
    Why not find one you like the look of and work through some of the `visualisation tutorials <https://seaborn.pydata.org/tutorial.html>`_.
