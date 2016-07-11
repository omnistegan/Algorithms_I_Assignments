#!/usr/bin/env python

class Union_Find():
    def __init__(self, n):
        self.id_array = list(range(0, n))
        self.index_array = list(range(0, len(self.id_array)))

    def root(self, i):
        count = 0
        while i != self.id_array[i]:
            i = self.id_array[i]
            count += 1
        return (i, count)

    def connected(self, p, q):
        return self.root(p)[0] == self.root(q)[0]

    def union(self, p, q):
        proot, psize = self.root(p)
        qroot, qsize = self.root(q)
        # Here we apply weighting to prevent tall trees
        if psize < qsize:
            self.id_array[proot] = qroot
        else:
            self.id_array[qroot] = proot

    def show_me(self):
        print(self.index_array)
        print(self.id_array)
        for root in set(filter(lambda x : x == self.id_array[x] , self.id_array)):
            print('Root: ' + str(root) + ' : ', end='')
            print(sorted(list(filter(lambda x : self.root(x)[0] == root , self.index_array))))


uf = Union_Find(10)


uf.union(4, 3)
uf.union(3, 8)


uf.show_me()