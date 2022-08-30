===============
Getting Started
===============

Create a new branch
-------------------

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


Create a Conda environment
--------------------------

Inside the ``task_1`` directory you should see a file called ``environment.yml``.
This contains a list of all the packages required to complete this task (excluding the extension!).

Create a Conda environment containing these packages, and then activate it, using the following commands:

.. code-block::

    conda env create --file environment.yml --name ceres-t1
    conda activate ceres-t1


Download the data
-----------------

Navigate to the directory called ``task_1``.

The dataset for this task is a set of satellite images that have been labelled as either containing a ship or not containing a ship.
The dataset comes from `Kaggle <https://www.kaggle.com/>`_, a cool platform for 'open data science'.
If you don't have a Kaggle account and don't want one, skip this step and talk to me.

If you have a Kaggle account, you can manually download the dataset by clicking the 'download' button on `the dataset webpage <https://www.kaggle.com/datasets/rhammell/ships-in-satellite-imagery>`_.
Unzip the downloaded file into a directory called ``data`` inside ``task-1``.

If you're using git via the command line, type the following into your terminal:

.. code-block::

    git status

You should see a message saying *"nothing to commit, working tree clean"*.
This may seem surprising - we have just added all of this data to our repository.
However, there is a file called ``.gitignore`` which is telling git to ignore any ``.png`` or ``.json`` files.

.. warning::

    You should not commit this data to version control. As it happens, it is within the size limits for GitHub, but it's bad practice to commit raw data and it can slow things down. If you don't see the 'working tree clean' message, let me know!



Investigate the data
--------------------

In the ``task-1`` directory, launch Jupyter Lab

.. code-block:: 

    jupyter lab

Open the notebook called ``dataset.ipynb``.
You should be able to run the cells inside using CTRL+ENTER.

Use this notebook to investigate the structure and properties of the dataset.
In particular, find out:

* What are the field names (``label``, ``data``, ...) and what do they correspond to?
* How many images are there?
* How many images contain ships (the ``label`` field is 1) and how many do not (``label`` is 0)
* How have the pixel values been serialized? I.e. what is the form of the ``data`` field?
* What is the maximum and minimum value of a pixel?

You may find the following commands useful:

.. code-block:: python

    type(obj)  # get the type of a Python object
    len(obj)  # get the length of a Python object

    # dataframe is a pandas DataFrame
    dataframe.info()
    dataframe.head()


In the same notebook, convert one or more of the elements of ``RAW_DATA["data"]`` (i.e. the lists of pixels) to an image, and display this image.
You will need to convert the list to a NumPy array and reshape it appropriately.

Take a look at a selection of images with ships (``label`` is 1) and without ships (``label`` is 0).
What sorts of images make up the 'no ship' class?


Commit your changes
-------------------

Once you are happy with the notebook, it's time to commit the changes to GitHub.
However, first you should make sure you have cleared all of the cell outputs from the notebook, by bringing the *Kernel* menu down and pressing *Restart Kernel and Clear All Outputs*.
The reason here is similar to the reason for not uploading the dataset; the outputs of Jupyter notebooks can contain huge amounts of data which slows down git operations.

.. warning::

    This approach to clearing the outputs of Jupyter notebooks before making a commit is quite tedious, but to my knowledge there aren't any *simple* ways to automate this.


.. note::

    If you're using GitHub Desktop, you will still follow the steps outlined below, even though you won't be typing commands.

Before commiting, let's check what has changed in the repository

.. code-block::

    git status

Unless you have many any other edits, you should see just one changed file - the notebook.

The next step is to add these files to the 'staging area',

.. code-block::

    git add .

Instead of ``.`` you can type file names explicitly; ``.`` just means 'this directory'.

To commit your changes locally, run

.. code-block::

    git commit -m "some message which explains what changes you have made"

with an appropriate message.


Finally, push the commit to the ``task-1`` branch on the remote repository (i.e. on GitHub)

.. code-block::

    git push -u origin task-1


Open a pull request
-------------------

Now that things are actually working, let's be bold and state our intentions to merge our changes into the ``main`` branch.
Github provides a nice way to do this called a 'pull request' (PR).

Go to your repository on the Github website, and navigate to the ``task-1`` branch.

Now, in the 'Pull Requests' tab, create a PR to merge ``task-1`` into ``main``.
Give your PR a sensible title, e.g. *"My attempt at task 1"*.
You can also add a description, comments, and even highlight bits of code when you make comments.

.. important:: Do not merge the pull request!


