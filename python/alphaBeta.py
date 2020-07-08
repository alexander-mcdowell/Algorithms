import numpy as np

# Alpha-Beta algorithm: for a two-player game, decide which moves will generate the greatest reward for you and the least reward for the opponent.
# Worst-case performance: O(b^d) where b is the branching factor and d is the depth.
# Best-case performance: O(sqrt(b ^ d))
# Method:
    # 1. Let you be the MAX player and the opponent be the MIN player.
    # 1 cont. The MAX player will always seek to maximize their score, whereas the MIN player will seek to minimize their score.
    # 2. Create a decision tree for the possible moves a player can take.
    # 2 cont. All nodes in-between the root and the bottommost leaves are assigned a value of infinity for the MAX player and -infinity for the MIN player.
    # 3. The bottommost leaves are assigned a value equal to the reward for who wins.
    # Example: For tic-tac-toe, if MIN wins in a state, the reward is -1. If MAX wins in a state, the reward is 0. If it is a tie, the reward is 0.
    # 4. Recursively compare children in the tree, alternating between MAX and MIN players.
    # 4 cont. The value of a MAX node is max(children values). The value of a MIN node is min(children values)
    # 4 cont. Let alpha be the highest-value choice along the path for MAX and beta be the lowest-valued choice along the path for MIN.
    # 4 cont. If alpha is at least beta, it is no longer worthwhile exploring that segment of the tree because the MIN node would never choose a node with more value (alpha) than a lesser alternative (beta)
    # 5. The algorithm ends when the root node is given a value informing it of the path to take along the tree.

class Node():
    def __init__(self, label, value, left = None, right = None, up = None):
        self.label = label
        self.value = value
        self.up = up
        self.left = left
        self.right = right

class Tree():
    def __init__(self, root):
        self.root = root
        self.nodes = [root]
    def getNode(self, label):
        for n in self.nodes:
            if n.label == label: return n
    def addNode(self, node, direction):
        if node in self.nodes:
            print("Node provided is already in the tree")
        if node.up:
            if direction == "left":
                node.up.left = node
                self.nodes.append(node)
            elif direction == "right":
                node.up.right = node
                self.nodes.append(node)
            else:
                print(str(direction) + " is not a valid placement")

def alphaBeta(node, isMaximizingPlayer = True, alpha = -np.inf, beta = np.inf):
    if node.left == None and node.right == None: return node.value
    if isMaximizingPlayer:
        best_v = -np.inf
        for child in [node.left, node.right]:
            v = alphaBeta(child, False, alpha, beta)
            best_v = max(v, best_v)
            alpha = max(alpha, best_v)
            print("At node " + child.label + ", best_v = " + str(best_v) + ", alpha = " + str(alpha) + ", beta = " + str(beta))
            if beta <= alpha:
                print("Pruning node " + child.label)
                break
        print("Is max at node " + node.label + ". Choosing value: " + str(best_v))
        return best_v
    else:
        best_v = np.inf
        for child in [node.left, node.right]:
            v = alphaBeta(child, True, alpha, beta)
            best_v = min(v, best_v)
            beta = min(beta, best_v)
            print("At node " + child.label + ", best_v = " + str(best_v) + ", alpha = " + str(alpha) + ", beta = " + str(beta))
            if beta <= alpha:
                print("Pruning node " + child.label)
                break
        print("Is min at node " + node.label + ". Choosing value: " + str(best_v))
        return best_v

tree = Tree(Node("A", -np.inf))
tree.addNode(Node("B", -np.inf, up = tree.root), direction = "left")
tree.addNode(Node("C", -np.inf, up = tree.root), direction = "right")
tree.addNode(Node("D", -np.inf, up = tree.getNode("B")), direction = "left")
tree.addNode(Node("E", -np.inf, up = tree.getNode("B")), direction = "right")
tree.addNode(Node("F", -np.inf, up = tree.getNode("C")), direction = "left")
tree.addNode(Node("G", -np.inf, up = tree.getNode("C")), direction = "right")
tree.addNode(Node("H", 3, up = tree.getNode("D")), direction = "left")
tree.addNode(Node("I", 5, up = tree.getNode("D")), direction = "right")
tree.addNode(Node("J", 6, up = tree.getNode("E")), direction = "left")
tree.addNode(Node("K", 9, up = tree.getNode("E")), direction = "right")
tree.addNode(Node("L", 1, up = tree.getNode("F")), direction = "left")
tree.addNode(Node("M", 2, up = tree.getNode("F")), direction = "right")
tree.addNode(Node("N", 0, up = tree.getNode("G")), direction = "left")
tree.addNode(Node("O", -1, up = tree.getNode("G")), direction = "right")
print("The optimal reward is " + str(alphaBeta(tree.root)))
