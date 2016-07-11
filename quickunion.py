#!/usr/bin/env python

class Union_Find():
    def __init__(self, n):
        self.id_array = list(range(0, n))
        self.index_array = list(range(0, len(self.id_array)))
        self.size_array = [1] * len(self.id_array)

    def root(self, i):
        while i != self.id_array[i]:
            i = self.id_array[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        self.id_array[proot] = qroot

    def show_me(self):
        print(self.index_array)
        print(self.id_array)
        for root in set(filter(lambda x : x == self.id_array[x] , self.id_array)):
            print('Root: ' + str(root) + ' : ', end='')
            print(sorted(list(filter(lambda x : self.root(x) == root , self.index_array))))


uf = Union_Find(10)

uf.union(4, 3)
uf.union(3, 8)

uf.show_me()