# from: https://edube.org/learn/pe-2/working-with-real-files-43
from os import strerror

try:
    cnt = 0
    s = open('newtext.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
