from termcolor import colored
import os
import math

# A* Algorithm: pathfinding algorithm that takes the shortest path from A to B in an open world environment.
# Worst-case performance: O(|E|) = O(b^d) where E is a list of edges, b is the branching factor, and d is the depth.
# Worst-case space requirement: O(|V|) = O(b^d) where V is a list of vertices.
# A* uses a lot of space because it stores all of the vertices. If space is an issue, one should use a different algorithm like IDA*
# Method: Simply just Dijkstra's Algorithm with an added heuristic function.
# Notable Heuristics:
    # Manhattan Heuristic: useful for grid worlds; abs(start - end)
    # Eudlidean Heuristic: useful for moving in any direction; "straight line distance" between the start and end.

# Coloring the grid world
os.system('color')
player = colored('@', "green")
wall = colored('#', "red")
goal = colored('G', "blue")
none = '0'
def path(step_num):
    if math.floor(step_num / 10) >= 1:
        step_num = step_num % 10
    return colored(str(step_num), "yellow")

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
class GridWorld():
    def __init__(self, size):
        self.arr = []
        self.graph = Graph(False)
        self.size = size
        self.playerLoc = ()
        self.goalLoc = ()
        self.step_num = 0
        for i in range(size):
            self.arr.append(list(none*size))

        for y in range(size):
            for x in range(size):
                root = (None, 10 * y + x)
                self.graph.addNode(None, root)
        for y in range(size):
            for x in range(size):
                root = (None, 10 * y + x)
                leftNode = (None, 10 * y + x - 1)
                rightNode = (None, 10 * y + x + 1)
                upNode = (None, 10 * y + x - 10)
                downNode = (None, 10 * y + x + 10)

                if (0 < (x - 1)) and ((x - 1) < self.size):
                    self.graph.addNode(root, leftNode)
                if (0 < (x + 1)) and ((x + 1) < self.size):
                    self.graph.addNode(root, rightNode)
                if (0 < (y - 1)) and ((y - 1) < self.size):
                    self.graph.addNode(root, upNode)
                if (0 < (y + 1)) and ((y + 1) < self.size):
                    self.graph.addNode(root, downNode)
    def printWorld(self):
        print("-"*50)
        for i in range(self.size):
            str = ""
            for j in range(self.size):
                str += self.arr[i][j]
            print(str)
    def addPlayer(self, loc):
        x, y = loc
        if (x >= 0 and x < self.size):
            if (y >= 0 and y < self.size):
                self.arr[y][x] = player
                self.playerLoc = (x, y)
    def addGoal(self, loc):
        x, y = loc
        if (x >= 0 and x < self.size):
            if (y >= 0 and y < self.size):
                self.arr[y][x] = goal
                self.goalLoc = (x, y)
    def addWall(self, loc):
        x, y = loc
        if (x >= 0 and x < self.size):
            if (y >= 0 and y < self.size):
                self.arr[y][x] = wall
                nodeLoc = 10 * y + x
                node = (None, nodeLoc)
                for n in self.graph.adjList[node]:
                    self.graph.weights[(node, n)] = 1e5
                    if not self.graph.directed:
                        self.graph.weights[(n, node)] = 1e5
    def movePlayer(self, dir):
        x, y = self.playerLoc
        if dir == "up":
            if ((y - 1) < self.size) and (0 <= (y - 1)) and (self.arr[y - 1][x] != wall):
                self.arr[y][x] = path(self.step_num)
                self.arr[y - 1][x] = player
                self.playerLoc = (x, y - 1)
                self.step_num += 1
        elif dir == "left":
            if ((x - 1) < self.size) and (0 <= (x - 1)) and (self.arr[y][x - 1] != wall):
                self.arr[y][x] = path(self.step_num)
                self.arr[y][x - 1] = player
                self.playerLoc = (x - 1, y)
                self.step_num += 1
        elif dir == "right":
            if ((x + 1) < self.size) and (0 <= (x + 1)) and (self.arr[y][x + 1] != wall):
                self.arr[y][x] = path(self.step_num)
                self.arr[y][x + 1] = player
                self.playerLoc = (x + 1, y)
                self.step_num += 1
        elif dir == "down":
            if ((y + 1) < self.size) and (0 <= (y + 1)) and (self.arr[y + 1][x] != wall):
                self.arr[y][x] = path(self.step_num)
                self.arr[y + 1][x] = player
                self.playerLoc = (x, y + 1)
                self.step_num += 1

