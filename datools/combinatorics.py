"""Utilities implementing combinatorics algorithms"""

from math import factorial


def binomial_coefficient(n, k):
    """Computes binomial coefficient for the given input numbers.
    """

    if k < 0:
        raise ValueError('k must not be negative')

    if n < k:
        raise ValueError('n must not be lower than k')

    return int(factorial(n) / (factorial(k) * factorial(n - k)))
