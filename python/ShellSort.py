import math

# Shell sort: a variant of isertion sort that sorts via the use of "gaps."
# Worst-case complexity: O(n log n) where n is the length of the array.
# Average-case complexity: O(n^4/3)
# Best-case complexity: O(n^3/2)
# Worst-case space complexity: O(1)
# Method:
    # 1. Initialize the gap values.
    # 2. Loop through the possible gap values:
        # 2a. Group values that are index + multiple * gap length
        # 2b. Insertion sort the partitions. Combine the sorted partitions.
    # 3. The final list has been sorted.

def insertionsort(array):
    sorted = []
    iterations = 0
    for i in range(len(array)):
        count = 0
        for k in range(len(sorted)):
            if array[i] > sorted[k]:
                count += 1
            iterations += 1
        sorted.insert(count, array[i])
    return sorted, iterations

def shellsort(array):
    iterations = 0
    intervals = [int((3 ** k - 1) / 2) for k in range(1, math.ceil(math.log(2 * len(array) - 1) / math.log(3)))][::-1]
    for interval in intervals:
        if interval == 1: break
        partitions = []
        for i in range(interval):
            a = []
            k = 0
            while True:
                x = interval * k + i
                if x > len(array) - 1: break
                a.append(array[x])
                k += 1
            partitions.append(a)
        b = []
        for p in partitions:
            x, iter = insertionsort(p)
            b += x
            iterations += iter
        array = b
    array, iter = insertionsort(array)
    iterations += iter
    return array, iterations

a = [3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1]
print("Unosorted list: " + str(a))
a, iterations = shellsort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations.")
