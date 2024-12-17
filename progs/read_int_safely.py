# from LAB: https://edube.org/learn/pe-2/reading-ints-safely-4

"""
Your task is to write a function able to input integer values and to check if they are within a
specified range.

The function should:

* accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
* if the user enters a string that is not an integer value, the function should emit the message
  Error: wrong input, and ask the user to input the value again;
* if the user enters a number which falls outside the specified range, the function should emit
  the message Error: the value is not within permitted range (min..max) and ask the user to input
  the value again;
* if the input value is valid, return it as a result.
"""

def read_int(prompt, min, max):
    #
    # Write your code here.
    #
    while True:
        try:
            v = int(input(prompt))
            assert min <= v <= max
            return v
        except AssertionError:
            print(f"Error: the value is not in the permitteed range ({min}..{max})")
            continue
        except ValueError:
            print("Error: wrong input")
            continue


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
