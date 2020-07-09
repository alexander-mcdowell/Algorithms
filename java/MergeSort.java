/*
Merge Sort: An efficient divide-and-conquer algorithm that divides the array up and sorts each subarray when they are merged.
Worst-case performance: O(n log n) where n is the length of the array.
Best-case performance: O(n log n)
Average performance: O(n log n)
Worst-case space complexity: O(n)
Method:
    1. Recursively divide the array in half until each element is by itself.
    2. Merge each array half using the merge function.
    Merge function:
        1. Let i be an index for the first array and j be an index for the second array. Let the merged array be merged = []
        2. If array1[i] < array[j]: merged.append(array1[i]); i++
        2 cont. Else if array1[i] >= array[j]: merged.append(array2[j]); j++
        3. If one of the arrays has no more elements, add the remaining elements from the other array to merged in the order they appear.
*/

class MergeSort {
    private static double[] merge(double[] left, double[] right) {
        int i = 0;
        int j = 0;
        int k = 0;
        double[] merged = new double[left.length + right.length];

        // Choose the minimum from both arrays and add to merged
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                merged[k] = left[i];
                i += 1;
            } else {
                merged[k] = right[j];
                j += 1;
            }
            k += 1;
        }
        // Add remainder
        while (i < left.length) {
            merged[k] = left[i];
            i += 1;
            k += 1;
        }
        while (j < right.length) {
            merged[k] = right[j];
            j += 1;
            k += 1;
        }

        return merged;
    }

    public static double[] sort(double[] array) {
        if (array.length != 1) {
            // Divide array into halves
            int n = array.length;
            int k = n / 2;
            double[] left_half = new double[k];
            double[] right_half = new double[n - k];
            for (int i = 0; i < k; i++) left_half[i] = array[i];
            for (int i = k; i < n; i++) right_half[i - k] = array[i];

            // Divide and conquer
            left_half = sort(left_half);
            right_half = sort(right_half);
            return merge(left_half, right_half);
        }
        return array;
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
        System.out.println("Mergesort took " + duration + " seconds.");
    }
}