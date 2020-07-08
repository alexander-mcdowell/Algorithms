import math
import datetime

def LinearCongruential(x, mod):
    multiplier = 1
    increment = 0
    return (multiplier * x + increment) % mod

def xorshift64(x):
    x = x ^ (x >> 12)
    x = x ^ (x << 25)
    x = x ^ (x >> 27)
    x *= 2685821657736338717
    return x

def xorshift1024(S):
    p = 0
    s0 = S[p]
    p = (p + 1) & 15
    s1 = S[p]
    s1 = s1 ^ (s1 << 31)
    s1 = s1 ^ (s1 >> 11)
    s0 = s0 ^ (s0 >> 30)
    S[p] = s0 ^ s1
    r = S[p] * 1181783497276652981
    return r

def random(low, high):
    seed = int(datetime.datetime.today().timestamp() * 1000)
    return (low + xorshift64(seed) % (high + 1))

def resevoirSample(stream, num_select):
    selected = []
    for i in range(0, num_select):
        selected.append(stream[i])
    t = num_select
    while t < len(stream):
        u = random(1, t)
        if u <= num_select:
            selected[u - 1] = stream[t]
        t += 1
    return selected

if __name__ == '__main__':
    seed = int(datetime.datetime.today().timestamp() * 1000)
    maximum = 100

    num = seed
    for i in range(0, 10):
        num = LinearCongruential(seed, maximum)
    print("Maximum of %d" % maximum)
    print("Random number from the Linear Congruential method: %d" % num)
    num = xorshift64(seed) % maximum
    print("Random number from the xorshift64 method: %d" % num)
    seed_num = seed
    seed = []
    for i in range(0, 16):
        seed.append(i + seed_num)
    num = xorshift1024(seed) % maximum
    print("Random number from the xorshift1024 method: %d" % num)
    print("-" * 50)

    items = ["Apples", "Bananas", "Cherries", "Durians", "Elderberries", "Grapes", "Kiwis", "Lemons", "Mangoes",
             "Peaches", "Raspberries"]
    sample_size = 7
    print("Items: " + str(items))
    print("Sample Size: %d" % sample_size)
    selected = resevoirSample(items, sample_size)
    print("Selected sample: " + str(selected))
