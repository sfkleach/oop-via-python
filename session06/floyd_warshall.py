"""
Taken from http://rosettacode.org/wiki/Floyd-Warshall_algorithm#Python

Suggestions
1.  Ignore the print method entirely and concentrate on the unit tests.
2.  Isolate the production of the table as a separate class, say, ShortestPaths?
3.  Isolate the graph as a separate class that has a method to generate
    the ShortestPaths object.

"""

from math import inf
from itertools import product
 
def floyd_warshall(n, edge):
    rn = range(n)
    dist = [[inf] * n for i in rn]
    nxt  = [[0]   * n for i in rn]
    for i in rn:
        dist[i][i] = 0
    for u, v, w in edge:
        dist[u][v] = w
        nxt[u][v] = v
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j]  = nxt[i][k]
    table = []
    for i, j in product(rn, repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            row = {
                "pair": (i, j),
                "dist": dist[i][j],
                "path": path
            }
            table.append(row)
    return table
    
def print_table(table):
    print("pair     dist    path")
    for row in table:
        print(
            "{0} → {1}  {2:4d}       {3}".format(
                *map( lambda x: x + 1, row['pair'] ), 
                row['dist'], 
                ' → '.join(str(p + 1) for p in row['path'])
            )
        )

def decrement_edges(edges):
    return [[i-1, j-1, d] for (i, j, d) in edges]
 
if __name__ == '__main__':
    print_table(floyd_warshall(4, decrement_edges([[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])))