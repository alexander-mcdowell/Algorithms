import math

# Newton's Method: Computes the zeros of a function by repeatedly calculating "guesses" using the derivative.
# Method:
    # 1. Estimate the derivative at the guess point.
    # 2. Calculate the guess point using new_guess = guess - f(guess) / f'(guess).
    # 3. Repeat #1 and #2 as many times as needed.

def NewtonsMethod(f, guess, max_steps, dx = 0.001):
    for step in range(max_steps):
        derivative = (f(guess + dx) - f(guess)) / dx
        guess = guess - (f(guess) / derivative)
        step += 1
    return guess

if __name__ == '__main__':
    func = lambda x: x ** 2 - 3
    print(NewtonsMethod(func, 1, 50))
