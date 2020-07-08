import math

# Merge Sort: An efficient divide-and-conquer algorithm that divides the array up and sorts each subarray when they are merged.
# Worst-case performance: O(n log n) where n is the length of the array.
# Best-case performance: O(n log n)
# Average performance: O(n log n)
# Worst-case space complexity: O(n)
# Method:
    # 1. Recursively divide the array in half until each element is by itself.
    # 2. Merge each array half using the merge function.
    # Merge function:
        # 1. Let i be an index for the first array and j be an index for the second array. Let the merged array be merged = []
        # 2. If array1[i] < array[j]: merged.append(array1[i]); i++
        # 2 cont. Else if array1[i] >= array[j]: merged.append(array2[j]); j++
        # 3. If one of the arrays has no more elements, add the remaining elements from the other array to merged in the order they appear.

def split(arr):         # Split the array in halves (approximately)
    return arr[:math.floor(len(arr) / 2)], arr[math.floor(len(arr) / 2):]

def merge(left, right):     # Merge two arrays based on the smallest elements
    merged = []
    left_index, right_index = 0, 0
    iterations = 0

    while (left_index < len(left)) and (right_index < len(right)):
        if left[left_index] < right[right_index]:   # If the value of the left array is smaller than the value of the right array
            merged.append(left[left_index])         # Add the value to the merged array
            left_index += 1                         # Test the next value of the left array
        elif left[left_index] >= right[right_index]: # If the value of the left array is at least greater than the value of the right array
            merged.append(right[right_index])
            right_index += 1                        # Test the next value of the right array
        iterations += 1

    if left:                # If the left array is not empty, add the remaining elements to the merged array
        merged.extend(left[left_index:])
    if right:               # If the right array is not empty, add the remaining elements to the merged array
        merged.extend(right[right_index:])
    return merged, iterations

def mergesort(array):
    iterations = 0
    if len(array) == 1:     # If fully split, return the array
        return array, iterations

    left, right = split(array)
    left, iter1 = mergesort(left)      # Keep splititng the left side
    right, iter2 = mergesort(right)    # Keep splititng the right side
    merged, iter3 = merge(left, right)
    iterations += iter1 + iter2 + iter3
    return merged, iterations   # Merge the current left and right arrays

a = [3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1]
print("Unosorted list: " + str(a))
a, iterations = mergesort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations.")
