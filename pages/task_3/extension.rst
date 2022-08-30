============================
Extension: Competition time!
============================

TODO: where to upload best model.

To ensure that everyone is using the data training, validation and test data, you should load the datamodule as follows:

.. code-block:: python

    datamodule = ShipsDataModule(
        batch_size=whatever_you_like,
        train_frac=0.75,
        random_split_seed=123456789,
    )

Some things to try:

* Change the parameters of the ``MLPClassifier`` model
* ``CNNClassifier``

If you are feeling adventurous, you might enjoy creating your own model by subclassing ``shipsnet.models.Classifier`` and overriding the ``__init__`` and ``forward`` methods, as follows:

.. code-block:: python

    from shipsnet.models import Classifier

    class MyModel(Classifier):

        def __init__(self, *args, **kwargs):
            super().__init__()

            # define your trainable layers here, e.g.
            # self.linear_layer = torch.nn.Linear(3 * 80 * 80, 100)
            # self.conv_layer = torch.nn.Conv2d(3, 3, kernel_size=9)
            ...

        def forward(self, data: torch.Tensor) -> torch.Tensor:
            """
            Transforms input data into class predictions.

            Arguments:
                data:
                    A Tensor of shape (N, 3, 80, 80) where N is the
                    batch size

            Returns:
                torch.Tensor:
                    A Tensor of shape (N,) containing predicted probabilities
                    (between 0 and 1) for the classes
            """
            # Define the forward pass of the model here
            ...

Some potentially interesting things to try are:

* `Pooling layers <https://pytorch.org/docs/stable/nn.html#pooling-layers>`_
* `Dropout layers <https://pytorch.org/docs/stable/nn.html#dropout-layers>`_
* `Batch normalisation <https://pytorch.org/docs/stable/nn.html#normalization-layers>`_
