import math

# Euclidean Algorithm: Quickly finds the greatest-common divisor (GCD) of two numbers.
# Method:
    # 1. Let a and b be the two numbers with a > b.
    # 2. x = a % b. If x = 0, return b
    # 3. Else, return Euclidean(b, a % b)
# Example: gcd(136, 120)
    # Euclidean(136, 120): 136 = 1 * 120 + 16. So x = 16.
    # Euclidean(120, 16): 120 = 7 * 16 + 8. So x = 8.
    # Euclidean(16, 8): 16 = 2 * 8 + 0. So x = 0.
    # Thus, the gcd is 8.

# r is gcd(a, b) and x and y are the integers such that r = ax + by
# For (a, b) => (r, x, y), r is the gcd of (a,b) and x is the multiplicative inverse of a mod b
def euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        r, x, y = euclid(b, a % b)
        return (r, y, x - math.floor(a / b) * y)

if __name__ == '__main__':
    a = 46
    b = 240
    r, x, _ = euclid(a, b)
    print("The gcd of %d and %d is %d" % (a, b, r))
    print("The multiplicative inverse of %d mod %d is %d" % (a, b, x))
