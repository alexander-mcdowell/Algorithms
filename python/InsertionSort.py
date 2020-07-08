# Insertion Sort: Simple sorting algorithm that works relatively well for small lists.
# Worst-case performance: O(n^2) where n is the length of the array.
# Average-case performance: O(n^2)
# Best-case performance: O(n)
# Worst-case space complexity: O(1)
# Method:
    # 1. Loop through the array. If array[i + 1] < array[i], insert array[i + 1] into the subarray to the left such that the subarray is sorted.
    # 1 cont. For example, if [3, 7, 8, 5] is the part of the array that has been seen thusfar, 5 is inserted in between 3 and 7 so that the subarray is [3, 5, 7, 8].

def insertionSort(array):
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

a = [3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1]
print("Unosorted list: " + str(a))
a, iterations = insertionSort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations.")
