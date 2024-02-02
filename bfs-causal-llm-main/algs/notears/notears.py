from .linear import notears_linear

def notears(data, lambda1, loss_type, w_threshold=0.3):
    """Wrapper for NOTEARS."""
    predicted_dag = notears_linear(data, lambda1, loss_type, w_threshold=w_threshold)
    predicted_adj_mat = (predicted_dag != 0).astype(int)
    return predicted_adj_mat