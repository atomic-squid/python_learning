class Fib:
    __fib = (1, 1) # Remember our previous calculated values

    def __calc_fib(n):
        try:
            return Fib.__fib[n]
        except IndexError:
            v = Fib.__calc_fib(n - 2) + Fib.__calc_fib(n - 1)
            Fib.__fib += (v,)
            return v

    def __init__(self, nn):
        if nn < 1:
            raise ValueError("Value must be 1 or higher")
        self.__n = nn
        self.__i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__i >= self.__n:
            raise StopIteration
        v = Fib.__calc_fib(self.__i)
        self.__i += 1
        return v

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        return self.__iter

object = Class(12)

for n in object:
    print(n)

print(Fib._Fib__fib)