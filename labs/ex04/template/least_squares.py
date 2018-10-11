# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np
from costs import compute_mse


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************
    tx_gram = tx.T @ tx  # gram matrix
    b = (tx.T @ y)
    w = np.linalg.solve(tx_gram, b)
    
    loss = compute_mse(y, tx, w)
    
    return loss, w
