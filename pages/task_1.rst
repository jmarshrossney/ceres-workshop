.. image:: ../assets/sfbay.png

=======================================
Task 1: A Binary Classification Problem
=======================================

As with many Machine Learning introduction courses, we're going to consider a binary classification task as a pedagogical example.
The task will be to construct a model that takes a satellite image as its input, and answers the question: does this image contain a ship? [#f1]_

.. note:: You might not be remotely interested in binary classification for your own research, but this workshop isn't really about applying sophisticated ML techniques to hard problems, it's about doing the basics well!

Before we start, have a quick think about the following questions.

:Code structure: How should we organise a project in a way that maximises clarity and reusability.
:Overfitting: How can we use a validation dataset to avoid overfitting.
:Metrics: Being critical about the use of metrics; each metric has its own merits and drawbacks, which make it more or less suited to a particular task.
:Unbiased reporting of results: Understanding the role of the test dataset in ensuring reported scores are unbiased.
:Reproducibility: How to ensure that we, and others, can reproduce our results *exactly*. 

The code for this task (and the third) is based on `this repository <https://github.com/marshrossney/ships-in-satellite-imagery>`_.
Feel free to refer to this as you go, although I only really expect it to be helpful for the extension tasks.

.. rubric:: Contents

.. toctree:: 

    task_1/getting_started
    task_1/main_task
    task_1/extension
    task_1/finishing_up


.. rubric:: Footnotes

.. [#f1] It's not hard to imagine situations in which such a model could be of use, either for logistical or law enforcement purposes.
