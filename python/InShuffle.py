import math

# In Shuffling splits the deck in half and merges each half.
# Example: Shuffling [0, 1, 2, 3, 4, 5] merges [0, 1, 2] and [3, 4, 5] forming [3, 0, 4, 1, 5, 2]
# As a general rule, one shuffle causes the element at index i to move to 2 * i mod (n + 1) where n is the length of the array.
# Thus, after k shuffles the element at i moves to 2^k * i mod (n + 1)

# Borrowing the exponentiation by squaring method from ExponentiationSqr.py
def modExpBySqr(n, k, p):
    d = k
    x = n % p
    c = 1
    while d > 1:
        if (d % 2 == 1):
            c *= x % p
        x *= x % p
        d = math.floor(d / 2)
    return (x * c) % p

# Shuffling using just recursion.
def recursion_shuffle(arr, times, count = 0):
    shuffled = []
    if count != times:
        left_half, right_half = arr[:math.floor(len(arr) / 2)], arr[math.floor(len(arr) / 2):]
        for _ in range(min(len(left_half), len(right_half))):
            shuffled.append(right_half.pop(0))
            shuffled.append(left_half.pop(0))
        shuffled += right_half
        return recursion_shuffle(shuffled, times, count + 1)
    return arr

# Shuffling using the math described in the header.
def power_shuffle(arr, times):
    if len(arr) % 2 == 1:
        return power_shuffle(arr[:-1], times) + [arr[-1]]
    n = len(arr)
    shuffled = [0] * n
    for i in range(1, n + 1): shuffled[(modExpBySqr(2, times, n + 1) * i) % (n + 1) - 1] = arr[i - 1]
    return shuffled

# a must have even length, else the shuffle method will keep the cards in the same place.
ranks = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["\u2663", "\u2666", "\u2665", "\u2660"]
cards = []
for s in suits:
    for r in ranks: cards.append(str(r) + s)
while True:
    times = input("How many shuffles do you want of a regular 52-card deck?\n")
    try:
        times = int(times)
        break
    except Exception as e:
        print("Provide your response as an integer.")
print("In Shuffle using recursion method:")
try:
    print(recursion_shuffle(cards, times))
except RecursionError as e:
    print("Execution took too long.")
print("In Shuffle using power method:")
print(power_shuffle(cards, times))
