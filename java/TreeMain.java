public class TreeMain {
    public static void main(String[] args) {
        Tree tree = new Tree("A", 0);
        tree.add(tree.root, new Node("B", 1));
        tree.add(tree.root, new Node("C", 2));
        tree.add(tree.root, new Node("D", 3));
        Node next = tree.root.children.get(0);
        tree.add(next, new Node("E", 4));
        tree.add(next, new Node("F", 5));
        next = tree.root.children.get(1);
        tree.add(next, new Node("G", 6));
        tree.add(next, new Node("H", 7));

        tree.print(tree.root, 0);

        System.out.println("Depth-first Traversal: " + tree.depthFirstTraversal(tree.root));
        System.out.println("Breadth-first Traversal: " + tree.breadthFirstTraversal(tree.root));
        System.out.println("Inorder Traversal: " + tree.inorderTraversal(tree.root));
        System.out.println("Preorder Traversal: " + tree.preorderTraversal(tree.root));
        System.out.println("Postorder Traversal: " + tree.postorderTraversal(tree.root));

        tree.root.removeChild("C");

        tree.print(tree.root, 0);
    }
}