# Manhattan heuristic
def Manhattan(current, end):
    return math.fabs(current[0] - end[0]) + math.fabs(current[1] - end[1])

# A star pathfinding
def AStar(gridworld, start, end):
    prev = []
    dist = []
    graph = gridworld.graph
    queue = Queue()
    V = len(graph.vertices)
    start = (None, 10 * start[1] + start[0])
    for i in range(V):
        if graph.vertices[i] == start:
            dist.append(0)
            prev.append(start)
        else:
            prev.append(-1)
            dist.append(1e5)   # inf
    queue.push(start)
    queue.push(V)
    i = 0
    while len(queue.arr) != 1 and i  < V:
        root = queue.pop()
        if root == V:
            i = i + 1
            queue.push(V)
        else:
            r = graph.vertices.index(root)
            adj = graph.adjList[root]
            for node in adj:
                if node not in prev:
                    n = graph.vertices.index(node)
                    x = node[1] % 10
                    y = math.floor(node[1] / 10)
                    sum = dist[r] + graph.weights[(root, node)] + Manhattan((x, y), end)
                    if dist[n] > sum:
                        dist[n] = sum
                        prev[n] = node
                        if node not in queue.arr:
                            queue.push(node)
    prev = [x for x in prev if x != -1]
    dist = [x for x in dist if x != 1e5]
    tree = Graph(True)
    for node in prev:
        tree.addNode(None, node)
    for node in prev:
        tree_root = node
        i = tree.vertices.index(node)
        adj = graph.adjList[node]
        for graph_node in adj:
            if graph_node in tree.vertices:
                j = tree.vertices.index(graph_node)
                x = graph_node[1] % 10
                y = math.floor(graph_node[1] / 10)
                sum = dist[i] + graph.weights[(tree_root, graph_node)] + Manhattan((x, y), end)
                if sum == dist[j]:
                    tree.addNode(tree_root, graph_node, sum)
    end = (None, 10 * end[1] + end[0])
    path = tree.GS(start, end)[1]
    return path

if __name__ == '__main__':
    gridworld = GridWorld(7)
    gridworld.addPlayer((0, 0))
    gridworld.addGoal((4, 0))

    gridworld.addWall((0, 1))
    gridworld.addWall((1, 1))
    gridworld.addWall((3, 0))
    gridworld.addWall((3, 1))
    gridworld.addWall((3, 2))
    gridworld.addWall((3, 3))
    gridworld.addWall((2, 3))
    gridworld.addWall((1, 3))
    gridworld.addWall((4, 1))
    gridworld.addWall((4, 2))
    gridworld.addWall((5, 2))
    gridworld.addWall((0, 5))
    gridworld.addWall((1, 5))
    gridworld.addWall((4, 3))
    gridworld.addWall((4, 5))
    gridworld.addWall((4, 4))

    gridworld.printWorld()

    short_path = AStar(gridworld, gridworld.playerLoc, gridworld.goalLoc)
    for n in short_path[1:]:
        coord = n[1]
        x = coord % 10
        y = math.floor(coord / 10)
        diffx = (x - gridworld.playerLoc[0])
        diffy = (y - gridworld.playerLoc[1])
        if diffx == -1:
            m = "left"
        elif diffx == 1:
            m = "right"
        elif diffy == -1:
            m = "up"
        elif diffy == 1:
            m = "down"
        gridworld.movePlayer(m)
    gridworld.printWorld()
