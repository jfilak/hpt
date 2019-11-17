"""Utilities implementing combinatorics algorithms"""

from math import factorial


def binomial_coefficient(n, k):
    """Computes binomial coefficient for the given input numbers.

    >>> binomial_coefficient(4, 2)
    6

    >>> binomial_coefficient(4, -1)
    Traceback (most recent call last):
        ...
    ValueError: k must not be negative

    >>> binomial_coefficient(2, 4)
    Traceback (most recent call last):
        ...
    ValueError: n must not be lower than k
    """

    if k < 0:
        raise ValueError('k must not be negative')

    if n < k:
        raise ValueError('n must not be lower than k')

    return int(factorial(n) / (factorial(k) * factorial(n - k)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
