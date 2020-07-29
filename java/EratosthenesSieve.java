class EratosthenesSieve {
    public static int[] findPrimes(int n) {
        int primes[] = new int[n];
        for (int x = 1; x < n + 1; x++) primes[x - 1] = x;
        int i = 1;
        int x, k;
        while (true) {
            x = primes[i];
            k = 2;
            if (x <= Math.floor(Math.sqrt(n))) {
                if (x != -1) {
                    while (k * x <= n) {
                        if (primes[k * x - 1] != -1) {
                            primes[k * x - 1] = -1;
                        }
                        k++;
                    }
                }
            } else break;
            i++;
        }
        int m = 0;
        for (int j = 0; j < n; j++) {
            if (primes[j] != -1 && primes[j] != 1) m++;
        }

        int new_primes[] = new int[m];
        int u = 0;
        for (int j = 0; j < n; j++) {
            if (primes[j] != -1 && primes[j] != 1) {
                new_primes[u] = j + 1;
                u++;
            }
        }
        return new_primes;
    }
    public static void main(String[] args) {
        int N = (int) 1e9;
        int primes[] = findPrimes(N);
        System.out.println("There are " + primes.length + " primes less than " + N + ".");
    }
}