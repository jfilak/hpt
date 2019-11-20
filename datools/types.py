"""Definition of comment types"""

class NChooseK:

    def __init__(self, n, k):
        self.n = n
        self.k = k

    def __repr__(self):
        return f'NChooseK({self.n}, {self.k})'

    def __eq__(self, other):
        if other is None:
            return False

        return self.n == other.n and self.k == other.k
