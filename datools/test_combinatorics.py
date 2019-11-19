"""Unit tests for the module combinatorics"""

import unittest


class TestCombinatorics(unittest.TestCase):

    def test_binomial_coefficient_4_2(self):
        result = combinatorics.binomial_coefficient(4, 2)
        self.assertEqual(result, 6)

    def test_binomial_coefficient_negative_k(self):
        self.assertRaises(ValueError, combinatorics.binomial_coefficient, 4, -2)

    def test_binomial_coefficient_lower_n(self):
        """binomial_coefficient raises an exception for n < k"""

        with self.assertRaises(ValueError) as caught:
            combinatorics.binomial_coefficient(2, 4)

        self.assertEqual(str(caught.exception), 'n must not be lower than k')


if __name__ == '__main__':
    import combinatorics
    unittest.main()
else:
    from . import combinatorics
