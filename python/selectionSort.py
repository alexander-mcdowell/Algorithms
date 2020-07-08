# Selection sort: a simple sorting algorithm that can be easily implemented but has generally poor performance.
# Worst-case performance: O(n^2) comparisons and O(n) swaps where n is the length of the array.
# Average-case performance: O(n^2) comparisons and O(n) swaps.
# Best-case performance: O(n^2) comparisons and O(n) swaps.
# Method:
     # 1. Start at the first index.
     # 2. Loop through the array and swap the value at the current index with the minimum value in the array that is lower.
     # 2 cont. For example, if the list is [3, 7, 8, 5, 2] and starts at the first index, swap the 3 and the 2.
     # 3. Increment the index.
     # 4. Repeat 2-4 until the maximum index has been reached. The array will have been sorted.

def heuristic(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def selectionSort(list):
    iterations = 0
    for i in range(len(list)):
        m = i
        for j in range(i + 1, len(list)):
            if heuristic(list[j], list[m]) < 0:
                m = j
            iterations += 1
        if i != m:
            list[i], list[m] = list[m], list[i]
    return list, iterations

a = [3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1]
print("Unosorted list: " + str(a))
a, iterations = selectionSort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations.")
