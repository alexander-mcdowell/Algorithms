import math

# Intersection algorithm: Finds the intersection between two functions given a known bound leftBound < intersection < rightBound
# Method:
    # 1. Set the "guess" point to halfway between the bounds.
    # 2. If both functions are nearly equal (their difference is zero) at this guess point, stop the algorithm.
    # 3. Otherwise, if their difference is negative, set the smaller bound to the guess point and repeat from 1.
    # 3 cont. If their difference is positive, set the larger bound to the guess point and repeat from 1.

def Intersection(func1, func2, leftBound, rightBound, dx = 1e-6):
    val = (leftBound + rightBound) / 2
    smaller = leftBound
    larger = rightBound
    diff = func1(val) - func2(val)
    while math.fabs(diff) > dx:
        if diff < 0:
            smaller = val
        else:
            larger = val
        val = (smaller + larger) / 2
        diff = func1(val) - func2(val)
    return val, func1(val)

if __name__ == '__main__':
    f = lambda x: x * x
    g = lambda x: math.sin(x)
    leftBound, rightBound = (0, 10)
    print(Intersection(f, g, leftBound, rightBound))
