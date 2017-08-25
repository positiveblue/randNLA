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
        sketch = clarkson_woodruff_transform(
            self.dense_big_matrix,
            self.n_sketch_rows,
            direcction="rows"
        )
        
        assert_almost_equal(
            np.linalg.norm(self.dense_big_matrix), np.linalg.norm(sketch), decimal=1)
    
    
    def test_sketch_columns_norm(self):
        """
        TODO: Explain what this test does
        """
        sketch = clarkson_woodruff_transform(
            self.dense_big_matrix,
            self.n_sketch_columns,
            direcction="columns"
        )

        #TODO: check how sketching by columns affects to the norm
