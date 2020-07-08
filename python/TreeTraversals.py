class Node():
    def __init__(self, value, left = None, right = None, up = None):
        self.value = value
        self.up = up
        self.left = left
        self.right = right

class Tree():
    def __init__(self, root):
        self.root = root
        self.nodes = [root]

    def getNode(self, value):
        for n in self.nodes:
            if n.value == value:
                return n

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

    def removeSubTree(self, node):
        if node in self.nodes:
            self.nodes.remove(node)

            if node.left:
                self.removeSubTree(node.left)
            if node.right:
                self.removeSubTree(node.right)

def preorderTraversal(node):
    if node:
        print(node.value)
        preorderTraversal(node.left)
        preorderTraversal(node.right)

def inorderTraversal(node):
    if node:
        inorderTraversal(node.left)
        print(node.value)
        inorderTraversal(node.right)

def postorderTraversal(node):
    if node:
        postorderTraversal(node.left)
        postorderTraversal(node.right)
        print(node.value)

def breadthfirstTraversal(node, count = 0):
    if count == 0:
        print(node.value)
        count += 1
    if node:
        if node.left:
            print(node.left.value)
        if node.right:
            print(node.right.value)
        breadthfirstTraversal(node.left, count)
        breadthfirstTraversal(node.right, count)

if __name__ == '__main__':
    tree = Tree(Node("A"))

    tree.addNode(Node("B", up = tree.root), "left")
    tree.addNode(Node("D", up = tree.getNode("B")), "left")
    tree.addNode(Node("E", up = tree.getNode("B")), "right")

    tree.addNode(Node("C", up = tree.root), "right")
    tree.addNode(Node("F", up = tree.getNode("C")), "left")

    tree.addNode(Node("G", up = tree.getNode("C")), "right")
    tree.addNode(Node("H", up = tree.getNode("G")), "left")
    tree.addNode(Node("I", up = tree.getNode("G")), "right")

    breadthfirstTraversal(tree.root)
