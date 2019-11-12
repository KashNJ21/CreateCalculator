import math

def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b

def subtraction(a,b):
    a = int(a)
    b = int(b)
    return b - a

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c

def division(a, b):
    a = int(a)
    b = int(b)
    c = b/a
    return round(c,9)

def square(a):
    a = int(a)
    c = a*a
    return c

def squareroot(a):
    a = int(a)
    return math.sqrt(a)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self,a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqroot(self, a):
        self.result = squareroot(a)
        return self.result



