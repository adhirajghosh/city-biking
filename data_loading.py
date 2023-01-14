import os
import sys
import time
import datetime
import os.path as osp
import numpy as np
import warnings
from torch.utils.data import Dataset

class CitiBikeDataset(Dataset):
    """Citi Biking dataset."""

    def __init__(self, dataset, root_dir, transform=None):

        self.dataset = dataset
        self.root_dir = root_dir

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return
