import json
import logging
from pathlib import Path
from typing import Union

import torch
from torch.utils.data import Dataset, DataLoader, random_split
from pytorch_lightning import LightningDataModule
from kaggle.api.kaggle_api_extended import KaggleApi

log = logging.getLogger(__name__)

DATA_DIR =  Path(__file__).parent.parent.joinpath("data")


def load_data_from_json(data_dir: Union[str, Path] = DATA_DIR) -> dict:
    """Reads data from json file and returns dict."""
    data_dir = Path(str(data_dir))
    data_json = data_dir / "shipsnet.json"
    with data_json.open("r") as file:
        data_dict = json.load(file)
    return data_dict


class LabelledTensorDataset(Dataset):
    """
    Dataset comprising tensors and corresponding class labels.

    Each element is a tuple (tensor, label).
    """
    def __init__(self, data: torch.Tensor, labels: torch.Tensor) -> None:
        super().__init__()
        assert len(data) == len(labels)
        self.data = data
        self.labels = labels

    def __len__(self) -> int:
        return len(self.labels)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, int]:
        return self.data[idx], self.labels[idx]


class ShipsDataModule(LightningDataModule):
    """
    Data module for ...
    """
    def __init__(
        self,
        batch_size: int = 32,
        train_frac: float = 0.75,
        random_split_seed: int = 123456789,
        data_dir: Union[str, Path] = DATA_DIR,
    ) -> None:
        super().__init__()
        self.batch_size = batch_size
        self.train_frac = train_frac
        self.data_dir = Path(str(data_dir)).resolve()
        self.random_split_seed = random_split_seed

        self.save_hyperparameters(ignore="data_dir")

    def prepare_data(self) -> None:
        """Downloads and extracts the dataset."""
        # Skip if data exists already
        json_file = self.data_dir / "shipsnet.json"
        if json_file.exists():
            log.info(f"Found existing dataset at '{json_file}'")
            return

        kaggle_api = KaggleApi()
        kaggle_api.authenticate()
        kaggle_api.dataset_download_files(
            dataset="rhammell/ships-in-satellite-imagery",
            path=str(self.data_dir),
            force=False,  # skip if already downloaded
            quiet=False,
            unzip=True,
        )

    def setup(self, stage: Union[str, None] = None) -> None:
        """Reads raw data, applies transformations and splits."""
        data_dict = load_data_from_json(self.data_dir)

        # Convert to torch.Tensor
        pixels = torch.tensor(data_dict["data"], dtype=torch.float).view(-1, 3, 80, 80)
        labels = torch.tensor(data_dict["labels"], dtype=torch.bool)

        # Apply standardising transformations here:
        pixels = (pixel/255)*2-1

        self.full_dataset = LabelledTensorDataset(pixels, labels)

        # Split into train / validation / test
        n_tot = len(self.full_dataset)
        n_train = int(n_tot * self.train_frac)
        n_val = (n_tot - n_train) // 2
        n_test = n_tot - n_val - n_train

        self.train_dataset, self.val_dataset, self.test_dataset = random_split(
            self.full_dataset,
            [n_train, n_val, n_test],
            generator=torch.Generator().manual_seed(self.random_split_seed),
        )

    def train_dataloader(self):
        return DataLoader(self.train_dataset, self.batch_size)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, self.batch_size)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, self.batch_size)
