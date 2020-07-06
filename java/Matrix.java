public class Matrix {
    private double elements[][];
    private int n, m;

    public Matrix(int n, int m) {
        this.n = n;
        this.m = m;
        elements = new double[n][m];
    }

    public void set(double value, int i, int j) {
        if (i > n || j > m) System.err.println("Indices for set() exceed matrix dimensions.");
        if (i < 0 || j < 0) System.err.println("Indices for set() must be non-negative.");
        elements[i][j] = value;
    }

    public void set(double values[][]) {
        if (values.length != n || values[0].length != m) 
            System.err.println("Dimensions of 2D array for set() do not equal matrix dimensions.");
        for (int i = 0; i < values.length; i++) {
            for (int j = 0; j < values[0].length; j++) {
                elements[i][j] = values[i][j];
            }
        }
    }

    // Set row to array of values.
    public void setRow(double values[], int i) {
        if (i > n) System.err.println("Index for setRow() exceeds matrix dimensions.");
        if (i < 0) System.err.println("Index for setRow() must be non-negative.");
        if (values.length != m) System.err.println("Value array for setRow() is not of correct length.");
        
        for (int j = 0; j < m; j++) {
            elements[i][j] = values[j];
        }
    }

    // Set column to array of values.
    public void setCol(double values[], int j) {
        if (j > n) System.err.println("Index for setCol() exceeds matrix dimensions.");
        if (j < 0) System.err.println("Index for setCol() must be non-negative.");
        if (values.length != n) System.err.println("Value array for setCol() is not of correct length.");
        
        for (int i = 0; i < n; i++) {
            elements[i][j] = values[i];
        }
    }

    public double get(int i, int j) {
        if (i > n || j > m) System.err.println("Indices for get() exceed matrix dimensions.");
        if (i < 0 || j < 0) System.err.println("Indices for get() must be non-negative.");
        return elements[i][j];
    }

    public double[] getRow(int i) {
        if (i > n) System.err.println("Indices for getRow() exceed matrix dimensions.");
        if (i < 0) System.err.println("Indices for getRow() must be non-negative.");
        return elements[i];
    }

    public double[] getCol(int j) {
        if (j > m) System.err.println("Indices for getCol() exceed matrix dimensions.");
        if (j < 0) System.err.println("Indices for getCol() must be non-negative.");
        
        double arr[] = new double[n];
        for(int i = 0; i < n; i++) arr[i] = elements[i][j];
        return arr;
    }

    public int getNumRows() { return n; }
    public int getNumCols() { return m; }

    // Return the transpose of the current matrix
    public Matrix T() {
        Matrix transposed = new Matrix(m, n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                transposed.set(elements[i][j], j, i);
            }
        }
        return transposed;
    }

    public Matrix copy() {
        Matrix copyMatrix = new Matrix(n, m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                copyMatrix.set(elements[i][j], i, j);
            }
        }
        return copyMatrix;
    }

    // Add a matrix to the current matrix.
    public Matrix add(Matrix A) {
        if (A.getNumRows() != n || A.getNumCols() != m) System.err.println("Dimensions of A in add() do not equal the dimensions of this matrix.");
        Matrix sum = new Matrix(n, m);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sum.set(elements[i][j] + A.get(i, j), i, j); 
            }
        }

        return sum;
    }

    // Subtract a matrix from the current matrix.
    public Matrix subtract(Matrix A) {
        if (A.getNumRows() != n || A.getNumCols() != m) System.err.println("Dimensions of A in add() do not equal the dimensions of this matrix.");
        Matrix difference = new Matrix(n, m);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                difference.set(elements[i][j] - A.get(i, j), i, j); 
            }
        }

        return difference;
    }

    // Multiplication by a scalar.
    public Matrix multiply(double c) {
        Matrix scaled = new Matrix(n, m);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scaled.set(elements[i][j] * c, i, j);
            }
        }

        return scaled;
    }

    private double dot(double a[], double b[]) {
        double x = 0.0;
        for (int i = 0; i < a.length; i++) x += a[i] * b[i];
        return x;
    }

    // Multiplication by a matrix
    public Matrix multiply(Matrix A) {
        if (A.getNumRows() != m) System.err.println("The number of rows in A must equal the number of columns for multiplication.");
        int o = A.getNumCols();
        Matrix product = new Matrix(n, o);

        for (int i = 0; i < n; i++) {
            for (int k = 0; k < o; k++) {
                product.set(dot(elements[i], A.getCol(k)), i, k);
            }
        }
        
        return product;
    }

    // Multiplication by a vector
    public double[] multiply(double[] b) {
        if (b.length != m) System.err.println("The length of b must equal the number of columns for multiplication.");
        double product[] = new double[n];

        for (int i = 0; i < n; i++) {
            product[i] = dot(elements[i], b);
        }

        return product;
    }

    @Override
    public String toString() {
        String out = "[";
        for (int i = 0; i < n; i++) {
            if (i == 0) out += "[";
            else out += " [";

            for (int j = 0; j < m; j++) {
                if (j != (m - 1)) out += toSigFigs(elements[i][j], 5) + ", ";
                else out += toSigFigs(elements[i][j], 5);
            }

            if (i != n - 1) out += "],\n";
            else out += "]";
        }
        out += "]";
        return out;
    }

    private double toSigFigs(double value, int sigfigs) {
        return Math.round(Math.pow(10, sigfigs) * value) / Math.pow(10, sigfigs);
    }
}