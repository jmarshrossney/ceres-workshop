=========
Main Task
=========

Check the data is being loaded correctly
----------------------------------------

The PyTorch library includes various utilities for constructing *data pipelines*.
By 'data pipeline' I mean a sequence of instructions that collects, modifies, and then returns a dataset, ready to be used in some other application.
Without wanting to dig too deep, the most important point is that a data pipeline should be **reusable** and **reproducible**.

Reusable
    We shouldn't have to rewrite the data pipeline in every new script.

Reproducible
    It should be possible to *exactly* reproduce a previous instance of the data pipeline.

We are going to use the ``LightningDataModule`` from the PyTorch Lightning library.
This simplifies 

The way data is loaded into the model is as follows:

.. code-block:: python

    # get an object that iterates over the training dataset
    training_batches = iter(datamodule.train_dataloader())

    # Get the first training batch
    inputs, labels = next(training_batches)

Open your ``data_check.ipynb`` notebook in Jupyter Lab.
Check that the data is being loaded correctly by visualising some of the elements of ``inputs`` using ``array_to_rgb_image`` and ``plt.imshow``.

.. note::

    Imshow expects inputs between 0 and 1. You may need to undo the effect of transforms of the data


Visualise the outputs
---------------------

.. code-block::

    %load_ext tensorboard
    %tensorboard --logdir lightning_logs

