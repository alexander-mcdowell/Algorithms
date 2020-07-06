class LinkedList {
    public static class LinkedListObj {
        private double value;
        private LinkedListObj next;

        public LinkedListObj() {
            next = null;
        }

        public LinkedListObj(double value) {
            this.value = value;
            next = null;
        }

        public LinkedListObj(double value, LinkedListObj next) {
            this.value = value;
            this.next = next;
        }

        public void set(double value) {
            this.value = value;
        }

        // Add a new linked list object to the end of the array.
        public void append(double value) {
            LinkedListObj iter = this;
            while (iter.next != null) iter = iter.next;
            iter.next = new LinkedListObj(value);
        }

        public void append(double[] value) {
            LinkedListObj iter = this;
            while (iter.next != null) iter = iter.next;
            for (int i = 0; i < value.length; i++) {
                iter.next = new LinkedListObj(value[i]);
                iter = iter.next;
            }
        }

        // Add a new linked list object at index i (as perceived by this object).
        // If i is never reached, just append. i cannot equal 1.
        public void insert(double value, int i) {
            if (i == 0) addToFront(value);
            LinkedListObj iter = this;
            int counter = 0;
            while ((iter != null) && (counter != i - 1)) {
                iter = iter.next;
                counter++;
            }
            LinkedListObj temp = iter.next;
            iter.next = new LinkedListObj(value);
            iter.next.next = temp;
        }

        // Adds a new value to the front of the linked list and returns the new front
        public LinkedListObj addToFront(double value) {
            LinkedListObj newFront = new LinkedListObj(value, this);
            return newFront;
        }

        public double pop(int i) {
            LinkedListObj iter = next;
            LinkedListObj prev = this;
            int counter = 0;
            while ((iter != null) && (counter != i - 1)) {
                prev = iter;
                iter = iter.next;
                counter++;
            }
            if (iter == null) return -Double.MAX_VALUE;
            prev.next = iter.next;
            return iter.value;
        }

        public void print() {
            System.out.print(value + " -> ");
            LinkedListObj iter = next;
            while (iter != null) {
                System.out.print(iter.value + " -> ");
                iter = iter.next;
            }
            System.out.print("null\n");
        }
    }

    public static void main(String[] args) {
        LinkedListObj root = new LinkedListObj(0);
        root.append(new double[]{1, 1, 2, 3, 5, 8, 13, 21});
        root.print();
        root = root.addToFront(-1);
        root.print();
        System.out.println(root.pop(5));
        root.insert(10, 3);
        root.append(34);
        root.print();
    }
}