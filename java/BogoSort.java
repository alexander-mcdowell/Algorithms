import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

/*
Bogosort: A terrible sorting method designed as a joke algorithm never to be used in real life applications.
Worst-Case performance: O((n + 1)!) where n is the length of the array.
Best-Case performance: O(n)
Worst-Case space complexity: O(n)
Method:
    1. Repeatedly shuffle the list until it is sorted.
*/

class Bogosort {
    private static double[] shuffle(double array[]) {
        double[] shuffled = new double[array.length];
        ArrayList<Integer> indices = new ArrayList<Integer>();
        int index;
        int j = 0;
        for (int i = 0; i < array.length; i++) indices.add(i);

        while (indices.size() != 1) {
            index = indices.get(ThreadLocalRandom.current().nextInt(0, indices.size()));
            indices.remove(indices.indexOf(index));
            shuffled[j] = array[index];
            j += 1;
        }
        shuffled[j] = array[indices.get(0)];
        return shuffled;
    }

    public static double[] sort(double array[]) {
        double[] shuffled = new double[array.length];
        int count;
        while (true) {
            shuffled = shuffle(array);
            count = 0;
            for (int i = 0; i < (shuffled.length - 1); i++) {
                if (shuffled[i] <= shuffled[i + 1]) count += 1;
            }
            if (count == shuffled.length - 1) break;
        }
        return shuffled;
    }
    public static void main(String[] args) {
        double[] array = new double[]{3, 7, 8, 5, 2, 1, 9, 5, 4};
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

        System.out.println("Bogosort took " + duration + " seconds.");
    }
}