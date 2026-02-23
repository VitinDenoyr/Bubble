"""Affinity functions used to decide whether two nodes should be connected."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def cosine_similarity(u: ArrayLike, v: ArrayLike) -> float:
    """Return the cosine similarity between two vectors.

    Parameters
    ----------
    u, v : array-like
        Probability / profile vectors of two nodes.

    Returns
    -------
    float
        Cosine similarity in [-1, 1].
    """
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    if norm_u == 0 or norm_v == 0:
        return 0.0
    return float(np.dot(u, v) / (norm_u * norm_v))


def dot_product(u: ArrayLike, v: ArrayLike) -> float:
    """Return the dot product between two vectors.

    Parameters
    ----------
    u, v : array-like
        Probability / profile vectors of two nodes.

    Returns
    -------
    float
        Dot product value.
    """
    return float(np.dot(u, v))
