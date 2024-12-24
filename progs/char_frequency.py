#from LAB: https://edube.org/learn/pe-2/lab-character-frequency-histogram-3

"""
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each
letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able
to do that in reference to the Latin alphabet.

Your task is to write a program which:

* asks the user for the input file's name;
* reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are
  treated as equal)
* prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Create a test file for the code, and check if your histogram contains valid results.
"""

from os import strerror

filename = input("Enter the file you wish to scan: ")
try:
    file = open(filename, "rt", encoding="utf-8")
except IOError as e:
    print(f"Unable to open file: {strerror(e.errno)}")

hist = {}

for ch in file.read():
    if ch.isalpha():
        try:
            hist[ch.upper()] += 1
        except KeyError:
            hist[ch.upper()] = 1

file.close()

sort_list = sorted(hist.keys())

for letter in sort_list:
    print(f"{letter} -> {hist[letter]}")