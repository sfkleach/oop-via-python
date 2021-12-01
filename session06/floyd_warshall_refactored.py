"""
Refactored shortest path example.
Taken from http://rosettacode.org/wiki/Floyd-Warshall_algorithm#Python
"""

from math import inf
from itertools import product

class Graph:
    def __init__(self, n, edge):
        self._n = n
        self._edge = edge
    def range(self):
        return range(self._n)
    def newShortestPaths(self):
        return ShortestPathsFactory(self).newShortestPaths()
    def initial_dist(self):
        d = [[inf] * self._n for i in self.range()]
        for i in self.range():
            d[i][i] = 0        
        return d
    def initial_nxt(self):
        return [[0]   * self._n for i in self.range()]
    def edges(self):
        yield from self._edge

class ShortestPathsFactory:
    def __init__(self, graph):
        # Take a coherent snapshot of the graph, so we are independent 
        # of updates of the graph.
        self._range = graph.range()
        self._dist = graph.initial_dist()
        self._nxt = graph.initial_nxt()
        for u, v, w in graph.edges():
            self._dist[u-1][v-1] = w
            self._nxt[u-1][v-1] = v-1
        self._needs_calcShortestPaths = True
    def _updatePathIfShorterVia(self, i, j, k):
        sum_ik_kj = self._dist[i][k] + self._dist[k][j]
        if self._dist[i][j] > sum_ik_kj:
            self._dist[i][j] = sum_ik_kj
            self._nxt[i][j]  = self._nxt[i][k]
    def _calcShortestPaths(self):
        for k, i, j in product(self._range, repeat=3):
            self._updatePathIfShorterVia(i, j, k)
    def calcShortestPathsIfNeeded(self):
        if self._needs_calcShortestPaths:
            self._calcShortestPaths()
            self._needs_calcShortestPaths = False
    def newShortestPaths(self):
        self.calcShortestPathsIfNeeded()            
        return ShortestPaths(self._range, self._dist, self._nxt)

class ShortestPaths:
    def __init__(self, rn, dist, nxt):
        self._range = rn
        self._dist = dist
        self._nxt = nxt
    def shortestPath(self, i, j):
        path = [i]
        while path[-1] != j:
            path.append(self._nxt[path[-1]][j])
        return path
    def printShortestPaths(self):
        print("pair     dist    path")
        for i, j in product(self._range, repeat=2):
            if i != j:
                path = self.shortestPath(i, j)
                pathstr = ' → '.join(str(p + 1) for p in path)
                print(f"{i+1} → {i+1}  {self._dist[i][j]:4d}       {pathstr}")

def floyd_warshall(n, edge):
    Graph(n, edge).newShortestPaths().printShortestPaths()

if __name__ == '__main__':
    floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])