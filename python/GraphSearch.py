# This program contains five graph-searching algorithms: Depth-First search, Breadth-First search, Topological search, Greedy Search, and Dijkstra's algorithm

# Depth-First search: Starting from a root node, recursively explore each node's children until all nodes have been searched.
# Worst-case performance: O(|V| + |E|) for vertices V and edges E.
# Worst-case space complexity: O(|V|)
# Method:
# 1. Start at the root node and add it to the list of visited nodes.
# 2. Look at each of the children, if they exist individually. Call depth-first search on each child if they have not been visited yet.

# Breadth-First search: Starting from a root node, add all children to the list of visited nodes and then recurse through each child individually.
# Worst-case performance: O(|V| + |E|) for vertices V and edges E.
# Worst-case space complexity: O(|V|)
# Method:
# 1. Add the root node to the priority queue.
# 2. Pop the priority queue. Add the popped element to the list of visited notes. Add all of the popped node's children to a priority queue
# 3. Repeat 2 until all nodes have been visited.

# Topological search: Works well for directed graphs; starting from a root node, depth-first search until no longer possible, then move onto the next node unvisited and repeat.
# Method:
# 1. Get a list of all the nodes.
# 2. Depth-first search the first node in the list and remove nodes visited from the list.
# 3. Repeat 2. until all nodes have been visited.

# Greedy search: Finds the shortest path between two nodes by choosing the minimum path option each time.
# Method:
# 1. Let the root node be the start node.
# 2. Go to the child that has not been visited yet which has the minimum weight along its path. Stop the algorithm if the child is the end node.
# 3. Repeat 2.

# Dijkstra's Algorithm: Effective algorithm for finding the shortest path between two nodes in a graph or for constructing a minimum spanning tree.
# Worst-case performance: O(|E| + |V| log |V|) for vertices V and edges E.
# Method:
# 1. Create a list dist which represents the sum of the weights along the shortest path to each node.
# 1 cont. For example, if the shortest path from A to D had a total weight of 17, then dist[D] = 17
# 1 cont. Dist = inf for all values except for the root, where dist[root] = 0.
# 2. Create a minimum priority queue that stores each node with their dist value. Add every node with their dist value to the priority queue.
# 3. Loop the following until the priority queue is empty:
    # 3a. Get the node with the minimum dist value from the queue.
    # 3b. Loop through all of the children of this node. Let x = dist[node] + weight[node, child].
    # 3c. If x < dist[child], dist[child] = x. Replace dist[child] in the priority queue with its new value.

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

# Priority Queue with nodes
class MinPriorityQueue():
    def __init__(self):
        self.nodes = []
        self.dists = []
    def look(self):
        if len(self.nodes) > 0:
            d = min(self.dists)
            n = self.nodes[self.dists.index(d)]
            return (n, d)
        else:
            return None
    def push(self, val):
        self.nodes.append(val[0])
        self.dists.append(val[1])
    def pop(self):
        val = self.look()
        self.nodes.remove(val[0])
        self.dists.remove(val[1])
        return val
    def replace(self, targ, val):
        i = self.nodes.index(targ)
        self.dists[i] = val

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
    # Depth-First Search
    def DFS(self, start, visited = []):
        visited.append(start)
        for n in self.adjList[start]:
            if n not in visited:
                self.DFS(n, visited)
        return visited
    # Breadth-First Search
    def BFS(self, start):
        queue = Queue()
        queue.push(start)
        visited = []
        while len(queue.arr) != 0:
            x = queue.pop()
            for n in self.adjList[x]:
                if n not in visited:
                    visited.append(n)
                    queue.push(n)
        return visited
    # Topological Search
    def TS(self):
        left_over = self.vertices.copy()
        path = []
        while len(left_over) != 0:
            x = self.DFS(left_over[0])
            for n in x:
                if n not in path:
                    path.append(n)
                if n in left_over:
                    left_over.remove(n)
        return path
    # Greedy Search
    def GS(self, start, end, visited = [], total_weight = 0):
        if start not in visited:
            visited.append(start)
        nodes = []
        w = []
        v = []
        node_index = 0
        for n in self.adjList[start]:
            if n not in visited:
                if n != end:
                    nodes.append(n)
                    w.append(self.weights[(start, n)])
                    v.append(node_index)
                else:
                    visited.append(end)
                    total_weight += self.weights[(start, end)]
                    return total_weight, visited
            node_index += 1
        min_weight = min(w)
        total_weight += min_weight
        next = self.adjList[start][v[w.index(min_weight)]]
        total_weight, path = self.GS(next, end, visited, total_weight)
        return total_weight, path
    # Dijkstra's Algorithm
    def DA(self, start, end):
        prev = []
        dist = []
        pq = MinPriorityQueue()
        for i in range(len(self.vertices)):
            if self.vertices[i] == start:
                dist.append(0)
                prev.append(start)
            else:
                prev.append(-1)
                dist.append(1e5)   # inf
            pq.push((self.vertices[i], dist[i]))
        while len(pq.dists) != 0:
            root, rdist = pq.pop()
            r = self.vertices.index(root)
            adj = self.adjList[root]
            for node in adj:
                n = self.vertices.index(node)
                sum = dist[r] + self.weights[(root, node)]
                if dist[n] > sum:
                    dist[n] = sum
                    prev[n] = node
                    pq.replace(node, dist[n])
        return (prev, dist)

if __name__ == '__main__':
    # Initialize the Graph
    directed = False
    graph = Graph(directed)
    vertices = [('A', 0), ('B', 1), ('C', 2), ('D', 3),
                ('E', 4), ('F', 5), ('G', 6), ('H', 7),
                ('I', 8)]
    for v in vertices:
        graph.addNode(None, v)
    # Create connections
    graph.addNode(None, vertices[0])
    graph.addNode(vertices[0], vertices[1], 4)
    graph.addNode(vertices[0], vertices[7], 8)
    graph.addNode(vertices[1], vertices[7], 11)
    graph.addNode(vertices[1], vertices[2], 8)
    graph.addNode(vertices[7], vertices[8], 7)
    graph.addNode(vertices[7], vertices[6], 1)
    graph.addNode(vertices[2], vertices[8], 2)
    graph.addNode(vertices[2], vertices[3], 7)
    graph.addNode(vertices[2], vertices[5], 4)
    graph.addNode(vertices[3], vertices[5], 14)
    graph.addNode(vertices[3], vertices[4], 9)
    graph.addNode(vertices[4], vertices[5], 10)
    graph.addNode(vertices[5], vertices[6], 2)
    graph.addNode(vertices[6], vertices[8], 6)

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

    # Start and Target nodes for search methods
    start = vertices[0]
    end = vertices[-1]

    # Search methods
    print("Depth-First Search from " + str(start) + ": " + str(graph.DFS(start)))
    print("Breadth-First Search from " + str(start) + ": " + str(graph.BFS(start)))
    print("Topological Search: " + str(graph.TS()))
    print("Greedy Search from " + str(start) + " to " + str(end) + ": " + str(graph.GS(start, end)))
    print("-"*50)

    nodes, dist = graph.DA(start, end)
    # Construct minimum spanning tree
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
    start = tree.vertices[0]
    end = tree.vertices[-1]
    print("Shortest path from " + str(start) + " to " + str(end) + ": " + str(tree.GS(start, end, visited = [])[1]))
    print("The above path has a distance of " + str(end[1]))
    print("-"*50)
