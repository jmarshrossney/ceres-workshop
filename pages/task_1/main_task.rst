=========
Main Task
=========

Now open the ``classifier.ipynb`` notebook in Jupyter Lab.

Run the notebook
----------------

Run all of the cells, making sure you understand what each of them are doing.

You should notice that:

* The training loss saturates (becomes constant) rather quickly
* The trained model has a classification accuracy of around 75% on the test dataset
* The reproducibility check fails


Better metrics
--------------

Look at the output of the ``ConfusionMatrixDisplay`` (the figure with four quadrants).
This tells you how the model scored on the test set in terms of:

* True positives: correct classification as having a ship
* False positives: model classifies the image as having a ship, but it doesn't
* True negatives: correct classification as having no ship
* False negatives: model classifies the image as having no ship, but it does

Given the results in this plot, think about how misleading the accuracy can be as a binary classification metric.
What accuracy would this model have acheived if 99% of the dataset had no ships in?

Your task is to compute some better classifications metrics for this model.
Luckily, all the hard work has been done by others!

Have a browse through the `classification metrics section in the Scikit-Learn documentation <https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics>`_.
Identify some good metrics and add them to the notebook alongside the accuracy.

You may also be interested in the `plotting utilities <https://scikit-learn.org/stable/modules/classes.html#id5>`_ provided by Scikit-Learn.

.. tip::

    If you're unsure which metrics to focus on, a good starting point is the `classification report <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report>`_. Make sure you understand what each of the metrics represents.


Standardise the input data
--------------------------

By now the metrics you've been calculating should have painted a very clear picture of how poor this model is performing.
It's time to fix that.

However, before you dive into tuning hyperparameters, it's worth pausing to consider the data that we're feeding into the network.
To be clear, the network receives batches of one-dimensional vectors, containing all :math:`3 \times 80 \times 80` pixel values in the image.
Each value is an integer between 0 and 255.

Data standardisation or normalisation is an important part of many data pipelines.
Why not try to rescale the pixels so that they fall between 0 and 1?
Or how about -0.5 and 0.5?
You should do this in the third cell, where the inputs are extracted from ``RAW_DATA``.


Hyper-parameter optimisation
----------------------------

The task now is simple: play around with hyperparameters until you are either satisfied with the results or too bored to continue.

If you're unsure where to start, try to answer the following questions:

* Are bigger models (as in more or larger hidden layers) always better?
* Is training for longer always better?
* What is the optimal batch size?

We can discuss our findings as a group.


Reproducibility
---------------

.. admonition:: Question

    Why is reproducibility important? What role do random number generators play in terms of reproducible computations?

Scroll to the end of the notebook to the section called *Reproducibility check*.
Your task is to modify the code so that the process of splitting the data and training a model is reproducible.

You will see that, in each of the two cells that defines and trains a model, there is a line

.. code-block:: python

    rng = np.random.RandomState(SEED)

This initialised as *pseudo-random number generator* (pRNG) with a known *seed*.
You will need to figure out how to use this pRNG in ``test_train_split`` and ``MLPClassifier`` - i.e. the two parts of the code that involve pseudo-random processes.

.. hint:: Remember, you can use ``?`` to bring up the help documentation for a Python object


Once you have done this and the ``assert`` statement at the bottom of the notebook is passing, you're ready to move on!


