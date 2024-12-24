# from LAB: https://edube.org/learn/pe-2/triangle-1

"""
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going
to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is the list of our expectations:

* the constructor accepts three arguments - all of them are objects of the Point class;
* the points are stored inside the object as a private list;
* the class provides a parameterless method called perimeter(), which calculates the perimeter of the
  triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for
  the record, although we are sure that you know it perfectly yourself.)

Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter
is the same as ours.
"""

from math import hypot


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Point({self.__x}, {self.__y})"

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        delta_x = x - self.__x
        delta_y = y - self.__y
        return hypot(delta_x, delta_y)

    def distance_from_point(self, point):
        delta_x = point.getx() - self.__x
        delta_y = point.gety() - self.__y
        return hypot(delta_x, delta_y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__v = (vertice1, vertice2, vertice3)
    
    def __str__(self):
        return f"Triangle({self.__v[0]}, {self.__v[1]}, {self.__v[2]})"

    def perimeter(self):
        side_a = self.__v[0].distance_from_point(self.__v[1])
        side_b = self.__v[1].distance_from_point(self.__v[2])
        side_c = self.__v[2].distance_from_point(self.__v[0])
        return side_a + side_b + side_c

    def area(self):
        x1 = self.__v[0].getx() * (self.__v[1].gety() - self.__v[2].gety())
        x2 = self.__v[1].getx() * (self.__v[2].gety() - self.__v[0].gety())
        x3 = self.__v[2].getx() * (self.__v[0].gety() - self.__v[1].gety())
        return abs(x1 + x2 + x3) / 2


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
print(triangle.area())
print(triangle)