import math
import numpy as np

# Binary Search: Quickly finds a desired value in a pre-sorted list.
# Worst-Case performance: O(log n) for an array of length n.
# Average performance: O(log n)
# Best-Case performance: O(1)
# Method:
    # 1. Let the desired value be x.
    # 2. Start halfway through the list and let this value be y.
    # 2 cont. If x > y: split the values left of y and repeat.
    # 2 cont. If x < y: split the values right of y and repeat.
    # 2 cont. If x == y: the value has been found; stop.

def heuristic(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def binarySearch(list, target):
    l = 0
    h = len(list) - 1
    while l <= h:
        i = l + math.floor((h - l) / 2)
        print(list[i])
        if heuristic(list[i], target) < 0:
            l = i + 1
        elif heuristic(list[i], target) > 0:
            h = i - 1
        else:
            return i
    return -1

if __name__ == '__main__':
    list = []
    for _ in range(20): list.append(np.random.randint(0, 1000))
    list = sorted(list)
    target = list[np.random.randint(0, len(list) - 1)]
    print(list, target)
    index = binarySearch(list, target)
    if index >= 0:
        print(str(target) + " is at index #" + str(index) + " of the list")
    else:
        print(str(target) + " is not in the list")
