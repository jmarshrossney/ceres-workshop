===============
Getting Started
===============

Create a new branch and Conda environment
-----------------------------------------

You know the drill by now!

Starting from the ``main`` branch, create a new branch called ``task-3``.
Push this branch to Github.

Use the ``environment.yml`` file provided in the ``tasks/task_3`` directory to create a new Conda environment called ``ceres-t3``.

.. important::
    
    Please keep an eye on the version of PyTorch Lightning that Conda installs.
    You can type ``conda list torch`` to see this.
    If it is below 1.0, let me know.
    I have found that Mamba can often resolve dependencies much better than Conda, resulting in more up-to-date packages.


Install the ``shipsnet`` package
--------------------------------

Activate your new Conda environment.

Use ``flit`` (which should be installed) to install the ``shipsnet`` package in 'editable' mode (i.e. with the ``--symlink`` option).


Standardise the input data
--------------------------

In the first task you will have found that it was important to apply some sort of standardising transform to the raw 8-bit pixels.
You'll want to apply the same transformation here.

Inside the ``shipsnet`` package there is a module called ``data`` (``data.py``) that contains 
a class ``ShipsDataModule``.
This class contains all of the instructions for downloading, transforming and splitting the dataset (neat, eh?)
You should add an appropriate standardisation transformation to the ``setup`` method, where indicated in the comments.


Commit your changes and open a PR
---------------------------------

Once you're done, commit your changes and push to GitHub and open a pull request to the ``main`` branch.


.. rubric:: Further reading: Data pipelines

The PyTorch library includes various utilities for constructing *data pipelines*.
By 'data pipeline' I mean a sequence of instructions that collects, modifies, and then returns a dataset, ready to be used in some other application.
Without wanting to dig too deep, the most important point is that a data pipeline should be **reusable** and **reproducible**.

:Reusable: We shouldn't have to rewrite the data pipeline in every new script.
:Reproducible: It should be possible to *exactly* reproduce a previous instance of the data pipeline.

The ``ShipsDataModule`` class is a subclass of ``LightningDataModule``, which comes from the PyTorch Lightning library.
It's aim is to be a *single source of truth* when it comes to questions related to the data, right the way from how it is obtained from e.g. some internet archive, through to the point at which it is passed through in batches to the model being trained.

Unfortunately the way it is actually used is fairly unintuitive if you are new to PyTorch; don't worry if you don't quite see how everything fits together!

In summary, what happens is:

1. The ``prepare_data`` method is executed, downloading/extracting the dataset
2. The ``setup`` method is executed, reading in the dataset, performing any transformations and splits
3. The ``train_dataloader`` method is called, and the resulting ``DataLoader`` is iterated over during a training epoch

Stage 3 is, roughly:

.. code-block:: python

    # This is a single training epoch!

    # training_batches is an iterator that iterates over the training dataset
    training_batches = iter(datamodule.train_dataloader())

    # iterate over all batches in the training dataset
    for i, (inputs, labels) in enumerate(training_batches):

        # pass the batch through the model and compute the loss
        loss = model.training_step((inputs, labels), i)

        # zero the gradients from the previous batch
        optimizer.zero_grad()

        # compute the gradients of the parameters wrt the loss
        loss.backward()

        # update the parameters of the model
        optimizer.step()

