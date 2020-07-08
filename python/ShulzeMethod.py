import numpy as np
from prettytable import PrettyTable

# Shulze's Method: In an election with preferential ballots, find the winner of the election.
# Winners are determined by a Condorcet criterion: the winner, when compared to every other candidate, is preferable.
# Example: D is the Condorcet winner if D is preferred more than other candidates (D > A, D > B, D > C)
# Method:
# 1. Find all of the pairwise preferences and construct a graph out of it.
# 2. Find the strongest path in the graph for each pairwise preference using Floyd-Warshall Algorithm.
# 2 cont. Strongest path = widest path; the path that maximizes its minimum weight.
# 3. For each strongest path, find the value of its minimum weight and record it in a table.
# 4. Compare each minimum weight in pairs and find the pairwise winners. Construct inequalities out of these winners.
# 5. The winner of the election is the one at the top of the inequality.

# Priority Queue with nodes
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
    def widestPath(self, start):
        prev = []
        width_to = {}
        queue = Queue()
        for i in range(len(self.vertices)):
            if self.vertices[i] == start:
                width_to[self.vertices[i]] = np.inf
                prev.append(start)
            else:
                width_to[self.vertices[i]] = -np.inf
                prev.append(-1)
            queue.push(self.vertices[i])
        while len(queue.arr) != 0:
            root = queue.pop()
            r = self.vertices.index(root)
            adj = self.adjList[root]
            for node in adj:
                n = self.vertices.index(node)
                alt = max(width_to[node], min(width_to[root], self.weights[(root, node)]))
                if alt > width_to[node]:
                    width_to[node] = alt
                    prev[n] = node
                    if node not in queue.arr:
                        queue.push(node)
        return width_to

def pairs(list):
    p = []
    for a in list:
        i = list.index(a)
        for b in list[i:]:
            if ((a, b) not in p) and ((b, a) not in p):
                p.append((a, b))
    return p

def pairwisePreferences(ballots):
    num_ballots = len(ballots)
    candidates = []
    for c in ballots[0]:
        candidates.append(c)
    candidates = sorted(candidates)
    num_candidates = len(candidates)
    prefs = np.zeros([num_candidates, num_candidates])
    for b in ballots:
        pairs_list = pairs(b)
        for p in pairs_list:
            a, b = p
            if a != b:
                i = candidates.index(a)
                j = candidates.index(b)
                prefs[i][j] = prefs[i][j] + 1
    return prefs, candidates

def createGraph(ballots):
    prefs, candidates = pairwisePreferences(ballots)
    num_candidates = len(candidates)
    for i in range(num_candidates):
        for j in range(num_candidates):
            if (prefs[i][j] > prefs[j][i]):
                prefs[i][j] = prefs[i][j] - prefs[j][i]
                prefs[j][i] = -np.inf
            elif i == j:
                prefs[i][j] = -np.inf
    graph = Graph(True)
    for i in range(num_candidates):
        for j in range(num_candidates):
            if prefs[i][j] != -np.inf:
                i_node = (candidates[i], 0)
                j_node = (candidates[j], 0)
                graph.addNode(None, i_node)
                graph.addNode(None, j_node)
                graph.addNode(i_node, j_node, prefs[i][j])
    return graph, candidates

def ShulzeMethod(ballots):
    graph, candidates = createGraph(ballots)
    S = []
    num_candidates = len(candidates)
    for root in graph.vertices:
        list = []
        widest_path = graph.widestPath(root)
        for node in graph.vertices:
            x = widest_path[node]
            if x == np.inf:
                x = -np.inf
            list.append(x)
        S.append(list)
    wins = []
    for i in range(num_candidates):
        list = []
        for j in range(num_candidates):
            if i != j:
                if S[i][j] > S[j][i]:
                    list.append(j)
        wins.append(list)
    best_cand = 0
    best_cand_wins = 0
    for i in range(len(wins)):
        cand_wins = len(wins[i])
        if cand_wins > best_cand_wins:
            best_cand = i
            best_cand_wins = cand_wins
    return candidates[best_cand]

if __name__ == '__main__':
    pref_table = PrettyTable()
    ballots = [['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C'],
               ['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C'],
               ['B', 'C', 'A'], ['B', 'C', 'A'], ['B', 'C', 'A'], ['B', 'C', 'A'], ['B', 'C', 'A'],
               ['C', 'A', 'B'], ['C', 'A', 'B'], ['C', 'A', 'B'], ['C', 'A', 'B'], ['C', 'A', 'B']]
    prefs, candidates = pairwisePreferences(ballots)

    pref_table.field_names = ["Preference Table"] + candidates
    i = 0
    for c in candidates:
        pref_table.add_row([c] + prefs[i].tolist())
        i += 1
    print(pref_table)
    winner = ShulzeMethod(ballots)
    print("The winner of the election is candidate " + winner)
