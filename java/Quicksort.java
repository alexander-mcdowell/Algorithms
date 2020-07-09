import java.util.ArrayList;

/*
Quicksort: a divide-and-conquer algorithm that is very effective.
If implemented well, quicksort can be twice or three times more effective than mergesort or heapsort.
Worst-case performance: O(n^2) where n is the length of the array.
Average-case performance: O(n log n).
Best-case performance: O(n log n).
Worst-case space complexity: O(log n).
Method:
    1. Declare the pivot point to be halfway through the array.
    2. Arrange (in any order) all elements less than the pivot to the left of the pivot and all elements greater than the pivot to the right of the pivot.
    3. Run quick sort on the left and right partitions.
    4. Combine the left and right partitions in the order of left + pivot + right. The resulting list is sorted.
*/

class Quicksort {
    public static double[] sort(double[] array) {
        ArrayList<Double> temp = new ArrayList<Double>();
        for (double x : array) temp.add(x);
        ArrayList<Double> sorted = sortArrayList(temp);
        double[] returnArr = new double[sorted.size()];
        for (int i = 0; i < sorted.size(); i++) returnArr[i] = sorted.get(i);
        return returnArr;
    }

    private static ArrayList<Double> sortArrayList(ArrayList<Double> array) {
        if (array.size() <= 1) return array;

        // Choose the pivot to be the midpoint
        int pivot = array.size() / 2;
        ArrayList<Double> left_half = new ArrayList<Double>();
        ArrayList<Double> right_half = new ArrayList<Double>();
        
        // All values less than the pivot element go to the left; all greater/equal go to the right
        for (int i = 0; i < array.size(); i++) {
            if (i != pivot) {
                if (array.get(i) < array.get(pivot)) left_half.add(array.get(i));
                else if (array.get(i) >= array.get(pivot)) right_half.add(array.get(i));
            }
        }

        // Sort the left and right partitions
        left_half = sortArrayList(left_half);
        right_half = sortArrayList(right_half);

        // Merge the left, pivot, and right
        ArrayList<Double> sorted = new ArrayList<Double>(array.size());
        sorted.addAll(left_half);
        sorted.add(array.get(pivot));
        sorted.addAll(right_half);

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
        System.out.println("Quicksort took " + duration + " seconds.");
    }
}