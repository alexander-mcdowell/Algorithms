import numpy as np
import matplotlib.pyplot as plt

# Ordinary Least Squares: A method for finding the best-fit curve, in this case a polynomial, to a set of (x, y) pairs.
# If the data can be described as y = X * w where y is the output data, X is the data matrix, and w is the weight vector, then w = (X.T * X)^-1 * X.T * y

def predict(x, weights):
    val = 0
    n = 0
    for w in weights:
        val += w * x ** n
        n += 1
    return val

def OLS(data_matrix, ys):
    meany = sum(ys) / len(ys)
    SStot = sum([(y - meany) ** 2 for y in ys])
    weights = np.dot(np.dot(np.linalg.inv(np.dot(data_matrix.T, data_matrix)), data_matrix.T), ys)
    SSres = sum([(ys[i] - predict(data_matrix[i][1], weights)) ** 2 for i in range(len(ys))])
    r2 = 1 - SSres/SStot
    return weights, r2

xs = [1, 2, 4, 7, 10, 14]
ys = np.asarray([3, 5, 6, 8, 12, 21])
degree = 3
data_matrix = np.array([[x ** n for n in range(degree + 1)] for x in xs])
weights, r2 = OLS(data_matrix, ys)
plt.scatter(xs, ys, c = "black")
model_xs = np.linspace(min(xs), max(xs), 100)
model_ys = [predict(x, weights) for x in model_xs]
plt.plot(model_xs, model_ys, "r-")
equation = "y = "
n = len(weights) - 1
for w in weights[::-1]:
    if n == len(weights) - 1: equation += "%.3fx^%d" % (w, n)
    else:
        if n == 0:
            if w >= 0: equation += " + %.3f" % w
            else: equation += " - %.3f" % abs(w)
        else:
            if w >= 0: equation += " + %.3fx^%d" % (w, n)
            else: equation += " - %.3fx^%d" % (abs(w), n)
    n -= 1
plt.suptitle("Ordinary Least Squares Regression")
plt.title(equation + ". R^2 = %.4f" % r2)
plt.show()
