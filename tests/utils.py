"""Utils for testing the randnla library"""

from __future__ import division, print_function, absolute_import
import numpy as np

# 
def make_random_dense_gaussian_matrix(n_rows, n_columns, mu=0, sigma=0.01):
    """
    TODO: Document this function
    """
    res = np.random.normal(mu, sigma, n_rows*n_columns)
    return np.reshape(res, (n_rows, n_columns))