"""Message generation strategies for influencer content."""

import numpy as np


def opposite_uniform_message(
    words_per_node: tuple[int, int],
    label: int,
) -> np.ndarray:
    """Create a uniform message that spreads weight across the *opposite* group's words.

    Parameters
    ----------
    words_per_node : tuple[int, int]
        Number of words for label-0 and label-1 respectively.
    label : int
        The label of the *sender* (0 or 1).

    Returns
    -------
    np.ndarray
        Message vector of length ``sum(words_per_node)`` with uniform
        weight on the opposite label's word slots.
    """
    total = int(np.sum(words_per_node))
    msg = np.zeros(total)
    if label == 1:
        msg[: words_per_node[0]] = np.ones(words_per_node[0]) / words_per_node[0]
    else:
        msg[words_per_node[0] :] = np.ones(words_per_node[1]) / words_per_node[1]
    return msg


def opposite_unique_message(
    words_per_node: tuple[int, int],
    label: int,
) -> np.ndarray:
    """Create a message that puts all weight on a single random word from the opposite group.

    Parameters
    ----------
    words_per_node : tuple[int, int]
        Number of words for label-0 and label-1 respectively.
    label : int
        The label of the *sender* (0 or 1).

    Returns
    -------
    np.ndarray
        Message vector of length ``sum(words_per_node)`` with a single
        1.0 entry in the opposite label's word range.
    """
    total = int(np.sum(words_per_node))
    msg = np.zeros(total)
    if label == 1:
        idx = np.random.randint(0, words_per_node[0])
    else:
        idx = np.random.randint(words_per_node[0], total)
    msg[idx] = 1.0
    return msg
