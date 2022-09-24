import unittest

import numpy as np
from interp.prelude import linterp


class test_linterp(unittest.TestCase):
    def test_linterp(self):
        self.assertTrue(
            linterp(np.array(1), np.array([1, 2, 3]), np.array([1, 2, 3])) == np.array(1))

    def test_defence_clause(self):
        with self.assertRaises(ValueError):
            linterp(np.array(1), np.array(
                [[1, 2, 3], [1, 2, 3]]), np.array([1, 2, 3]))
