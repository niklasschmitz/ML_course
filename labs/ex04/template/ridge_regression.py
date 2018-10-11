# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    N, M = tx.shape
    w = np.linalg.inv(tx.T @ tx + lambda_*(2*N) * np.identity(M)) @ (tx.T @ y)
    
    return w
