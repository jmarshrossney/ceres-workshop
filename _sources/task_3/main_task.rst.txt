=========
Main Task
=========

Train a classifier
------------------

Open the ``mlp_classifier.ipynb`` notebook.
Within it are instructions to train and run a feed-forward neural network classifier that is entirely analogous to the one in the first task.

The cells should run without needing to be modified.
Run each cell one-at-a-time.
As you are doing so, try to understand what each line is doing. [#f1]_
Feel free to ask me!


Change some hyperparameters
---------------------------

Based on your intuition from the first task, play around with the hyperparameters (hidden layer sizes, activation function etc).
Train four or five models before moving onto the next section.


Introducing Tensorboard
-----------------------

At the end of the notebook there is a rather strange looking cell

.. code-block::

    %load_ext tensorboard
    %tensorboard --logdir lightning_logs

which you should run.

Hopefully, you should see a `Tensorboard <https://www.tensorflow.org/tensorboard/>`_ window appear in the notebook.
Browse around the tabs and plots.
While you are doing this, look back at the earlier cells and try to understand which lines of code were relevant to producing this tensorboard.


.. rubric:: Footnotes


.. [#f1] Don't worry if it's not clear; in many ways PyTorch and PyTorch Lightning have together succeeded in being highly flexible and yet easy to read, but there are also many areas where using them feels a bit like pressing a button on a black box.
