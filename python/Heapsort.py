import math

# Heapsort: Efficient sorting algorithm that sorts arrays through the use of a max heap.
# A max heap is a binary tree where each node is larger than each of its children.
# Worst-case performance: O(n log n) where n is the length of the array.
# Best-case performance: O(n log n)
# Average performance: O(n log n)
# Worst-case space complexity: O(n) or O(1) depending if the heap is separate from the array or not.
# Method:
    # 1. Construct a max-heap out of the list using the max_heapify algorithm.
        # Max_Heapify: for each list element added to the heap, check if the max heap property applies; if not, swap the nodes until it does.
    # 2. Create a list "sorted_list"
    # 3. Swap the root node with the furthestmost node. Pop the furthestmost node and add it to sorted_list. Apply Max_Heapify to the new heap.
    # 4. Repeat 3 until the heap is empty. sorted_list is now sorted.

def max_heapify(list):
    heaped_list = list
    i = 0
    iterations = 0
    while (2 * i + 1) < len(heaped_list):
        left, right = 2 * i + 1, 2 * i + 2
        swap = i
        if heaped_list[left] > heaped_list[swap]: swap = left
        if right < len(heaped_list):
            if heaped_list[right] > heaped_list[swap]: swap = right
        if swap != i:
            heaped_list[i], heaped_list[swap] = heaped_list[swap], heaped_list[i]
            j = i
            k = math.floor(j - 1 / 2)
            while not k < 0:
                if heaped_list[k] < heaped_list[j]:
                    heaped_list[j], heaped_list[k] = heaped_list[k], heaped_list[j]
                    j = k
                else: break
                iterations += 1
                k = math.floor(j - 1 / 2)
        else:
            i += 1
            iterations += 1
    return heaped_list, iterations

def heapsort(list):
    sorted_list = []
    iterations = 0
    list, i = max_heapify(list)
    iterations += i
    while len(list) != 0:
        list[-1], list[0] = list[0], list[-1]
        sorted_list.append(list.pop(-1))
        list, i = max_heapify(list)
        iterations += i
    return sorted_list[::-1], iterations

a = [3, 7, 8, 5, 2, 1, 9, 5, 4, 4, 7, 5, 3, 4, 8, 7, 3, 7, 9, 2, 5, 8, 0, 2, 6, 6, 1]
print("Unosorted list: " + str(a))
a, iterations = heapsort(a)
print("Sorted list: " + str(a))
print("Sort took " + str(iterations) + " iterations.")
