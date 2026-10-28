import random

import numpy as np
import torch

from dense_retrieval.utils import set_seed


def test_set_seed_reproduces_random_values() -> None:
    set_seed(42)

    python_value = random.random()
    numpy_value = np.random.rand()
    torch_value = torch.rand(1).item()

    set_seed(42)

    assert random.random() == python_value
    assert np.random.rand() == numpy_value
    assert torch.rand(1).item() == torch_value