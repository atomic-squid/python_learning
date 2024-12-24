#from LAB: https://edube.org/learn/pe-2/lab-sorted-character-frequency-histogram-4

"""
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

* the output histogram will be sorted based on the characters' frequency (the bigger counter should
  be presented first)
* the histogram should be sent to a file with the same name as the input one, but with the suffix
  '.hist' (it should be concatenated to the original name)
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

sorted_hist = sorted(hist.items(), key = lambda item: item[1], reverse = True)

try:
    file = open(filename + ".hist", "wt", encoding="utf-8")
except IOError as e:
    print(f"Unable to open file: {strerror(e.errno)}")

for letter, count in sorted_hist:
    file.write(f"{letter} -> {count}\n")
file.close()