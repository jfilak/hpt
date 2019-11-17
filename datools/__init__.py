"""This module provides helper functionality for Data Analysis tasks.

In case you are not happy with the default seed for our RNGs

>>> get_seed()
331999

you can use the function set_seed to change it.

>>> set_seed(17)
>>> get_seed()
17
"""


_SEED = 331999


def get_seed():
    """Returns the common seed number for pseudo random number generators used
    by this module.
    """

    return _SEED


def set_seed(new_seed):
    """Sets the common seed number for pseud random number generators used by
    this module.
    """

    _SEED = new_seed
