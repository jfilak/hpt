import pytest

from datools.types import NChooseK

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, NChooseK) and isinstance(right, NChooseK) and op == '==':
        result = [f'{left} != {right}']

        if left.n != right.n:
            result.extend([f'  Expected N: {left.n}', f'  Got      N: {right.n}'])

        if left.k != right.k:
            result.extend([f'  Expected K: {left.k}', f'  Got      K: {right.k}'])

        return result


@pytest.fixture(scope='module')
def salute(request):
    our_name = getattr(request.module, 'my_name', 'datools')
    return f'Hello, {our_name}!'
