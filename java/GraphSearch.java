import java.util.ArrayList;

/*
This program contains three graph-searching algorithms: Depth-First search, Breadth-First search, and Dijkstra's algorithm

Depth-First search: Starting from a root node, recursively explore each node's children until all nodes have been searched.
Worst-case performance: O(|V| + |E|) for vertices V and edges E.
Worst-case space complexity: O(|V|)
Method:
    1. Start at the root node and add it to the list of visited nodes.
    2. Look at each of the children, if they exist individually. Call depth-first search on each child if they have not been visited yet.

Breadth-First search: Starting from a root node, add all children to the list of visited nodes and then recurse through each child individually.
Worst-case performance: O(|V| + |E|) for vertices V and edges E.
Worst-case space complexity: O(|V|)
Method:
    1. Add the root node to the priority queue.
    2. Pop the priority queue. Add the popped element to the list of visited notes. Add all of the popped node's children to a priority queue
    3. Repeat 2 until all nodes have been visited.

Dijkstra's Algorithm: Effective algorithm for finding the shortest path between two nodes in a graph or for constructing a minimum spanning tree.
Worst-case performance: O(|E| + |V| log |V|) for vertices V and edges E.
Method:
    1. Create a list dist which represents the sum of the weights along the shortest path to each node.
    1 cont. For example, if the shortest path from A to D had a total weight of 17, then dist[D] = 17
    1 cont. Dist = inf for all values except for the root, where dist[root] = 0.
    2. Create a minimum priority queue that stores each node with their dist value. Add every node with their dist value to the priority queue.
    3. Loop the following until the priority queue is empty:
        3a. Get the node with the minimum dist value from the queue.
        3b. Loop through all of the children of this node. Let x = dist[node] + weight[node, child].
        3c. If x < dist[child], dist[child] = x. Replace dist[child] in the priority queue with its new value.
*/

class GraphSearch {
    // Returns an integer array of all the indices in the order visited
    public static void depthFirstSearch(Graph g, int rootIndex, ArrayList<Integer> visited) {
        int[] connected = g.getConnected(rootIndex);
        for (int i = 0; i < connected.length; i++) {
            if (!visited.contains(connected[i])) {
                visited.add(connected[i]);
                depthFirstSearch(g, connected[i], visited);
            }
        }
    }

    public static void breadthFirstSearch(Graph g, int rootIndex, ArrayList<Integer> visited) {
        ArrayList<Integer> queue = new ArrayList<Integer>();
        queue.add(rootIndex);
        int popped;
        while (queue.size() != 0) {
            popped = queue.get(0);
            if (!visited.contains(popped)) visited.add(popped);
            queue.remove(0);
            int[] connected = g.getConnected(popped);
            for (int x : connected) {
                if (!visited.contains(x)) queue.add(x);
            }
        }
    }

    // NOTE: This method doesn't always work. TODO: FIX!
    // Finds the shortest path between two nodes in a minimum spanning tree. Returns the path length.
    public static double findSpanningPath(Graph spanning, int rootIndex, int targetIndex, ArrayList<Integer> visited) {
        double pathLength = 0.0;
        double minValue = Double.MAX_VALUE;
        int chosen_vertex = 0;
        for (int x : spanning.getConnected(rootIndex)) {
            if (x == targetIndex) {
                visited.add(x);
                return spanning.getWeight(rootIndex, x) + pathLength;
            }
            else {
                double weight = spanning.getWeight(rootIndex, x);
                if (weight < minValue && !visited.contains(x)) {
                    minValue = weight;
                    chosen_vertex = x;
                }
            }
        }
        visited.add(chosen_vertex);
        return minValue + findSpanningPath(spanning, chosen_vertex, targetIndex, visited);
    }

    // Returns a minimum spanning tree
    public static Graph Dijkstra(Graph g, int rootIndex) {
        int n = g.numVerticesDeclared;
        Graph tree = new Graph(n);

        double dist[] = new double[n];
        ArrayList<Integer> queue = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            dist[i] = Double.MAX_VALUE;
            queue.add(i);
        }
        dist[rootIndex] = 0.0;

        int chosen_vertex;
        double min_dist;
        while (queue.size() != 0) {
            chosen_vertex = 0;
            min_dist = Double.MAX_VALUE;
            
            // Get the next element in the queue with minimum value
            for (int x : queue) {
                if (dist[x] < min_dist) {
                    chosen_vertex = x;
                    min_dist = dist[x];
                }
            }
            // Remove the element from the queue
            queue.remove(queue.indexOf(chosen_vertex));

            // Replace the distances to each neighboring vertex with the shortest path to that vertex
            for (int u : g.getConnected(chosen_vertex)) {
                if (dist[chosen_vertex] + g.getWeight(chosen_vertex, u) < dist[u]) {
                    dist[u] = dist[chosen_vertex] + g.getWeight(chosen_vertex, u);
                }
            }
        }

        // Create a new graph representing the minimum spanning tree of the original graph.
        for (int i = 0; i < n; i++) tree.createVertex(g.getName(i), i);
        for (int i = 0; i < n; i++) {
            for (int j : g.getConnected(i)) {
                double weight = g.getWeight(i, j);
                if (dist[i] + weight == dist[j]) tree.connect(i, j, weight);
            }
        }

        return tree;
    }

    public static void main(String[] args) {
        Graph graph = new Graph(10);
        String[] vertices = {"A", "B", "C", "D", "E", "F", "G", "H", "I"};
        
        // Create vertices
        for (int i = 0; i < vertices.length; i++) graph.createVertex(vertices[i], i);
        
        // Connect vertices
        graph.connect(0, 1, 4);
        graph.connect(0, 7, 8);
        graph.connect(1, 2, 8);
        graph.connect(1, 7, 11);
        graph.connect(7, 8, 7);
        graph.connect(7, 6, 1);
        graph.connect(2, 8, 2);
        graph.connect(2, 3, 7);
        graph.connect(2, 5, 4);
        graph.connect(3, 5, 14);
        graph.connect(3, 4, 9);
        graph.connect(4, 5, 10);
        graph.connect(5, 6, 2);
        graph.connect(6, 8, 6);

        // Show the graph
        graph.print();

        // Display depth-first search
        int root = 0;
        ArrayList<Integer> path = new ArrayList<Integer>();
        path.add(root);
        depthFirstSearch(graph, root, path);
        System.out.print("Depth-first search: ");
        for (int i : path) System.out.print(vertices[i] + ", ");
        System.out.println();

        // Display breadth-first search
        path.clear();
        path.add(root);
        breadthFirstSearch(graph, root, path);
        System.out.print("Breadth-first search: ");
        for (int i : path) System.out.print(vertices[i] + ", ");
        System.out.println();

        // Use Dijsktra's algorithm to get a minimum spanning tree and then print the tree.
        Graph tree = Dijkstra(graph, 0);
        tree.print();

        // Display shortest route
        int target = 4;
        path.clear();
        path.add(root);
        double pathLength = findSpanningPath(tree, root, target, path);
        System.out.print("Shortest path from " + vertices[root] + " to " + vertices[target] + ": ");
        for (int i : path) System.out.print(vertices[i] + ", ");
        System.out.println();
        System.out.println("Shortest path has a length of " + pathLength + ".");
    }
}