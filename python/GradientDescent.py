# Single-variable gradient descent.
# Gradient descent is a simple method for determining a local minimum of a function, though convergence is not always guaranteed.
# x' = x - f'(x) * dx

def gradientDescent(f, dx, guess, error):
    max_steps = 1000000
    steps = 0
    x = guess
    while steps < max_steps:
        step = f(x + dx) - f(x)
        x_new = x - step
        if abs(x_new - x) < error: return x_new
        x = x_new
        steps += 1
    print("Local minimum not found within maximum number of steps")
    return None

if __name__ == "__main__":
    f = lambda x: (x ** 4 - 3 * x ** 3 + 2)
    error = 1e-10
    guess = 1
    dx = 1e-4
    print(gradientDescent(f, dx, guess, error))