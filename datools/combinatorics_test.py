import pytest

from datools.combinatorics import *


def test_binomial_coefficient_n_4_k_2():
    assert 6 == binomial_coefficient(4, 2)

def test_binomial_coefficient_negative_k():
    with pytest.raises(ValueError) as caught_exception:
        binomial_coefficient(4, -1)

    assert str(caught_exception.value) == 'k must not be negative'
