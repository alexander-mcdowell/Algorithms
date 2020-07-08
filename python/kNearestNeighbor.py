import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

def LpNorm(a, b, p):
    s = 0
    for i in range(len(a)):
        s += abs(a[i] - b[i]) ** p
    return s ** (1/p)

def kNN(test_data, train_data, k, classes):
    classifications = []
    for target in test_data:
        distances = []
        for data in train_data:
            distances.append(LpNorm(target, data[:-1], p = 2))
        top_k = sorted(distances)[:k]
        top_k_classes = [train_data[distances.index(x)][-1] for x in top_k]
        counts = {top_k_classes.count(c): c for c in classes}
        classifications.append(counts[max(counts)])
    return classifications

N = 100
centers = [(2, 2), (4, 4)]
cluster_std = [1.5, 2]
X, classes = make_blobs(n_samples = N, cluster_std = cluster_std, centers = centers, n_features = 2)
train_data = [[X[i][0], X[i][1], classes[i]] for i in range(N)]
plt.scatter(X[classes == 0, 0], X[classes == 0, 1], color = "red")
plt.scatter(X[classes == 1, 0], X[classes == 1, 1], color = "blue")
plt.suptitle("k-Nearest Neighbor Classification")

test_data = [[1, 2], [3, 5], [2, 3], [5, 7], [0, 3]]
k = 5
classifications = kNN(test_data, train_data, k, [0, 1])
plt.title("k = %d" % k)
for i in range(len(test_data)):
    plt.scatter(test_data[i][0], test_data[i][1], color = "black")
    print("Point at (%.3f, %.3f) belongs to classification %s" % (test_data[i][0], test_data[i][1], ["red", "blue"][classifications[i]]))
plt.show()
