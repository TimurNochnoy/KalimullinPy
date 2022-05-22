class Iterator:

    def __init__(self, n):
        self.n = n
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.k < self.n:
            self.k += 1
            return self.k ** 2
        else:
            raise StopIteration
