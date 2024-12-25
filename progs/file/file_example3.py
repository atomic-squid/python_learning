#from: https://edube.org/learn/pe-2/working-with-real-files-44
from os import strerror

try:
    cnt = 0
    s = open('newtext.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
