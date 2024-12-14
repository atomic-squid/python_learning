# from https://edube.org/learn/pe-2/lab-palindromes-4

"""
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is
a palindrome, while "loyal" is not.

Your task is to write a program which:

* asks the user for some text;
* checks whether the entered text is a palindrome, and prints result.

Note:

* assume that an empty string isn't a palindrome;
* treat upper- and lower-case letters as equal;
* spaces are not taken into account during the check - treat them as non-existent;
* there are more than a few correct solutions - try to find more than one.
"""

def is_palindrome(palindrome):
    if palindrome == '':
        return False

    target_text = ''

    for ch in palindrome.lower():
        if ch.isalpha():
            target_text += ch
    
    return target_text == target_text[::-1]

palindrome = input("Enter your palindrome: ")

if is_palindrome(palindrome):
    print("It's a palindrome.")
else:
    print("Not a palindrome.")