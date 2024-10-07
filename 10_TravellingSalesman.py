from sys import maxsize
from itertools import permutations

V = 4

def travelling_salesman(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_perm = permutations(vertex)
    
    for i in next_perm:
        curr_path = 0
        k = s
        
        for j in i:
            curr_path += graph[k][j]
            k = j
        curr_path += graph[k][s]

        min_path = min(min_path, curr_path)

    return min_path


if __name__ == "__main__":
    Graph = [[0, 10, 15, 25], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0

    res = travelling_salesman(Graph, s)
    print(res)
