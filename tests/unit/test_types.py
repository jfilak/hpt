"""datools/types.py tests"""

import unittest

from datools.types import NChooseK


class CombinatoricsAsserts:

    def assertNChooseKEqual(self, first, second, msg=None):
        self.assertIsInstance(first, NChooseK, 'First argument is not an NChooseK')
        self.assertIsInstance(second, NChooseK, 'Second argument is not an NChooseK')

        diff_msg = ''
        if first.n != second.n:
            diff_msg += f'  Expected N: {first.n}\n  Got      N: {second.n}'

        if first.k != second.k:
            diff_msg += f'  Expected K: {first.k}\n  Got      K: {second.k}'

        if diff_msg:
            message = f'{first} != {second}\n{diff_msg}'
            if msg:
                message = f'{mesage}\n: {msg}'

            self.fail(message)


class CombinatoricsTestCase(unittest.TestCase, CombinatoricsAsserts):

    def __init__(self, *args, **kwargs):
        super(CombinatoricsTestCase, self).__init__(*args, **kwargs)

        self.addTypeEqualityFunc(NChooseK, 'assertNChooseKEqual')


class TestTypesNChooseK(CombinatoricsTestCase):

    def test_n_choose_k_constructor_assignments(self):
        lhs = NChooseK(4, 2)
        rhs = NChooseK(4, 2)

        self.assertEqual(lhs, rhs)

    def test_n_choose_k_constructor_assignments_false(self):
        lhs = NChooseK(4, 2)
        rhs = NChooseK(4, 1)

        #import pdb; pdb.set_trace()
        self.assertEqual(lhs, rhs)

    def test_n_choose_k_str(self):
        self.assertEqual(str(NChooseK(4, 2)), 'NChooseK(4, 2)')
