# assignmen from 
from sys import exit

font = {
    '1': ("  #", "  #", "  #", "  #", "  #"),
    '2': ("###", "  #", "###", "#  ", "###"),
    '3': ("###", "  #", "###", "  #", "###"),
    '4': ("# #", "# #", "###", "  #", "  #"),
    '5': ("###", "#  ", "###", "  #", "###"),
    '6': ("###", "#  ", "###", "# #", "###"),
    '7': ("###", "  #", "  #", "  #", "  #"),
    '8': ("###", "# #", "###", "# #", "###"),
    '9': ("###", "# #", "###", "  #", "###"),
    '0': ("###", "# #", "# #", "# #", "###"),
    ' ': (" ", " ", " ", " ", " "),
    '': ("", "", "", "", "")
}

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