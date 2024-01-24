from collections import Counter
import string
with open("books/frankenstion.txt") as f:
    stuff = f.read()
    words = stuff.lower()
    print(Counter(words))
    g=Counter(words)
    print(type(g))
    print(string.ascii_lowercase)
    for i in string.ascii_lowercase:
        print(f"The number of times the {i} character was found {g[i]} times")
