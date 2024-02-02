import numpy as np
import igraph as ig

def is_dag(W: np.ndarray) -> bool:
    """
    Returns ``True`` if ``W`` is a DAG, ``False`` otherwise.
    """
    G = ig.Graph.Weighted_Adjacency(W.tolist())
    return G.is_dag()

def dag_to_adj_mat(dag):
    # Transform causal learn format into bn format
    n = len(dag.graph)
    adj_mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if dag.graph[i][j] == -1:
                adj_mat[i][j] = 1
    return adj_mat

def adj_mat_to_edge_list(adj_mat):
    n = adj_mat.shape[0]
    edge_list = []
    for i in range(n):
        for j in range(n):
            if adj_mat[i][j] == 1:
                edge_list.append((i, j))
    return edge_list

