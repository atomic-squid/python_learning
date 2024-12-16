# taken from LAB: https://edube.org/learn/pe-2/lab-anagrams-3

"""
An anagram is a new word formed by rearranging the letters of a word, using all the original
letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams,
while "I am" and "You are" are not.

Your task is to write a program which:

* asks the user for two separate texts;
* checks whether, the entered texts are anagrams and prints the result.0

Note:

* assume that two empty strings are not anagrams;
* treat upper- and lower-case letters as equal;
* spaces are not taken into account during the check - treat them as non-existent
"""

def is_anagram(left, right):
    left_letters, right_letters = [], []

    # populate lists with
    for ch in left.lower():
        if ch.isalpha():
            left_letters.append(ch)

    for ch in right.lower():
        if ch.isalpha():
            right_letters.append(ch)
    
    left_letters.sort()
    right_letters.sort()

    if left_letters == right_letters == []:
        return False
    else:
        return left_letters == right_letters

# run tests
# print(is_anagram("rail safety", "fairy tales"))
# print(is_anagram("I am", "You are"))

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
    print("Anagrams")
else:
    print("Not Anagrams")