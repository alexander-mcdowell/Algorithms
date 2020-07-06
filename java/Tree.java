import java.util.ArrayList;

public class Tree {
    public Node root;

    public Tree(String label, double value) {
        root = new Node(label, value);
    }

    public void add(Node root, Node child) { root.addChild(child); }

    public void print(Node root, int depth) {
        if (depth == 0) System.out.println(root);
        for (Node child : root.children) {
            for (int i = 0; i < (depth + 1); i++) System.out.print("--");
            System.out.println(child);
            print(child, depth + 1);
        }
    }

    public String depthFirstTraversal(Node root) {
        String traversal = root + ", ";
        for (Node child : root.children) {
            traversal += depthFirstTraversal(child);
        }
        return traversal;
    }

    public String breadthFirstTraversal(Node root) {
        ArrayList<Node> queue = new ArrayList<Node>();
        Node u;
        queue.add(root);
        String traversal = "";
        while (queue.size() != 0) {
            u = queue.get(0);
            queue.remove(0);
            queue.addAll(u.children);
            traversal += u + ", ";
        }
        return traversal;
    }

    public String inorderTraversal(Node root) {
        String traversal = "";
        if (root.children.size() != 0) traversal += inorderTraversal(root.children.get(0));
        traversal += root + ", ";
        if (root.children.size() > 1) {
            for (int i = 1; i < root.children.size(); i++) {
                traversal += inorderTraversal(root.children.get(i));
            }
        }
        return traversal;
    }

    public String preorderTraversal(Node root) {
        String traversal = "";
        traversal += root + ", ";
        for (int i = 0; i < root.children.size(); i++) {
            traversal += preorderTraversal(root.children.get(i));
        }
        return traversal;
    }

    public String postorderTraversal(Node root) {
        String traversal = "";
        for (int i = 0; i < root.children.size(); i++) {
            traversal += postorderTraversal(root.children.get(i));
        }
        traversal += root + ", ";
        return traversal;
    }
}