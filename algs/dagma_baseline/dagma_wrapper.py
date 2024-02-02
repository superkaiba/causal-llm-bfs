from dagma.linear import DagmaLinear
from dagma.nonlinear import DagmaNonlinear, DagmaMLP
import torch
import numpy as np

def dagma_nonlinear_wrapper(data, dim, lambda1, lambda2):
    """
    Wrapper for GES algorithm from causallearn package. Takes in data and returns adjacency matrix of a DAG
    """
    eq_model = DagmaMLP(dims=[dim, 10, 1], bias=True, dtype=torch.double) # create the model for the structural equations, in this case MLPs
    model = DagmaNonlinear(eq_model, dtype=torch.double) # create the model for DAG learning
    W_est = model.fit(data, lambda1=lambda1, lambda2=lambda2)
    W_est = (W_est != 0)
    return W_est

def dagma_linear_wrapper(data, lambda1):
    model = DagmaLinear(loss_type='l2') # create a linear model with least squares loss
    W_est = model.fit(data.astype(np.float64), lambda1=lambda1) # fit the model with L1 reg. (coeff. 0.02)
    W_est = (W_est != 0)
    return W_est
