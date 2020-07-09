/*
Euclidean Algorithm: Quickly finds the greatest-common divisor (GCD) of two numbers.
Method:
    1. Let a and b be the two numbers with a > b.
    2. x = a % b. If x = 0, return b
    3. Else, return Euclidean(b, a % b)
Example: gcd(136, 120)
    Euclidean(136, 120): 136 = 1 * 120 + 16. So x = 16.
    Euclidean(120, 16): 120 = 7 * 16 + 8. So x = 8.
    Euclidean(16, 8): 16 = 2 * 8 + 0. So x = 0.
    Thus, the gcd is 8.
*/

class Euclidean {
    public static int gcd(int a, int b) {
        int x = (a >= b) ? (a % b) : (b % a);
        if (x == 0) return b;
        else return gcd(b, a % b);
    }
    public static void main(String[] args) {
        System.out.println("The gcd of 136 and 120 is " + gcd(136, 120));
        System.out.println("The gcd of 45 and 245 is " + gcd(45, 245));
        System.out.println("The gcd of 4353 and 5321 is " + gcd(4353, 5321));
    }
}