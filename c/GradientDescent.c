#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#define NO_VALUE_FOUND -10000000

/* 
Single-variable gradient descent.
Gradient descent is a simple method for determining a local minimum of a function, though convergence is not always guaranteed.
x' = x - f'(x) * dx 
*/

double f(double x) {
    return pow(x, 4) - 3 * pow(x, 3) + 2;
}

double gradientDescent(double dx, double guess, double error) {
    int max_steps = 100000;
    int steps = 0;
    double x = guess;
    double step, x_new;

    while (steps < max_steps) {
        step = f(x + dx) - f(x);
        x_new = x - step;
        if (fabs(x_new - x) < error) return x_new;
        x = x_new;
        steps += 1;
    }

    (void) printf("Could not converge to a local minimum within the maximum number of steps.\n");
    return NO_VALUE_FOUND;
}

int main(int argc, char const *argv[]) {
    double guess = 1.0;
    double error = 1e-6;
    double dx = 1e-3;
    (void) printf("Local minimum found at %.5f\n.", gradientDescent(dx, guess, error));
    return 0;
}
