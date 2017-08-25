from __future__ import division, print_function, absolute_import

import numpy as np

__all__ = ['clarkson_woodruff_transform']

def cwt_matrix(n_rows, n_columns):
    """
    TODO: Document Function
    """
    S = np.zeros((n_rows, n_columns))
    nz_positions = np.random.randint(0, n_rows, n_columns)
    values = np.random.choice([1, -1], n_columns)
    for i in range(n_columns):
        S[nz_positions[i]][i] = values[i]
    
    return S

def clarkson_woodruff_transform(input_matrix, sketch_size, direcction="rows"):
    """
    Given a matrix A (input_matrix) of size (n, d), compute a matrix A' of size  (n, s) which holds:
        $||Ax|| = (1 \pm \epsilon) ||A'x||$
    with high probability.
    To obtain A' we create a matrix S of size (d, s) where every column of transpose(S) has only one position distinct to zero
    with value +1 or -1. We multiply S*A to obtain A'.
    Parameters
    ----------
    input_matrix (A) : (n, d) array_like
        Input matrix
    n_columns (s) : int
        number of columns for A'
    Returns
    -------
    A' : (n, s) array_like
        Sketch of A
    Notes
    -----
    This is an implementation of the Clarckson-Woodruff Transform (also known as CountSketch) introduced for
    first time in Kenneth L. Clarkson and David P. Woodruff. Low rank approximation and regression in input sparsity time. In STOC, 2013.
    A' can be computed in O(nnz(A)) but we don't take advantage of sparse matrix in this implementation
    """
    #TODO: Rewrite function documentation

    if (direcction == "rows"):
        S = cwt_matrix(sketch_size, input_matrix.shape[0])
        return np.dot(S, input_matrix)
    elif (direcction == "columns"):
        S = cwt_matrix(input_matrix.shape[1], sketch_size)
        return np.dot(input_matrix, S)
    else:
        raise ValueError('Value of direrction must be "rows" or "columns"')
