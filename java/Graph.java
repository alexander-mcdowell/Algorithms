class Graph {
    public int maxVertices;
    public int numVerticesDeclared;
    private double[][] adjacencyMatrix;
    private String[] vertexNames;

    public Graph(int maxVertices) {
        this.maxVertices = maxVertices;
        adjacencyMatrix = new double[maxVertices][maxVertices];
        vertexNames = new String[maxVertices];

        // Initialize all of the elements in the adjacency matrix to zero.
        for (int i = 0; i < maxVertices; i++) {
            for (int j = 0; j < maxVertices; j++) {
                adjacencyMatrix[i][j] = 0.0;
            }
            vertexNames[i] = null;
        }
        numVerticesDeclared = 0;
    }

    // createVertex creates or replaces a vertex at a certain vertex index
    public void createVertex(String name, int vertexIndex) {
        if (vertexIndex < 0 || vertexIndex > maxVertices) System.err.println("vertexIndex must be greater than zero and less than maxVertices.");
        else {
            if (vertexNames[vertexIndex] == null) numVerticesDeclared += 1;
            vertexNames[vertexIndex] = name;
        }
    }

    // Connect two existing vertices
    public void connect(int vertexIndex1, int vertexIndex2, double weight) {
        if (vertexNames[vertexIndex1] == null || vertexNames[vertexIndex2] == null) System.err.println("Either vertex and vertexIndex1 or vertexIndex2 is undefined.");
        else {
            adjacencyMatrix[vertexIndex1][vertexIndex2] = weight;
            adjacencyMatrix[vertexIndex2][vertexIndex1] = weight;
        }
    }

    public void print() {
        for (int i = 0; i < maxVertices; i++) {
            if (vertexNames[i] != null) {
                System.out.print(vertexNames[i] + " (index  " + i + "): {");
                for (int j = 0; j < maxVertices; j++) {
                    if (adjacencyMatrix[i][j] != 0.0) System.out.print(" " + vertexNames[j] + " (weight " + adjacencyMatrix[i][j] + "),");
                }
                System.out.println("}");
            }
        }
    }

    // Returns the indices of all the connected vertice to a root index
    public int[] getConnected(int rootIndex) {
        int connected[] = new int[maxVertices];
        int j = 0;
        for (int i = 0; i < maxVertices; i++) {
            if (adjacencyMatrix[rootIndex][i] != 0.0) {
                connected[i] = i;
                j += 1;
            }
            else connected[i] = -1;
        }
        int pruned[] = new int[j];
        j = 0;
        for (int i = 0; i < maxVertices; i++)
            if (connected[i] != -1) {
                pruned[j] = connected[i];
                j += 1;
            }
        return pruned;
    }

    // Gets the weight of the edge connecting two vertices
    public double getWeight(int u, int v) { return adjacencyMatrix[u][v]; }
    public String getName(int vertexIndex) { return vertexNames[vertexIndex]; }
}