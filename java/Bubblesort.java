/*
Bubble Sort: A simple yet inefficient sorting algorithm that uses swaps to sort a list.
Worst-Case performance: O(n^2) comparisons, O(n) swaps where n is the length of the array.
Best-Case performance: O(n) comparisons, O(1) swaps.
Average performance: O(n^2) comparisons, O(n^2) swaps.
Worst-case space complexity: O(n)
Method:
    1. Loop through the list, comparing list[i] and list[i + 1]. If list[i + 1] > list[i], swap the two.
    2. Repeat 1 until the list is sorted.
*/

class Bubblesort {
    public static double[] sort(double array[]) {
        double[] sorted = array.clone();
        int swaps;
        while (true) {
            swaps = 0;
            for (int i = 0; i < sorted.length - 1; i++) {
                if (sorted[i] > sorted[i + 1]) {
                    // Swap the elements
                    sorted[i] += sorted[i + 1];
                    sorted[i + 1] = sorted[i] - sorted[i + 1];
                    sorted[i] -= sorted[i + 1];
                    swaps += 1;
                }
            }
            if (swaps == 0) break;
        }
        return sorted;
    } 
    public static void main(String[] args) {
        double[] array = new double[]{3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 11};
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

        System.out.println("Bubblesort took " + duration + " seconds.");
    }
}