import random

# Bogosort: A terrible sorting method designed as a joke algorithm never to be used in real life applications.
# Worst-Case performance: O((n + 1)!) where n is the length of the array.
# Best-Case performance: O(n)
# Worst-Case space complexity: O(n)
# Method:
    # 1. Repeatedly shuffle the list until it is sorted.

def bogosort(list):
    def shuffle(list):
        a = list[::]
        iterations = 0
        shuffled_list = []
        while len(shuffled_list) != len(list) - 1:
            index = random.randint(0, len(a) - 1)
            shuffled_list.append(a.pop(index))
            iterations += 1
        shuffled_list.append(a.pop(0))
        return shuffled_list, iterations

    iterations = 0
    while True:
        list, iter = shuffle(list)
        iterations += iter
        count = 0
        for i in range(len(list) - 1):
            iterations += 1
            if list[i] <= list[i + 1]: count += 1
            else: break
        if count == len(list) - 1: return list, iterations

a = [3, 7, 8, 5, 2, 1, 9, 5, 4]
print("Unosorted list: " + str(a))
a, iterations = bogosort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations.")
