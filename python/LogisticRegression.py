import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

E = 2.718281828

# Logistic function and its derivative.
def logit(x): return 1/(1 + E ** -x)
def dlogit(x):
    f = logit(x)
    return f * (1 - f)

def LogisticRegression(datapoints, num_iterations, learning_rate = 0.1):
    weights = [0.0, 0.0]
    losses = []
    for iteration in range(num_iterations):
        loss = 0
        for datapoint in datapoints:
            output = datapoint[1] - (weights[0] + weights[1] * datapoint[0])
            h = logit(output)
            delta = (datapoint[2] - h)
            loss += delta ** 2
            df = dlogit(output)
            weights[0] -= learning_rate * delta * df
            weights[1] -= learning_rate * delta * df * datapoint[0]
        losses.append(loss)
    return weights, losses

N = 100
fig, axs = plt.subplots(2, 1)
# Make sure the blob to the left appears first
centers = [(2, 2), (4, 4)]
cluster_std = [1.5, 2]
X, classes = make_blobs(n_samples = N, cluster_std = cluster_std, centers = centers, n_features = 2)
data = [[X[i][0], X[i][1], classes[i]] for i in range(N)]
xs = np.hstack((X[classes == 0, 0], X[classes == 1, 0]))
axs[0].scatter(X[classes == 0, 0], X[classes == 0, 1], color = "red")
axs[0].scatter(X[classes == 1, 0], X[classes == 1, 1], color = "blue")
axs[0].set_title("Logistic Regression")

num_iterations = 500
weights, losses = LogisticRegression(data, num_iterations)
separator_xs = np.linspace(min(xs), max(xs), 100)
separator_ys = []
for x in separator_xs:
    y = weights[0] + weights[1] * x
    separator_ys.append(y)
accuracy = 0
for datapoint in data:
    if datapoint[1] - (weights[0] + weights[1] * datapoint[0]) < 0 and datapoint[2] == 0: accuracy += 1
    elif datapoint[1] - (weights[0] + weights[1] * datapoint[0]) >= 0 and datapoint[2] == 1: accuracy += 1
accuracy /= N
print("Final Loss: %.3f, Accuracy: %.2f%%" % (losses[-1], 100 * accuracy))
axs[0].plot(separator_xs, separator_ys, "k--")

axs[1].plot(list(range(num_iterations)), losses)
axs[1].set_title("Losses vs. Iterations")
plt.show()
