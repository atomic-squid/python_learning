#from: https://edube.org/learn/pe-2/working-with-real-files-52
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.

newdata = bytearray(10)

try:
    bf = open("file.bin", "rb")
    bf.readinto(newdata)
    bf.close()

    for bt in newdata:
        print(hex(bt))
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
