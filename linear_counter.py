import hashlib

class LinearCounter:
    def __init__(self, m):
        self.mask = [False] * m
        self.m = m

    def clear(self):
        self.mask = [False] * self.m

    def bit(self, i):
        return self.mask[i]

    def add(self, value):
        position = self.hash(value) % self.m
        self.mask[position] = True

    def print_mask(self):
        print(self.mask)

    def hash(self, x):
        md5 = hashlib.md5(str(hash(x)).encode('utf-8'))
        return int(md5.hexdigest(), 16) % self.m
    
    def estimate_cardinality(self):
        return self.mask.count(True)
    