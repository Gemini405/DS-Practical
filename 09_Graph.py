from collections import defaultdict

def addEdge(graph, u, v):
    graph[u].append(v)

def generateEdges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges

graph = defaultdict(list)

addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'c')
addEdge(graph, 'b', 'd')
addEdge(graph, 'a', 'd')
addEdge(graph, 'a', 'b')

print(generateEdges(graph))
