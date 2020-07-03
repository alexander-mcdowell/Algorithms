import numpy as np

# Choose a pivot in a matrix.
# A pivot is any non-zero number in a row such that the elements in its column (and the other row-member's columns) are non-zero.
def getPivot(matrix):
    for i in range(len(matrix)):
        count = 0
        k = -1
        for j in range(len(matrix[i])):
            a = np.delete(matrix.T[j], i)
            #print(count, matrix[i][j], a, matrix[i], matrix.T[j], matrix[i][j] == 0, not np.all(a == 0))
            if (matrix[i][j] == 0) or (not np.all(a == 0)): 
                count += 1
                if matrix[i][j] != 0 and k == -1: k = j
            if count == len(matrix[i]): 
                if k == -1: return None
                return (i, k)

def GaussianElimination(matrix):
    reduced = np.copy(matrix)
    
    # Repeatedly row-reduce by choosing a pivot point and subtracting out multiples of that pivot
    while True:
        pivot = getPivot(reduced)
        #print(reduced, pivot)
        if pivot == None: break
        if np.all(reduced[pivot[0]] == 0): break
        for i in range(len(matrix)):
            if i != pivot[0]:
                a = reduced[pivot[0]] * (reduced[i][pivot[1]] / reduced[pivot[0], pivot[1]])
                reduced[i] -= a
    
    # Determine rows to swap
    indices = list(range(len(matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if reduced[i][j] != 0:
                if j != i: indices[i] = j
                break

    # Swap rows as part of conversion to row-echelon
    swapped = np.zeros(matrix.shape)
    for i in range(len(indices)):
        swapped[i] = reduced[indices[i]]
    reduced = np.copy(swapped)
    del swapped

    # Scale rows as part of conversion to row-echelon.
    for i in range(len(matrix)):
        k = 1
        for j in range(len(matrix[i])):
            if reduced[i][j] != 0:
                k = reduced[i][j]
                break
        reduced[i] /= k

    return reduced

if __name__ == "__main__":
    a = np.array([[3, 0, -9, 33], [7, -4, -1, -15], [4, 6, 5, -6]], dtype = np.float64)
    b = GaussianElimination(a)
    print("A:")
    print(a)
    print("Row-Reduced A:")
    print(b)