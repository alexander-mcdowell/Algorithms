import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

# Perceptron Classifier: A simple yet powerful machine learning algorithm that classifies data according to a threshold.
# For this task, the agent will determine the linear separator that best separates a group of data with two variables, x and y.
# If h(x, w) is the model where x is the data being tested and w are the weights of the linear separator,
# Then h(x, w) = 0 if x is to the left of the linear separator and h(x, w) = 1 if x is to the right of the linear separator.

def threshold(x): return 1.0 if x >= 0.0 else 0.0

def PerceptronClassifier(datapoints, num_iterations = 1000, learning_rate = 0.01):
    N = len(datapoints)
    weights = [0.0, 0.0]
    losses = []
    accuracies = []
    for iteration in range(num_iterations):
        loss = 0
        accuracy = 0
        for datapoint in datapoints:
            output = weights[0] + weights[1] * datapoint[0]
            h = threshold(datapoint[1] - output)
            delta = datapoint[2] - h
            loss += delta
            weights[0] -= learning_rate * delta
            weights[1] -= learning_rate * delta * datapoint[0]
            if delta == 0: accuracy += 1
        losses.append(loss)
        accuracies.append(accuracy / N)
    return weights, losses, accuracies

N = 100
# Make sure the blob to the left appears first
centers = [(2, 2), (4, 4)]
cluster_std = [1.5, 2]
X, classes = make_blobs(n_samples = N, cluster_std = cluster_std, centers = centers, n_features = 2)
data = [[X[i][0], X[i][1], classes[i]] for i in range(N)]
xs = np.hstack((X[classes == 0, 0], X[classes == 1, 0]))
plt.scatter(X[classes == 0, 0], X[classes == 0, 1], color = "red")
plt.scatter(X[classes == 1, 0], X[classes == 1, 1], color = "blue")

weights, losses, accuracies = PerceptronClassifier(data)
separator_xs = np.linspace(min(xs), max(xs), 100)
separator_ys = []
for x in separator_xs:
    y = weights[0] + weights[1] * x
    separator_ys.append(y)
print("Accuracy: %.2f%%" % (accuracies[-1] * 100))
plt.plot(separator_xs, separator_ys, "k--")
plt.title("Perceptron Classifier")
plt.show()
