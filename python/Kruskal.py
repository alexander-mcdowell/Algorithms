import math
import numpy as np
import matplotlib.pyplot as plt

# Kruskal's Algorithm: Efficient greedy algorithm that finds the minimum spanning tree in a graph using edges.
# Note: A tree cannot contain a cycle otherwise it would violate its definition.
# Worst-case performance: O(|E| log |E|) where E is the list of edges.
# Method:
    # 1. Repeat until all nodes are connected:
        # 1a. Get the minimum-weight edge in the graph that has not already been checked.
        # 1b. If adding this edge to the current minimum spanning tree would not create a cycle, add the edge to the tree.

def euclidean(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Contains cycle searches the graph keeping track of the edges and vertices already visited.
# If a node already visited is met along a new edge, the graph contains a cycle.
# This cycle-detection method is not the most efficient, but it makes conceptual sense.
def containsCycle(edges):
    adjList = {}
    for e in edges:
        if e[0] not in adjList: adjList[e[0]] = []
        if e[1] not in adjList: adjList[e[1]] = []
        adjList[e[0]].append(e[1])
        adjList[e[1]].append(e[0])
    edges_visited = []
    vertices_visited = []
    for u in set(adjList):
        if u not in vertices_visited:
            stack = [u]
            while len(stack) != 0:
                x = stack.pop(0)
                if x in vertices_visited:
                    return True
                vertices_visited.append(x)
                for v in adjList[x]:
                    e = sorted((x, v))
                    if e not in edges_visited:
                        stack += [v]
                        edges_visited.append(e)
    return False

def Kruskal(adjacency_matrix):
    n = len(adjacency_matrix)
    connections = np.zeros((n, n))
    edges = {}
    visited = []
    for i in range(n):
        for j in range(i + 1, n):
            edges[adjacency_matrix[i][j]] = (i, j)
    edges = {k:edges[k] for k in sorted(edges)}
    tree_edges = []
    stop = False
    while not stop:
        # Search for the minimum weight edge that does not create a cycle.
        while True:
            if len(edges) == 0:
                stop = True
                break
            x = min(edges)
            e = edges[x]
            del edges[x]
            if not containsCycle(tree_edges + [e]): break
        if not stop:
            tree_edges.append(e)
            connections[e[0]][e[1]] = 1
    return connections

minval, maxval = 0, 10
num_points = 100
xs = np.random.uniform(minval, maxval, (num_points,))
ys = np.random.uniform(minval, maxval, (num_points,))
adjacency_matrix = np.zeros((num_points, num_points))
for i in range(num_points):
    for j in range(num_points):
        adjacency_matrix[i][j] = euclidean((xs[i], ys[i]), (xs[j], ys[j]))
adjacency_matrix = np.where(adjacency_matrix == 0, np.inf, adjacency_matrix)
connections = Kruskal(adjacency_matrix)
plt.scatter(xs, ys, c = 'black')
text_offset = 0.1
for i in range(num_points):
    plt.text(xs[i] + text_offset, ys[i] + text_offset, str(i))
    for j in range(num_points):
        if connections[i][j] == 1:
            linex = [xs[i] + (xs[j] - xs[i]) * t for t in np.linspace(0, 1, 100)]
            liney = [ys[i] + (ys[j] - ys[i]) * t for t in np.linspace(0, 1, 100)]
            plt.plot(linex, liney, "r-")
plt.title("Kruskal's Algorithm")
plt.show()
