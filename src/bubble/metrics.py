"""Metrics for measuring filter-bubble phenomena."""

import networkx as nx
from networkx.algorithms.community import modularity

"""
    Parameters
    ----------
    G : nx.Graph
        The social-network graph.  Each node must have a ``'label'``
        attribute (0 or 1).

    words_per_node : tuple[int, int]
        Number of words for label-0 and label-1 respectively.

    initial_modularity : float
        The modularity of the graph at stage 0, used as a baseline for calculating change in modularity."""

def cross_group_connectivity(
    G: nx.Graph,
    words_per_node: tuple[int, int],
    initial_modularity: float
) -> float:
    """Fraction of realized cross-group edges relative to the maximum possible.

    This serves as a proxy for "bubble burst": higher values indicate
    more interaction across group boundaries.

    Returns
    -------
    float
        Ratio in [0, 1].
    """
    counts = {0: 0, 1: 0}
    for _, attrs in G.nodes(data=True):
        label = attrs.get("label")
        counts[label] += 1

    total_possible = counts[0]*counts[1]
    if total_possible == 0:
        return 0.0

    cross_edges = sum(1 for u, v in G.edges() if G.nodes[u]["label"] != G.nodes[v]["label"])

    return float(cross_edges) / total_possible

def modularity_change(
    G: nx.Graph,
    words_per_node: tuple[int, int],
    initial_modularity: float
) -> float:
    """Change in assortativity relative to the initial stage.

    This serves as a proxy for "bubble burst": higher values indicate
    more interaction across group boundaries.

    Returns
    -------
    float
        Difference between the initial Modularity and the current modularity.
    """

    # Get the current modularity
    current_modularity = modularity(G, [[R for R, attrs in G.nodes(data=True) if attrs.get("label") == 0],
                                       [L for L, attrs in G.nodes(data=True) if attrs.get("label") == 1]])

    # Calculate the change in modularity
    modularity_change =  initial_modularity - current_modularity

    return modularity_change

def assortativity_change(
    G: nx.Graph,
    words_per_node: tuple[int, int],
    initial_modularity: float
) -> float:
    """Change in assortativity relative to the initial stage, whose value is 1.

    This serves as a proxy for "bubble burst": higher values indicate
    more interaction across group boundaries.

    Returns
    -------
    float
        Difference between the initial assortativity 
        (1) and the current assortativity.
    """

    # Get the current assortativity
    current_assortativity = nx.attribute_assortativity_coefficient(G, "label")

    # Calculate the change in assortativity
    assortativity_change = 1 - current_assortativity

    return assortativity_change
