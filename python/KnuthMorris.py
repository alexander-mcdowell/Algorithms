from termcolor import colored
import os
os.system('color')

def findBorders(str):
    b = []
    for i in range(0, len(str) + 1):
        b.append(0)
    j = 0
    for i in range(1, len(str)):
        while j > 0 and str[j] != str[i]:
            j = b[j]
        if str[j] == str[i]:
            j += 1
        b[i + 1] = j
    return b

def KnuthMorris(str, pattern):
    matches = []
    borders = findBorders(pattern)
    j = 0
    for i in range(0, len(str)):
        while j > 0 and pattern[j] != str[i]:
            j = borders[j]
        if pattern[j] == str[i]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = borders[j]
    return matches

if __name__ == '__main__':
    pattern = "AB"
    text = "AABABBBAABABBABBABABABBABABAB"
    matches = KnuthMorris(text, pattern)
    print("Target Str: %s, Pattern: %s" % (text, pattern))
    print("-" * 50)
    for m in matches:
        match_str = colored(text[m:m + len(pattern)], 'green')
        print("String match found at index %d: %s" % (m, text[:m] + match_str + text[m + len(pattern):]))
