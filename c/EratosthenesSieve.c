#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define END -100000

int* findPrimes(int n) {
    int* primes = (int *) malloc(sizeof(int) * (n + 1));
    for (int x = 1; x < n + 1; x++) *(primes + x - 1) = x;
    *(primes + n) = END;

    int i = 1;
    int x, k;
    while (1) {
        x = primes[i];
        k = 2;
        if (x <= floor(sqrt(n))) {
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
        if (*(primes + j) != -1 && *(primes + j) != 1) m++;
    }

    int* new_primes = (int *) malloc(sizeof(int) * (m + 1));
    int u = 0;
    for (int j = 0; j < n; j++) {
        if (*(primes + j) != -1 && *(primes + j) != 1) {
            *(new_primes + u) = j + 1;
            u++;
        }
    }
    *(new_primes + m) = END;
    return new_primes;
}

int main(int argc, char const *argv[]) {
    int N = (int) 1e8;
    int* primes = findPrimes(N);
    int i = 0;

    while (1) {
        if (*(primes + i) == END) break;
        i++;
    }
    (void) printf("There are %d primes less than %d\n", i, N);

    return 0;
}
