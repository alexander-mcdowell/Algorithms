/*
Binary Search: Quickly finds a desired value in a pre-sorted list.
Worst-Case performance: O(log n) for an array of length n.
Average performance: O(log n)
Best-Case performance: O(1)
Method:
    1. Let the desired value be x.
    2. Start halfway through the list and let this value be y.
    2 cont. If x > y: split the values left of y and repeat.
    2 cont. If x < y: split the values right of y and repeat.
    2 cont. If x == y: the value has been found; stop.
*/

class BinarySearch {
    public static int search(double[] array, double element) {
        int low = 0;
        int high = array.length - 1;
        int midpoint;

        while (true) {
            midpoint = (int) Math.ceil((high + low) / 2.0);
            if (array[midpoint] == element) return midpoint;
            else if (array[midpoint] > element) high = midpoint - 1;
            else if (array[midpoint] < element) low = midpoint + 1;
            
            if (midpoint == high || midpoint == low) {
                System.err.println("Element " + element + " is not in the list.");
                return -1;
            }
        }
    }
    public static void main(String[] args) {
        double array[] = {1.4, 4.6, 7.4, 8.4, 10.6, 20.7, 30.2, 40.9, 59.0, 65.7, 98.6, 100.9};
        for (double x : array) {
            int index = search(array, x);
            if (index > -1) System.out.println("Element " + x + " found at " + index + ".");
        }
        search(array, 2);
    }
}