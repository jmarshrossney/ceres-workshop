import pytorch_lightning as pl
import torch
from torchmetrics.functional import (
    accuracy,
    precision_recall,
    f1_score,
    matthews_corrcoef,
)


class Classifier(pl.LightningModule):
    def forward(self, data: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError

    def on_train_start(self):
        if self.logger is None:
            return

        hparams = self.hparams | self.trainer.datamodule.hparams
        metrics = {
            "val/accuracy": 0,
            "val/precision": 0,
            "val/recall": 0,
            "val/matthews": 0,
        }
        self.logger.log_hyperparams(hparams, metrics)

    def training_step(self, batch, batch_idx):
        data, labels = batch
        data.requires_grad_()
        preds = self(data)

        loss = torch.nn.functional.binary_cross_entropy(preds, labels.float())
        accu = accuracy(preds, labels)

        self.log("train/loss", loss, on_step=False, on_epoch=True, prog_bar=True)
        self.log("train/accuracy", accu, on_step=False, on_epoch=True)

        return loss

    def validation_step(self, batch, batch_idx):
        data, labels = batch
        preds = self(data)

        loss = torch.nn.functional.binary_cross_entropy(preds, labels.float())
        accu = accuracy(preds, labels)
        precision, recall = precision_recall(preds, labels)
        matthews = matthews_corrcoef(preds, labels, 2)

        self.log("val/loss", loss, on_step=False, on_epoch=True)
        self.log("val/accuracy", accu, on_step=False, on_epoch=True)
        self.log("val/precision", precision, on_step=False, on_epoch=True)
        self.log("val/recall", recall, on_step=False, on_epoch=True)
        self.log("val/matthews", matthews, on_step=False, on_epoch=True)

    def test_step(self, batch, batch_idx):
        data, labels = batch
        preds = self(data)

        loss = torch.nn.functional.binary_cross_entropy(preds, labels.float())
        accu = accuracy(preds, labels)
        precision, recall = precision_recall(preds, labels)
        matthews = matthews_corrcoef(preds, labels, 2)

        self.log("test/loss", loss, on_step=False, on_epoch=True)
        self.log("test/accuracy", accu, on_step=False, on_epoch=True)
        self.log("test/precision", precision, on_step=False, on_epoch=True)
        self.log("test/recall", recall, on_step=False, on_epoch=True)
        self.log("test/matthews", matthews, on_step=False, on_epoch=True)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters())
        return optimizer


class MLPClassifier(Classifier):
    def __init__(
        self,
        hidden_shape: list[int],
        activation: str,
    ) -> None:
        super().__init__()
        self.save_hyperparameters()

        net_shape = [3 * 80 * 80, *hidden_shape, 1]
        self.layers = torch.nn.ModuleList(
            [
                torch.nn.Linear(in_features, out_features)
                for in_features, out_features in zip(net_shape[:-1], net_shape[1:])
            ]
        )
        self.activation = getattr(torch.nn.functional, activation)

    def forward(self, data: torch.Tensor) -> torch.Tensor:
        x = data.flatten(start_dim=1)
        *all_but_final_layer, final_layer = self.layers

        for layer in all_but_final_layer:
            x = self.activation(layer(x))

        preds = torch.sigmoid(final_layer(x))

        return preds.squeeze()


class CNNClassifier(Classifier):
    def __init__(
        self, hidden_shape: list[int], activation: str, kernel_size: int
    ) -> None:
        super().__init__()
        self.save_hyperparameters()

        net_shape = [3, *hidden_shape]
        self.layers = torch.nn.ModuleList(
            [
                torch.nn.Conv2d(in_channels, out_channels, kernel_size)
                for in_channels, out_channels in zip(net_shape[:-1], net_shape[1:])
            ]
        )
        self.layers.append(torch.nn.LazyLinear(1))
        self.activation = getattr(torch.nn.functional, activation)

    def forward(self, data: torch.Tensor) -> torch.Tensor:
        x = data
        *all_but_final_layer, final_layer = self.layers

        for layer in all_but_final_layer:
            x = self.activation(layer(x))

        preds = torch.sigmoid(final_layer(x.flatten(start_dim=1)))

        return preds.squeeze()
