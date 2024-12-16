# from LAB: https://edube.org/learn/pe-2/lab-the-digit-of-life-3

"""
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you
just need to sum all the digits of the date. If the result contains more than one digit, you have
to repeat the addition until you get exactly one digit. For example:

* 1 January 2017 = 2017 01 01
* 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
* 1 + 2 = 3

3 is the digit we searched for and found.

Your task is to write a program which:

* asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually,
  the order of the digits doesn't matter)
* outputs the Digit of Life for the date.
"""

# recusive to make life easier
def digit_of_life(num):
    if -10 < num < 10:
        return num
    val = sum(int(n) for n in str(num))
    return digit_of_life(val)

# test code
# print(digit_of_life(19991229))
# print(digit_of_life(20000101))

while True:
    try:
        num = int(input("Enter your birthday (In YYYYMMDD, YYYYDDMM, or MMDDYYYY form): "))

        if len(str(num)) != 8:
            print("Incorrect number of digits!")
            continue

        break # exit loop if everything else is good
    except ValueError:
        print("Not a Integer!")

print(digit_of_life(num))