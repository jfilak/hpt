"""This module provides helper functionality for Data Analysis tasks."""


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
