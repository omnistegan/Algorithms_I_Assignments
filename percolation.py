#!/usr/bin/env python

from quickunion03 import Union_Find
from random import randrange
from statistics import mean, stdev

class Perc_Grid():

    def __init__(self, n):
        # Init a grid size n squared with all spaces initially blocked
        self.uf = Union_Find((n*n)+2)
        # UF index -1 and -2 reserved for virtual percolation test points
        for each in list(range(n)):
            self.uf.union(-2, each)
        for each in list(range(-2-n, -2)):
            self.uf.union(-1, each)
        self.size = n
        self.grid = [[False for x in range(n)] for y in range(n)]
        self.count = 0

    def uf_index(self, x, y):
        # Return UF index for our 2d x, y coords
        return (y*self.size)+x

    def open_random_blocked(self):
        # Find a randomly selected blocked space and perform self.open() in it.
        while True:
            randx, randy = (randrange(self.size), randrange(self.size))
            if not self.grid[randy][randx]:
                self.open(randx, randy)
                break

    def open(self, x, y):
        # Perform opening and unioning operations on a new space
        self.grid[y][x] = True
        self.count += 1
        new_ufi = self.uf_index(x, y)
        # Must union with neighbouring open spaces
        neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        # Filter out of range neighbours
        neighbours = [space for space in neighbours if self.size not in space and -1 not in space]
        nei_ufi = []
        for each in neighbours:
            if self.grid[each[1]][each[0]]:
                nei_ufi.append(self.uf_index(*each))
        for each in nei_ufi:
            self.uf.union(new_ufi, each)

    def percolates(self):
        return self.uf.connected(-1, -2)

    def show_me(self):
        for each in pc.grid:
            for item in each:
                if item is False:
                    print('X', end='')
                else:
                    print(' ', end='')
            print()
    
    def percent_filled(self):
        return self.count/(self.size*self.size)

def perform_tests(grid_size, tests):
    probabilities = []
    for i in range(tests):
        pc = Perc_Grid(grid_size)
        while not pc.percolates():
            pc.open_random_blocked()
        probabilities.append(pc.percent_filled())
    print('mean = ' + str(mean(probabilities)))
    print('stddev = ' + str(stdev(probabilities)))