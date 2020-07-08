# Bubble Sort: A simple yet inefficient sorting algorithm that uses swaps to sort a list.
# Worst-Case performance: O(n^2) comparisons, O(n) swaps where n is the length of the array.
# Best-Case performance: O(n) comparisons, O(1) swaps.
# Average performance: O(n^2) comparisons, O(n^2) swaps.
# Worst-case space complexity: O(n)
# Method:
    # 1. Loop through the list, comparing list[i] and list[i + 1]. If list[i + 1] > list[i], swap the two.
    # 2. Repeat 1 until the list is sorted.

def bubblesort(list):
    iterations = 0
    i = 1
    swapped = False
    while True:
        if i == len(list):
            i = 1
            if not swapped: break
            swapped = False
        if list[i] > list[i - 1]:
            list[i], list[i - 1] = list[i - 1], list[i]
            swapped = True
        i += 1
        iterations += 1
    return list[::-1], iterations

a = [3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1]
print("Unosorted list: " + str(a))
a, iterations = bubblesort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations")
