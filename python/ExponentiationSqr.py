import math

# There are two algorithms here: Exponentiation by Squaring and Modulo of Exponentiation by Squaring.
# Both algorithms use O(log n) squarings and O(log n) multiplications.

# Exponentiation by Squaring: Quickly computes the value n^k by using properties of squaring.
# This method works because of the property that n^k = n^a * n^b where a is a power of 2 and b is a number such that the equality is true.
# Example: 5^10
    # Init: (d, x, c) = (10, 5, 1)
    # (d, x, c) = (5, 25, 1)
    # (d, x, c) = (2, 625, 25)
    # (d, x, c) = (1, 390625, 25)
    # Result = x * c = 9765625

# Modulo of Exponentiation by Squaring: Quickly computes the value mod(n^k, p) by using properties of squaring.
# This method uses the same technique as above except that everytime a multiplication happens, mod p is applied to it.
# Example: 5^10 mod 9.
    # Init: (d, x, c) = (10, 5, 1)
    # (d, x, c) = (5, 7, 1)
    # (d, x, c) = (2, 4, 7)
    # (d, x, c) = (1, 7, 7)
    # Result = x * c mod 9 = 49 mod 9 = 4

def expBySqr(n, k):
    d = k
    x = n
    c = 1
    while d > 1:
        if (d % 2 == 1):
            c *= x
        x *= x
        d = math.floor(d / 2)
        print((d, x, c))
    return x * c

def modExpBySqr(n, k, p):
    d = k
    x = n % p
    c = 1
    while d > 1:
        if (d % 2 == 1):
            c *= x % p
        x *= x % p
        d = math.floor(d / 2)
    return (x * c) % p

n = 5
k = 10
print(expBySqr(n, k))
