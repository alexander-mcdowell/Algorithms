import math
import numpy as np
import matplotlib.pyplot as plt

# Naive Bayes Classifier: Decides, out of a given list of classes and labeled training data, which class given test data belong in.
# Assumption: The classifier is "Naive" because it assumes that the training data is mututally independent from one another and only dependent on the class.
# Method:
    # 1. For the given training data, compute the probability that a property x is true given it belongs to a known class C_k = P(x | C_k)
    # 1 cont. For example, one might find P(height = 68 inches | male).
    # 2. Compute the probability of a given test data X belongs to a class C_k = P(C_k | X)
    # 2 cont. Applying bayes rule successively yields P(C_k | X) = a * P(C_k, X) = a * P(X | C_k) = a * P(x1 | C_k, x2, x3, ...) * P(x2 | C_k, x3, x4, ...) * ... * P(C_k)
    # 2 cont. Making the assumption that data is mutually independent from one another yields P(C_k | X) = a * P(C_k) * P(x1 | C_k) * P(x2 | C_k) * ... * P(xn | C_k)
    # 3. The class that the test data most likely belongs to is the class C_k that maximizes P(C_k | X) that was computed above.

# This bayesian classifer takes a list of conditional probabilities, probabilities of each class occurring, and a list of class labels.
# The conditional probabilities are of the form p(x_i | C_k) where x_i is some data that is dependent on its class C_k.
def BayesClassifier(conditionals, class_probabilities, class_labels):
    assert len(class_probabilities) == len(class_labels)
    best_prob = 0
    best_k = 0
    for k in range(len(class_labels)):
        probability = class_probabilities[k]
        # The assumption here is that the data is mututally independent from one another and only dependent on the class.
        for prob in conditionals[k]:
            probability *= prob
        if probability > best_prob:
            best_k = k
            best_prob = probability
    return class_labels[best_k]

# Computes the conditional probability that a datapoint belongs to a given class which follows a normal distribution.
def Gaussian(data, mean, stdev):
    return math.exp(-(data - mean) ** 2 / (2 * stdev ** 2)) / math.sqrt(2 * math.pi * stdev ** 2)

def mean(data): return sum(data) / len(data)
def stdev(data):
    val = 0
    u = mean(data)
    for x in data: val += (x - mean(data)) ** 2
    return math.sqrt(val / len(data))

num_points = 500
class_probabilities = [0.5, 0.2, 0.3]
colors = ["red", "blue", "green"]
num_classes = len(class_probabilities)
point_partitions = [round(num_points * class_probabilities[k]) for k in range(num_classes - 1)]
point_partitions.append(num_points - sum(point_partitions))

means_x, means_y = [4.0, 5.0, 6.0], [4.0, 5.0, 6.0]
stdevs_x, stdevs_y = [1, 0.5, 1.2], [1, 0.5, 1.2]
noisiness = 0.1
xs = [np.random.normal(means_x[k], stdevs_x[k], point_partitions[k]) + noisiness * np.random.randn() for k in range(num_classes)]
ys = [np.random.normal(means_y[k], stdevs_y[k], point_partitions[k]) + noisiness * np.random.randn() for k in range(num_classes)]
for k in range(num_classes):
    plt.scatter(xs[k], ys[k], s = 10, c = colors[k])

test_data = [[2, 3], [5, 7], [6, 4]]
for sample in test_data:
    plt.scatter(sample[0], sample[1], s = 25, c = "black")

new_means = [[mean(xs[k]) for k in range(num_classes)], [mean(ys[k]) for k in range(num_classes)]]
new_stdevs = [[mean(xs[k]) for k in range(num_classes)], [stdev(ys[k]) for k in range(num_classes)]]
test_classes = []
for sample in test_data:
    conditionals = [[Gaussian(sample[i], new_means[i][k], new_stdevs[i][k]) for i in range(len(sample))] for k in range(num_classes)]
    test_classes.append(BayesClassifier(conditionals, class_probabilities, colors))
for i in range(len(test_data)):
    print("The point at " + str(test_data[i]) + " belongs to class " + str(test_classes[i]))
plt.show()
