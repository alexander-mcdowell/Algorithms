import numpy as np
import matplotlib.pyplot as plt

# Simple Linear Regression: A simplification of the Ordinary Least Squares method for fitting a curve to data.
# Simple Linear Regression finds the best-fit line that relates a single input variable with a single output variable.

def univariate_regression(xs, ys):
    assert len(xs) == len(ys)
    N = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum([x * x for x in xs])
    sxy = sum([xs[i] * ys[i] for i in range(N)])
    w1 = (N * sxy - sx * sy) / (N * sxx - sx ** 2)
    w0 = (sy - w1 * sx) / N
    meany = sy / N
    SStot = sum([(y - meany) ** 2 for y in ys])
    SSres = sum([(ys[i] - (w0 + w1 * xs[i])) ** 2 for i in range(N)])
    r2 = 1 - SSres/SStot
    return w0, w1, r2

xs = [1, 2, 3, 4, 5, 6]
ys = [2, 1, 4, 5, 5, 9]
b, w, r2 = univariate_regression(xs, ys)
plt.scatter(xs, ys, c = "black")
model_xs = np.linspace(min(xs), max(xs), 100)
model_ys = w * model_xs + b
plt.plot(model_xs, model_ys, "r-")
equation = "y = %.3fx" % w
if b >= 0: equation += " + %.3f" % b
else: equation += " - %.3f" % abs(b)
plt.suptitle("Simple Linear Regression")
plt.title(equation + ". R^2 = %.4f" % r2)
plt.show()
