public class GaussianElimination {
    // Get a sub-array of all the elements between start and end (not including end)
    public static double[] slice(double arr[], int start, int end) {
        if (end > start) System.err.println("end is greater than start in slice().");
        if (end >= arr.length) System.err.println("end is greater than the dimension of arr.");
        if (start < 0) System.err.println("start must be non-negative.");
        double sliced[] = new double[end - start];

        for (int i = start; i < end; i++) {
            sliced[i - start] = arr[i];
        }

        return sliced;
    }

    // Return an array with the value at index i removed.
    public static double[] delete(double arr[], int i) {
        double deleted[] = new double[arr.length - 1];
        int k = 0;
        for (int j = 0; j < arr.length; j++) {
            if (j != i) {
                deleted[k] = arr[j];
                k++;
            }
        }
        return deleted;
    }

    // Checks if all values of an array are equal to that value
    public static boolean allEqual(double arr[], double val) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == val) count += 1;
        }
        return count == arr.length;
    }

    // Determines the pivot point for row-reducing
    public static int[] getPivot(Matrix A) {
        int count;
        int k = -1;
        double col[] = new double[A.getNumRows() - 1];

        for (int i = 0; i < A.getNumRows(); i++) {
            count = 0;
            for (int j = 0; j < A.getNumCols(); j++) {
                col = delete(A.getCol(j), i);
                if (A.get(i, j) == 0 || !allEqual(col, 0)) {
                    count += 1;
                    if (A.get(i, j) != 0 && k == -1) k = j;
                }
            }
            if (count == A.getNumCols()) {
                if (k == -1) return new int[]{-1, -1};
                return new int[]{i, k};
            }
        }
        return new int[]{-1, -1};
    }

    public static Matrix rowReduce(Matrix A) {
        Matrix rowReduced = A.copy();
        int pivot[] = new int[2];

        // Repeatedly row-reduce by choosing a pivot point and subtracting out multiples of that pivot
        while (true) {
            pivot = getPivot(rowReduced);
            if (pivot[0] == -1 && pivot[1] == -1) break;
            if (allEqual(rowReduced.getRow(pivot[0]), 0)) break;
            
            for (int i = 0; i < rowReduced.getNumRows(); i++) {
                if (i != pivot[0]) {
                    double x[] = new double[A.getNumCols()];
                    for (int j = 0; j < rowReduced.getNumCols(); j++) {
                        x[j] = rowReduced.get(i, j) - (rowReduced.get(pivot[0], j) * 
                            (rowReduced.get(i, pivot[1]) / rowReduced.get(pivot[0], pivot[1])));
                    }
                    rowReduced.setRow(x, i);
                }
            }
        }

        // Determine rows to swap
        int indices[] = new int[rowReduced.getNumRows()];
        for (int i = 0; i < rowReduced.getNumRows(); i++) {
            indices[i] = i;
            for (int j = 0; j < rowReduced.getNumCols(); j++) {
                if (rowReduced.get(i, j) != 0) {
                    if (j != i) indices[i] = j;
                    break;
                }
            }
        }

        // Swap rows as part of conversion to row-echelon
        Matrix swapped = rowReduced.copy();
        for (int i = 0; i < rowReduced.getNumRows(); i++) {
            swapped.setRow(rowReduced.getRow(indices[i]), i);
        }
        rowReduced = swapped.copy();
        // Remove the temporary swapped object.
        swapped = null;
        System.gc();

        // Scale rows as part of conversion to row-echelon.
        double c;
        for (int i = 0; i < rowReduced.getNumRows(); i++) {
            c = 1;
            for (int j = 0; j < rowReduced.getNumCols(); j++) {
                if (rowReduced.get(i, j) != 0) {
                    c = rowReduced.get(i, j);
                    break;
                }
            }
            for (int j = 0; j < rowReduced.getNumCols(); j++) {
                rowReduced.set(rowReduced.get(i, j) / c, i, j);
            }
        }

        return rowReduced;
    }

    public static void main(String[] args) {
        Matrix matrix = new Matrix(3, 4);
        matrix.set(new double[][]{{3, 0, -9, 33}, {7, -4, -1, -15}, {4, 6, 5, -6}});

        System.out.println("Original Matrix:");
        System.out.println(matrix);
        System.out.println("Row-Reduced Matrix:");
        System.out.println(rowReduce(matrix));
    }  
}