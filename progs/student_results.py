# from LAB: https://edube.org/learn/pe-2/lab-evaluating-students-results-3

"""
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of
the file contains three elements: the student's first name, the student's last name, and the number
of point the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof.
Jekyll's file.

Your task is to write a program which:

* asks the user for Prof. Jekyll's file name;
* reads the file contents and counts the sum of the received points for each student;
* prints a simple (but sorted) report, just like this one:

Andrew Cox  1.5
Anna Boleyn 15.5
John Smith  7.0

Note:

* your program must be fully protected against all possible failures: the file's non-existence, the
  file's emptiness, or any input data failures; encountering any data error should cause immediate
  program termination, and the erroneous should be presented to the user;
* implement and use your own exceptions hierarchy - we've presented it in the editor; the second
  exception should be raised when a bad line is detect, and the third when the source file exists
  but is empty.
"""

from os import strerror

class StudentsDataException(Exception):
    def __init__(self, *args):
        super().__init__(self, *args)
        self.errno = 1

class BadLine(StudentsDataException):
    def __init__(self, line_number, line_content, message = "Invalid line"):
        super().__init__(self)
        self.line_number = line_number
        self.line_content = line_content
        self.message = message

    def __str__(self):
        return f"{self.message}: Line {self.line_number}, Content = \"{self.line_content.strip()}\""

class FileEmpty(StudentsDataException):
    def __init__(self, filename, message = "File is empty"):
        super().__init__(self)
        self.filename = filename
        self.message = message

    def __str__(self):
        return f"{self.message}: \"{self.filename}\""

filename = input("Enter the filename for the class notes: ")
try:
    scores = {}
    line_number = 0

    for line in open(filename, "rt", encoding="utf-8"):
        try:
            line_number += 1
            items = line.split()
            if len(items) != 3:
                raise BadLine(line_number, line)
            name = f"{items[1]}, {items[0]}"
            score = float(items[2])
            scores[name] += score
        except ValueError:
            raise BadLine(line_number, line)
        except KeyError:
            scores[name] = score

    if line_number == 0:
        raise FileEmpty(filename)

except IOError as e:
    print(f"Unable to open file: {strerror(e.errno)}")
    exit(e.errno)
except StudentsDataException as e:
    print(e)
    exit(e.errno)

for name, score in sorted(scores.items()):
    print(f"{name.ljust(20)} {score}")