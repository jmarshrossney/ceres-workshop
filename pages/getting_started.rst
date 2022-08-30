===============
Getting Started
===============

Prerequisites
-------------

**Git and Github:**

You will need [#f1]_

* A `GitHub <https://github.com/>`_ account
* The ability to perform git operations on your computer, either via terminal commands or through `GitHub Desktop <https://desktop.github.com/>`_

GitHub have recently increased their security quite dramatically, so you will need to `create a personal access token <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>`_ to push to GitHub from the command line.

**Conda:**

You have a choice to use either

* `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, or
* `Anaconda <https://www.anaconda.com/>`_

I personally recommend Miniconda because it doesn't require you to download thousands of packages you will never use, but Anaconda is designed to be more user-friendly.


**Kaggle:**

Take a look at `Kaggle <https://www.kaggle.com/>`_.
It's a rather nice platform for 'open' data science, which is now owned by Google.
If you don't mind ths, create an account.
This will make it easier to access some data we will use in the workshop.

If you would prefer not to create a Kaggle account don't worry - talk to me and we can get the data another way.


**Text editor or IDE:**

You need something that is able to read and edit ``.py`` and other text-based files.


**Internet access:**

Several parts of this workshop require internet access.


Preliminary exercise
--------------------

Check that your Conda installation is working correctly by running the following commands:

.. code-block::
    
    conda create --name test python=3.9
    conda activate test
    conda install ipython

If this all works, you should find that you can run Interactive Python in the terminal be typing ``ipython``.

It's well worth knowing from the get-go how to bring up documentation for Python objects.
Generally, you can do this by typing ``help(object)``, but in IPython you can also use ``?``.

Try to run the following

.. code-block::

    $ ipython

    In [1]: import math

    In [3]: math.sqrt?
    Signature: math.sqrt(x, /)
    Docstring: Return the square root of x.
    Type:      builtin_function_or_method


Let's clean up after ourselves and delete this Conda environment

.. code-block::

    conda deactivate
    conda env remove --name test


Fork and clone the repository
-----------------------------

Go to the `workshop GitHub page <https://github.com/marshrossney/ceres-workshop>`_ and click the button in the top-right that says *Fork*.
If prompted, select the option that clones the 'main' branch only.

You should now find that ``ceres-workshop`` appears in *your* list of GitHub repositories.

Next, make a local clone of your fork.

If you're using GitHub Desktop, you can do this from the browser by click on the green 'Code' button, followed by 'Open with GitHub Desktop' - see `these instructions <https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop>`_.

If you're using the command line, simply navigate to a directory that you'd like to work from and enter

.. code-block:: 

    git clone https://github.com/username/ceres-workshop.git

in your terminal, where ``username`` is clearly your own GitHub username.


Before you continue...
----------------------

* Have you installed ``git`` or GitHub Desktop on your computer, and authenticated them so that you can push changes to GitHub?
* Have you forked the ``ceres-workshop`` repository, so that it appears in your repositories on GitHub?
* Have you made a local clone of this repository, using GitHub Desktop or ``git clone``?
* Have you installed either Miniconda (recommended) or Anaconda, and are able to activate an environment using ``conda activate``?
* Have you made an account with Kaggle, or talked to me about getting hold of the data?
* Are you able to open ``.py`` files using a text editor or IDE?
* Are you connected to the internet?


.. rubric:: Footnotes

.. [#f1] It is actually possible to do the tasks without using ``git`` or GitHub; you can just download the code as a zipped archive and work on it locally. However, I strongly recommend against this; the focus of this workshop is just as much on using git as it is on Python.
