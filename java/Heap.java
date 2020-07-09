import java.util.ArrayList;

// Max-Heap: a binary tree created via the max-heapify property - all children are less than the root.
class Heap {
    public ArrayList<Double> array;

    public Heap() {
        array = new ArrayList<Double>();
    }

    public double pop() {
        double x = array.get(0);
        array.remove(0);
        heapify();
        return x;
    }

    public void push(double x) {
        array.add(x);
        heapify();
    }

    public void pushAll(double[] x) {
        for (double y : x) array.add(y);
        heapify();
    }

    public void heapify() {
        int i = 1;
        int j;
        while (i < array.size()) {
            j = (i - 1) / 2;
            if (array.get(i) > array.get(j)) {
                swap(i, j);
                i = j;
            } else {
                i += 1;
            }
        }
    }

    // Swaps elements without calling heapify.
    public void swap(int i, int j) {
        double x = array.get(j);
        array.set(j, array.get(i));
        array.set(i, x);
    }
}