from termcolor import colored
import os
os.system('color')

def createOccurenceTable(pattern):
    table = []
    for i in range(0, 127):
        table.append(len(pattern))
    for i in range(0, len(pattern) - 1):
        table[ord(pattern[i])] = len(pattern) - i - 1
    return table

def BoyerMoore(text, pattern):
    matches = []
    table = createOccurenceTable(pattern)
    i = 0
    while i <= (len(text) - len(pattern)):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            matches.append(i)
        c = text[i + len(pattern) - 1]
        i += table[ord(c)]
    return matches

if __name__ == '__main__':
    pattern = "AB"
    text = "AABABBBAABABBABBABABABBABABAB"
    matches = BoyerMoore(text, pattern)
    print("Target Str: %s, Pattern: %s" % (text, pattern))
    print("-" * 50)
    for m in matches:
        match_str = colored(text[m:m + len(pattern)], 'green')
        print("String match found at index %d: %s" % (m, text[:m] + match_str + text[m + len(pattern):]))
