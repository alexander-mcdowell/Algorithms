import random

# Monte-Carlo Method: A class of algorithms in which a complicated problem is approximated through many trials/samples.
# The algorithm below computes the value of pi by "throwing darts" against a circular "dartboard" of radius 1/2 inscribed in a square of side length 1.
# The number of darts which land in the circle, if a large number of darts are thrown, should approximately by the area of the circle.
# Monte-Carlo methods require the number of trials to be very large and so they don't scale well if one wants a precise value.

def MonteCarlo_Pi(num_points):
    correct_points = 0
    incorrect_points = 0

    for n in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if (x ** 2) + (y ** 2) <= 1:
            correct_points += 1
        else:
            incorrect_points += 1

    return 4 * (correct_points / num_points)

if __name__ == '__main__':
    print(MonteCarlo_Pi(int(5e7)))
