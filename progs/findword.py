# from LAB: https://edube.org/learn/pe-2/lab-find-a-word-3

"""
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a
combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising
the first string hidden inside the second string?

For example:

* if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
* if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters
  "d", "o", or "g", in this order)

Hints:

* you should use the two-argument variants of the pos() functions inside your code;
* don't worry about case sensitivity.
"""

def findword(target, source):
    num_found, num_chars, source_pos = 0, 0, 0
    target, source = target.lower(), source.lower()
    for ch in target:
        if ch.isalpha():
            num_chars += 1
            find_pos = source.find(ch, source_pos)
            if find_pos != -1:
                num_found += 1
                source_pos = find_pos + 1
    return num_found == num_chars

# tests
# print(findword("donor", "Nabucodonosor")) # true
# print(findword("donut", "Nabucodonosor")) # false
# print(findword("dog", "vcxzxduybfdsobywuefgas")) # true
# print(findword("dog", "vcxzxdcybfdstbywuefsas")) # false

target = input("Enter the string to search for: ")
source = input("Enter the string to search in: ")

if findword(target, source):
    print('Yes')
else:
    print('No')