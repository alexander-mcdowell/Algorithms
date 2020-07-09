/*
Heapsort: Efficient sorting algorithm that sorts arrays through the use of a max heap.
A max heap is a binary tree where each node is larger than each of its children.
Worst-case performance: O(n log n) where n is the length of the array.
Best-case performance: O(n log n)
Average performance: O(n log n)
Worst-case space complexity: O(n) or O(1) depending if the heap is separate from the array or not.
Method:
    1. Construct a max-heap out of the list using the max_heapify algorithm.
        Max_Heapify: for each list element added to the heap, check if the max heap property applies; if not, swap the nodes until it does.
    2. Create a list "sorted_list"
    3. Repeat until the heap is empty. sorted_list is now sorted.
*/

class Heapsort {
    public static double[] sort(double array[]) {
        Heap heap = new Heap();
        heap.pushAll(array);
        double sorted[] = new double[array.length];
        for (int i = 0; i < array.length; i++) sorted[i] = heap.pop();
        // Reverse the order of the array from max -> smallest to smallest -> max.
        double temp;
        for (int i = 0; i < array.length / 2; i++) {
            temp = sorted[array.length - i - 1];
            sorted[array.length - i - 1] = sorted[i];
            sorted[i] = temp;
        }
        return sorted;
    }
    public static void main(String[] args) {
        double[] array = new double[]{3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1};
        System.out.println("Unsorted array: ");
        for (double x : array) System.out.print(x + ", ");
        System.out.println();
        
        long startTime = System.nanoTime();
        double[] sorted = sort(array);
        long endTime = System.nanoTime();
        double duration = (endTime - startTime) * (1e-9);

        System.out.println("Sorted array: ");
        for (double x : sorted) System.out.print(x + ", ");
        System.out.println();

        System.out.println("Heapsort took " + duration + " seconds.");
    }
}