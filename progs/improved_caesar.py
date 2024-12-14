# from https://edube.org/learn/pe-2/lab-improving-the-caesar-cipher-3

'''
You are already familiar with the Caesar cipher, and this is why we want you to
improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a,
and so on. Let's make it a bit harder, and allow the shifted value to come from
the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain
lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

* asks the user for one line of text to encrypt;
* asks the user for a shift value (an integer number from the range 1..25 - note:
  you should force the user to enter a valid shift value (don't give up and don't
  let bad data fool you!)
* prints out the encoded text.
'''

# base caesar shift
def _caesar(ch, shift = 1, base = 'A'):
    return chr((ord(ch) - ord(base) + shift) % 26 + ord(base))

# standard caesar shift
def caesar_std(plaintext):
    cyphertext = ''

    for ch in plaintext.upper():
        if ch.isalpha():
            cyphertext += _caesar(ch)
    
    return cyphertext

# enhanced caesar shift
def caesar_enh(plaintext, shift):
    cyphertext = ''

    for ch in plaintext:
        if ch.isupper():
            cyphertext += _caesar(ch, shift, 'A')
        elif ch.islower():
            cyphertext += _caesar(ch, shift, 'a')
        else:
            cyphertext += ch

    return cyphertext

# base code
plaintext = input('Enter your plaintext message: ')

while True:
    try:
        shift = int(input('Enter the shift value, an integer from 1 to 25: '))

        # validate range
        if shift < 1 or shift > 25:
            print('That is not in range!')
            continue
        
        break # exit if we have a valid integer

    except ValueError:
        print('That is not a integer!')
        continue

print(caesar_enh(plaintext, shift))