# from: https://edube.org/learn/pe-2/working-with-real-files-47
from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('newtext.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
