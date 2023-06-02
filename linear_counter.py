import hashlib

class LinearCounter:
    def __init__(self, m):
        self.mask = [False] * m
        self.m = m

    def add(self, value):
        position = self._hash(value) % self.m
        self.mask[position] = True

    def print_mask(self):
        print(self.mask)

    def _hash(self, x):
        md5 = hashlib.md5(str(hash(x)).encode('utf-8'))
        # md5.update(str(0))
        return int(md5.hexdigest(), 16) % self.m
    