# Bellman-Ford Algorithm: Finds the minimum spanning tree weights from a start node in a graph.
# Bellman-Ford uses the same technique for "relaxing" weights as Dijkstra's algorithm, except Bellman-Ford works with negative edges where Dijsktra's does not.
# Bellman-Ford is a generalized version of Dijkstra's but is slower than Dijsktra's for postive-only weights.
# The difference between Bellman-Ford and Dijkstra is that Bellman-Ford loops through all the vertices until all have been met, whereas Dijsktra loops until the queue is empty.
# Worst-case performance: O(|V| * |E|) where V is a list of vertices and E is a list of edges.
# Best-case performance: O(|E|)
# Worst-case space complexity: O(|V|)

class Queue():
    def __init__(self):
        self.arr = []
    def look(self):
        if len(self.arr) > 0:
            return self.arr[0]
        else:
            return None
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        val = self.look()
        self.arr.remove(val)
        return val

class Graph():
    def __init__(self, directed):
        self.vertices = []
        self.weights = {}
        self.adjList = {}
        self.directed = directed
    def addNode(self, root, node, weight = 1):
        # Add the node to the list of vertices
        if node not in self.vertices:
            self.vertices.append(node)
        if self.directed:
            if (root, node) not in self.weights:
                self.weights[(root, node)] = weight
        else:
            if (root, node) not in self.weights:
                self.weights[(root, node)] = weight
                self.weights[(node, root)] = weight

        # If the node doesn't already have adjacencies, create an empty list
        try:
            _ = self.adjList[node]
        except KeyError:
            self.adjList[node] = []

        # Add the nodes
        if self.directed:
            if root is not None:
                self.adjList[root].append(node)
        else:
            if root is not None:
                self.adjList[root].append(node)
                self.adjList[node].append(root)
    # Bellman Ford Algorithm
    def BF(self, start):
        prev = []
        dist = []
        queue = Queue()
        V = len(self.vertices)
        for i in range(V):
            if self.vertices[i] == start:
                dist.append(0)
                prev.append(start)
            else:
                prev.append(-1)
                dist.append(1e5)   # inf
        queue.push(start)
        queue.push(V)
        i = 0
        while len(queue.arr) != 1 and i < V:
            root = queue.pop()
            if root == V:
                i = i + 1
                queue.push(V)
            else:
                r = self.vertices.index(root)
                adj = self.adjList[root]
                for node in adj:
                    n = self.vertices.index(node)
                    sum = dist[r] + self.weights[(root, node)]
                    if dist[n] > sum:
                        dist[n] = sum
                        prev[n] = node
                        if node not in queue.arr:
                            queue.push(node)
        return (prev, dist)

if __name__ == '__main__':
    # Initialize the Graph
    directed = True
    graph = Graph(directed)
    vertices = [('A', 0), ('B', 1), ('C', 2), ('D', 3),
                ('E', 4)]
    for v in vertices:
        graph.addNode(None, v)
    # Create connections
    graph.addNode(vertices[0], vertices[1], 1)
    graph.addNode(vertices[4], vertices[0], 5)
    graph.addNode(vertices[3], vertices[1], -6)
    graph.addNode(vertices[3], vertices[4], 4)
    graph.addNode(vertices[1], vertices[2], 2)
    graph.addNode(vertices[2], vertices[3], 3)

    # Print the graph
    print("-"*50)
    print("Graph Vertices: " + str(graph.vertices))
    print("Graph Adjacencies:")
    for k in graph.adjList:
        adj = graph.adjList[k]
        list = []
        for n in adj:
            a = n[0][0]
            list.append((a, graph.weights[(k, n)]))
        print(str(k[0]) + ": " + str(list))
    print("-"*50)

    # Bellman Ford
    nodes, dist = graph.BF(vertices[0])
    # Construct minimum spanning tree from the nodes and distances of Bellman-Ford
    tree = Graph(directed)
    for i in range(len(nodes)):
        node = (nodes[i][0], dist[i])
        tree.addNode(None, node)
    for i in range(len(tree.vertices)):
        tree_root = tree.vertices[i]
        graph_root = graph.vertices[i]
        adj = graph.adjList[graph.vertices[i]]
        for graph_node in adj:
            j = graph.vertices.index(graph_node)
            tree_node = tree.vertices[j]
            if (dist[i] + graph.weights[(graph_root, graph_node)]) == dist[j]:
                tree.addNode(tree_root, tree_node, tree_node[1])
    print("Tree Vertices: " + str(tree.vertices))
    print("Tree Adjacencies:")
    for k in tree.adjList:
        adj = tree.adjList[k]
        list = []
        for n in adj:
            list.append(n)
        print(str(k[0]) + ": " + str(list))
    print("-"*50)
