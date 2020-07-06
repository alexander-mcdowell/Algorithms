import java.util.ArrayList;

public class Node {
    public String label;
    public double value;
    public ArrayList<Node> children = new ArrayList<Node>();

    public Node(String label, double value) {
        this.label = label;
        this.value = value;
    }

    public void addChild(Node child) { children.add(child); }
    
    public void removeChild(String label) {
        Node toRemove = null;
        for (Node child : children) {
            if (child.label == label) {
                toRemove = child;
                break;
            }
        }
        if (toRemove == null) System.out.println("Removal of child node failed. Label '" + label + "' not found,");
        else {
            while (toRemove.children.size() != 0) toRemove.children.remove(toRemove.children.get(0));
            children.remove(toRemove);
        }
    }
    
    @Override
    public String toString() {
        return "{" + label + ": " + value + "}";
    }
}