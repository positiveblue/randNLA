"""Testing the Clarkson Woodruff Transform"""

from __future__ import division, print_function, absolute_import
import numpy as np
from numpy.testing import assert_almost_equal
import pytest

from randnla.cwt_sketch import clarkson_woodruff_transform

from .utils import make_random_dense_gaussian_matrix


class TestCWT:
    """
    Testing the Clarkson Woodruff Transform
    """
    # Big dense matrix dimensions
    n_matrix_rows = 2000
    n_matrix_columns = 100

    # Sketch matrix dimensions
    n_sketch_rows = 100
    n_sketch_columns = 20

    # Repetitions/max_errors per test
    repetitions_per_test = 10
    n_max_errors = 3

    # Error threshold
    threshold = 0.1

    dense_big_matrix = make_random_dense_gaussian_matrix(n_matrix_rows,
        n_matrix_columns)
    

    def test_sketch_rows_dimensions(self):
        """
        TODO: Explain what this test does
        """
        sketch = clarkson_woodruff_transform(
            self.dense_big_matrix,
            self.n_sketch_rows,
            direcction="rows"
        )

        assert(
            sketch.shape == (
                self.n_sketch_rows,
                self.dense_big_matrix.shape[1]
            )
        )

    def test_sketch_columns_dimensions(self):
        """
        TODO: Explain what this test does
        """
        sketch = clarkson_woodruff_transform(
            self.dense_big_matrix,
            self.n_sketch_columns,
            direcction="columns"
        )

        assert(
            sketch.shape == (
                self.dense_big_matrix.shape[0],
                self.n_sketch_columns
            )
        )

    def test_sketch_rows_norm(self):
        """
        TODO: Explain what this test does
        """

        n_errors = 0
        for _ in range(self.repetitions_per_test):
            sketch = clarkson_woodruff_transform(
                self.dense_big_matrix,
                self.n_sketch_rows,
                direcction="rows"
            )
        
            err = np.linalg.norm(self.dense_big_matrix) - np.linalg.norm(sketch)
            if err > self.threshold:
                n_errors+=1
        
        assert (n_errors <= self.n_max_errors)
    
    
    def test_sketch_columns_norm(self):
        """
        TODO: Explain what this test does
        """

        n_errors = 0
        for _ in range(self.repetitions_per_test):
            sketch = clarkson_woodruff_transform(
                self.dense_big_matrix,
                self.n_sketch_columns,
                direcction="columns"
            )

            err = np.linalg.norm(self.dense_big_matrix, ord=2) - np.linalg.norm(sketch, ord=2)
            
            if err > self.threshold:
                n_errors+=1
        
        assert (n_errors <= self.n_max_errors)
