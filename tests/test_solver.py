import numpy as np
from src.solver import entropy


def test_entropy():
    assert np.isclose(entropy(np.array([0.5, 0.5])), 1.0)
    assert np.isclose(entropy(np.array([0.9, 0.1])), 0.4689955935892812)
    assert np.isclose(entropy(np.array([0.1, 0.9])), 0.4689955935892812)
    assert np.isclose(entropy(np.array([0.1, 0.2, 0.7])), 1.1567796494470395)
    assert np.isclose(entropy(np.array([0.1, 0.7, 0.2])), 1.1567796494470395)
