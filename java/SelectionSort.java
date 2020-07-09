/*
Selection sort: a simple sorting algorithm that can be easily implemented but has generally poor performance.
Worst-case performance: O(n^2) comparisons and O(n) swaps where n is the length of the array.
Average-case performance: O(n^2) comparisons and O(n) swaps.
Best-case performance: O(n^2) comparisons and O(n) swaps.
Method:
    1. Start at the first index.
    2. Loop through the array and swap the value at the current index with the minimum value in the array that is lower.
    2 cont. For example, if the list is [3, 7, 8, 5, 2] and starts at the first index, swap the 3 and the 2.
    3. Increment the index.
    4. Repeat 2-4 until the maximum index has been reached. The array will have been sorted.
*/

class SelectionSort {
    public static double[] sort(double[] array) {
        double[] sorted = array.clone();
        double smallest;
        int smallest_index;

        for (int i = 0; i < array.length - 1; i++) {
            smallest = sorted[i];
            smallest_index = i;
            for (int j = i + 1; j < array.length; j++) {
                if (sorted[j] < smallest) {
                    smallest = sorted[j];
                    smallest_index = j;
                }
            }
            // Swap the current i with index of smallest value
            if (i != smallest_index) {
                sorted[i] += sorted[smallest_index];
                sorted[smallest_index] = sorted[i] - sorted[smallest_index];
                sorted[i] -= sorted[smallest_index];
            }
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

        System.out.println("Selection sort took " + duration + " seconds.");
    }
}