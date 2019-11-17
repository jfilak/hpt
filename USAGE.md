# Programming

Start with importing the module:

    >>> import datools

## Initialization

It might be necessary to change seed for RNGs which is by default:

    >>> datools.get_seed()
    331999

To change the value you can use the function;

    >>> datools.set_seed(17)
    >>> datools.get_seed()
    17

## API

### Combinatorics

Star with importing the module:

    >>> from datools import combinatorics

To get number of possible combinations also known as binomial coefficient you
can use the function:

    >>> combinatorics.binomial_coefficient(4, 2)
    6

The function raises ValueError exception, if the parameters of the function do
not meed the following expectations:

The first argument n is higher or equal to the second one:

    >>> combinatorics.binomial_coefficient(4, -1)
    Traceback (most recent call last):
        ...
    ValueError: k must not be negative

and the second argument is not lower than the first one:

    >>> combinatorics.binomial_coefficient(2, 4)
    Traceback (most recent call last):
        ...
    ValueError: n must not be lower than k
