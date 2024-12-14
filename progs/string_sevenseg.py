# assignment from edube.org
from sys import exit

font_lines = """
###|  #|###|###|# #|###|###|###|###|###
# #|  #|  #|  #|# #|#  |#  |  #|# #|# #
# #|  #|###|###|###|###|###|  #|###|###
# #|  #|#  |  #|  #|  #|# #|  #|# #|  #
###|  #|###|###|  #|###|###|  #|###|###
""".strip().split('\n')

# generate lookup table from base font
font = {}
for num in range(10):
    font[str(num)] = tuple(font_lines[x][num * 4:num * 4 + 3] for x in range(5)) # slice and dice
font[' '] = tuple(' ' for x in range(5))
font[''] = tuple('' for x in range(5))

# ask for number
number = -1

while number < 0:
    try:
        number = int(input("Enter a postive integer: "))
    except ValueError:
        print("That is not a number!")
        continue
    except:
        print("Something very bad happened.")
        exit()

output = list(font[''])

# build number string and include spacing
number_string = str(number).replace('', ' ').strip()

for ch in number_string:
    for i in range(5):
        output[i] += font[ch][i]

print('\n'.join(output))