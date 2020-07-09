/*
Insertion Sort: Simple sorting algorithm that works relatively well for small lists.
Worst-case performance: O(n^2) where n is the length of the array.
Average-case performance: O(n^2)
Best-case performance: O(n)
Worst-case space complexity: O(1)
Method:
    1. Loop through the array. If array[i + 1] < array[i], insert array[i + 1] into the subarray to the left such that the subarray is sorted.
    1 cont. For example, if [3, 7, 8, 5] is the part of the array that has been seen thusfar, 5 is inserted in between 3 and 7 so that the subarray is [3, 5, 7, 8].
*/

class InsertionSort {
    public static double[] sort(double array[]) {
        double[] sorted = array.clone();
        int i = 1;
        int j;

        while (i != array.length) {
            if (sorted[i] < sorted[i - 1]) {
                j = i;
                while (true) {
                    if (j == 0) break;
                    if (sorted[j] < sorted[j - 1]) {
                        // Swap the two elements
                        sorted[j] += sorted[j - 1];
                        sorted[j - 1] = sorted[j] - sorted[j - 1];
                        sorted[j] -= sorted[j - 1];

                        j -= 1;
                    }
                    else break;
                }
            }
            i += 1;
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

        System.out.println("Insertion sort took " + duration + " seconds.");
    }
}