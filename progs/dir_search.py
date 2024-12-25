# from LAB: https://edube.org/learn/pe-2/the-os-module-lab-1

"""
Your program should meet the following requirements:

1: Write a function or method called find that takes two arguments called path and dir. The path
   argument should accept a relative or absolute path to a directory where the search should start,
   while the dir argument should be the name of a directory that you want to find in the given path.
   Your program should display the absolute paths if it finds a directory with the given name.
2: The directory search should be done recursively. This means that the search should also include all
   subdirectories in the given path.
"""

import os

def find(path, dir):
    directory_contents = os.listdir(path)
    for name in directory_contents:
        new_path = f"{path}/{name}"
        if name == dir:
            # print(f"match found, yeilding {new_path}")
            yield os.path.abspath(new_path)
        if os.path.isdir(new_path):
            # print(f"searching subdir {new_path}")
            yield from find(new_path, dir)

for path in find("./tree", "python"):
    print(path)