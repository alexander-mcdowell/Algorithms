import math
import random
import numpy as np
import matplotlib.pyplot as plt

# deCasteljau's Algorithm: Creates a Bezier Curve through special geometric properties.
# Worst-case performance: O(t * n^2) where t is the number of timesteps and n is the number of points.
# Method:
    # 1. For a given t, do the following:
        # 2. For each line between start/end points and control points, draw a line.
        # 3. Create a point that is t% along each line.
        # 4. Remove the lines and draw new lines between the ponts. Repeat 2 and 3. until there is only one point left.
    # 2. Apply deCasteljau's algorithm for 0 < t < 1. The resulting points is a Bezier curve.

def deCasteljau(points, t):
    while len(points) > 1:
        new_points = []
        for i in range(len(points) - 1):
            x = points[i][0] + (points[i + 1][0] - points[i][0]) * t
            y = points[i][1] + (points[i + 1][1] - points[i][1]) * t
            new_points.append((x, y))
        points = new_points
    return points[0]

Min, Max = 0, 10
start, end = [(random.randint(Min, Max), random.randint(Min, Max)) for _ in [0, 1]]
controls = [(random.randint(Min, Max), random.randint(Min, Max)) for _ in range(3)]
points = [start,] + controls + [end]
ts = np.linspace(0, 1, 100)
beziers = [deCasteljau(points, t) for t in ts]
xs, ys = [bezier[0] for bezier in beziers], [bezier[1] for bezier in beziers]
plt.plot(xs, ys, "b-")

minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
bounding_points = [(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny), (minx, miny)]
for i in range(len(bounding_points) - 1):
    boundx = [bounding_points[i][0] + (bounding_points[i + 1][0] - bounding_points[i][0]) * t for t in ts]
    boundy = [bounding_points[i][1] + (bounding_points[i + 1][1] - bounding_points[i][1]) * t for t in ts]
    plt.plot(boundx, boundy, "g-")

for i in range(len(points) - 1):
    linex = [points[i][0] + (points[i + 1][0] - points[i][0]) * t for t in ts]
    liney = [points[i][1] + (points[i + 1][1] - points[i][1]) * t for t in ts]
    plt.plot(linex, liney, "k--")

text_offset = 0.1
plt.scatter(start[0], start[1], c = "red")
plt.text(start[0] + text_offset, start[1] + text_offset, "Start")
n = 1
for control in controls:
    plt.scatter(control[0], control[1], c = "black")
    plt.text(control[0] + text_offset, control[1] + text_offset, "Control-" + str(n))
    n += 1
plt.scatter(end[0], end[1], c = "red")
plt.text(end[0] + text_offset, end[1] + text_offset, "End")

plt.title("Bezier Curve using deCasteljau's Algorithm")
plt.show()
