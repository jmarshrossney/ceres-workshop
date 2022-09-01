============
Finishing up
============


Test your best model
--------------------

Once you've trained a selection of models and identified the one that performs best on the *validation* dataset, it's time to see how that model performs on the *test* dataset.

Open the ``test_best_model.ipynb`` notebook.

Modify the ``best_model_path`` to point to the checkpoint file for your best model (this can be found under the *hparams* tab on tensorboard.
If your best model wasn't an instance of ``MLPClassifier``, change ``ModelClass`` to point to the class that your model belongs to.
Now you should be able to load this model using ``ModelClass.load_from_checkpoint``.

Run the cell that tests the model.

How did you do?


Push your changes and merge the pull request
--------------------------------------------

You know the drill by now!
Commit your changes, being careful to clear the outputs of the Jupyter notebooks, push the commit to GitHub, and merge your pull request to the ``main`` branch.

You've completed the third task - **congratulations!**
