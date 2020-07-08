# Quicksort: a divide-and-conquer algorithm that is very effective.
# If implemented well, quicksort can be twice or three times more effective than mergesort or heapsort.
# Worst-case performance: O(n^2) where n is the length of the array.
# Average-case performance: O(n log n).
# Best-case performance: O(n log n).
# Worst-case space complexity: O(log n).
# Method:
    # 1. Declare the pivot point to be halfway through the array.
    # 2. Arrange (in any order) all elements less than the pivot to the left of the pivot and all elements greater than the pivot to the right of the pivot.
    # 3. Run quick sort on the left and right partitions.
    # 4. Combine the left and right partitions in the order of left + pivot + right. The resulting list is sorted.

def quicksort(array):
    iterations = 0
    if len(array) <= 1:         # If the array is a singular value or [].
        return array, iterations
    else:
        pivot = array[len(array) // 2]       # Use the middle value as the pivot
        left = []       # Values less than the pivot
        middle = []     # Values equal to the pivot
        right = []      # Values more than the pivot

        for i in array:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                middle.append(i)
            iterations += 1

    left, iter1 = quicksort(left)      # Recurse through the leftmost values
    right, iter2 = quicksort(right)    # Recurse through the rightmost values
    iterations += iter1 + iter2
    return left + middle + right, iterations

a = [3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1]
print("Unosorted list: " + str(a))
a, iterations = quicksort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations.")
