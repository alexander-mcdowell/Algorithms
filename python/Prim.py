import math
import numpy as np
import matplotlib.pyplot as plt

# Prim's algorithms: Efficient algorithm that finds the minimum spanning tree in a graph using greedy methods by looking at vertices.
# Minimum spanning tree: A tree within a graph that has the minimum total weight sum and reaches every node.
# Worst-case performance:
    # For an adjacency matrix implementation: O(|V|^2) V are the vertices.
    # For a binary heap implementation: O(|E| log |V|) where E are the edges
# Method:
    # 1. Assign each vertex in the graph a "cost" equivalent to the minimum weight to that node (such that two nodes don't point to eachother)
    # 2. Repeat until all nodes have been visited:
        # 2a. Choose the node with the least cost. Add this node to the list of visited nodes.
        # 2b. Update the cost values for all of that node's neighbors.

def euclidean(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def Prim(adjacency_matrix, start = 0):
    n = len(adjacency_matrix)
    visited = []
    costs = [np.inf] * n
    costs[start] = 0
    connections = np.zeros((n, n))
    edges_added = []
    while len(visited) < n:
        # Choose the node with the least cost and add it to the list of visited nodes
        u = 0
        best_cost = np.inf
        for i in range(n):
            if costs[i] <= best_cost and i not in visited:
                best_cost = costs[i]
                u = i
        visited.append(u)
        # Update the cost values of neighboring nodes
        for i in range(n):
            if u != i:
                edge = sorted((u, i))
                x = adjacency_matrix[u][i]
                if x < costs[i] and edge not in edges_added:    # Make sure that two nodes don't make a connection to eachother
                    costs[i] = x
                    edges_added.append(edge)
    # Create the actual minimum spanning tree from the costs.
    for u in range(n):
        for v in range(n):
            if adjacency_matrix[u][v] == costs[v]:
                connections[u][v] = 1
    return connections, costs

minval, maxval = 0, 10
num_points = 30
xs = np.random.uniform(minval, maxval, (num_points,))
ys = np.random.uniform(minval, maxval, (num_points,))
adjacency_matrix = np.zeros((num_points, num_points))
for i in range(num_points):
    for j in range(num_points):
        adjacency_matrix[i][j] = euclidean((xs[i], ys[i]), (xs[j], ys[j]))
adjacency_matrix = np.where(adjacency_matrix == 0, np.inf, adjacency_matrix)
connections, costs = Prim(adjacency_matrix)
print(costs)
plt.scatter(xs, ys, c = 'black')
text_offset = 0.1
for i in range(num_points):
    plt.text(xs[i] + text_offset, ys[i] + text_offset, str(i))
    for j in range(num_points):
        if connections[i][j] == 1:
            linex = [xs[i] + (xs[j] - xs[i]) * t for t in np.linspace(0, 1, 100)]
            liney = [ys[i] + (ys[j] - ys[i]) * t for t in np.linspace(0, 1, 100)]
            plt.plot(linex, liney, "r-")
plt.title("Prim's Algorithm")
plt.show()
