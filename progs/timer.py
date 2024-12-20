# from LAB: https://edube.org/learn/pe-2/the-timer-class-1

"""
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some
specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international
missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from
range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range
[0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation
checks.

The class itself should provide the following facilities:

* objects of the class should be "printable", i.e. they should be able to implicitly convert themselves
  into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less
  than 10;
* the class should be equipped with parameterless methods called next_second() and previous_second(),
  incrementing the time stored inside objects by +1/-1 second respectively.

Use the following hints:

* all object's properties should be private;
* consider writing a separate function (not method!) to format the time string.

Complete the template we've provided in the editor. Run your code and check whether the output looks the
same as ours.
"""

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__time = hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        hour = (self.__time % 86400) // 3600
        minute = (self.__time % 3600) // 60
        second = self.__time % 60
        return f"{hour:02}:{minute:02}:{second:02}"

    def next_second(self):
        self.__time += 1

    def prev_second(self):
        self.__time -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
