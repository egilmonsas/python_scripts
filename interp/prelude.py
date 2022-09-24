import numpy as np


def linterp(x: np.ndarray, xs: np.ndarray, ys: np.ndarray) -> np.ndarray:
    if xs.ndim != 1 or ys.ndim != 1:
        raise ValueError("Vectors must be 1-dimensional")
    if len(xs) != len(ys):
        raise ValueError("Vectors must be of same length")
    return np.interp(x, xs, ys)
