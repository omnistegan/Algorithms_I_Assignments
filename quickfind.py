#!/usr/bin/env python

class Union_Find():
    def __init__(self, n):
        self.id_array = list(range(0, n))

    def connected(self, p, q):
        return self.id_array[p] == self.id_array[q]

    def union(self, p, q):
        pid = self.id_array[p]
        qid = self.id_array[q]
        for i, id in enumerate(self.id_array):
            if id == pid:
                self.id_array[i] = qid

    def show_me(self):
        print(list(range(0, len(self.id_array))))
        print(self.id_array)
        for group in set(self.id_array):
            print('{ ', end='')
            for i, id in enumerate(self.id_array):
                if id == group:
                    print(i, end=' ')
            print('}')

uf = Union_Find(10)

'''
uf.union(3, 4)
uf.union(3, 5)
uf.union(7, 9)
uf.union(1, 0)
uf.union(2, 6)
uf.union(9, 6)
'''

uf.union(4, 3)
uf.union(3, 8)

uf.show_me()