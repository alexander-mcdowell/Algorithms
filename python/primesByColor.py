# Eratosthenes sieve: A quick and dirty method for finding primes.
# Average time performance: O(n log log n) where n is the number of numbers to search.
# Method:
    # 1. Create a list of all the numbers between 2 and n.
    # 2. Loop through the list and remove all multiples of the number chosen.
    # 3. When the loop is finished, all the remaining numbers are prime.

def findPrimes(max):
    nums = list(range(2, max + 1))
    for n in nums:
        k = int((max / n) - n)
        for m in range(0, k + 1):
            x = m * n + n ** 2
            if x in nums:
                nums.remove(x)
    return nums

if __name__ == '__main__':
    print(len(findPrimes(int(1e6))))
