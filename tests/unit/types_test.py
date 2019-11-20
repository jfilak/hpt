from datools.types import NChooseK


def test_n_choose_k_constructor_assignments_false():
    lhs = NChooseK(4, 2)
    rhs = NChooseK(4, 1)

    assert lhs == rhs
