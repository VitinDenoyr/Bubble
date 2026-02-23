"""Metrics for measuring filter-bubble phenomena."""

from __future__ import annotations

from typing import Tuple

import networkx as nx


def cross_group_connectivity(
    G: nx.Graph,
    words_per_node: Tuple[int, int],
) -> float:
    """Fraction of realised cross-group edges relative to the maximum possible.

    This serves as a proxy for "bubble burst": higher values indicate
    more interaction across group boundaries.

    Parameters
    ----------
    G : nx.Graph
        The social-network graph.  Each node must have a ``'label'``
        attribute (0 or 1).
    words_per_node : tuple[int, int]
        Number of words for label-0 and label-1 respectively.

    Returns
    -------
    float
        Ratio in [0, 1].
    """
    total_possible = words_per_node[0] * words_per_node[1]
    if total_possible == 0:
        return 0.0

    cross_edges = 0
    for n1 in range(len(G.nodes)):
        for n2 in range(n1 + 1, len(G.nodes)):
            if G.nodes[n1]["label"] != G.nodes[n2]["label"] and G.has_edge(n1, n2):
                cross_edges += 1

    return cross_edges / total_possible
