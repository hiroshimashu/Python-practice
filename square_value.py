""""Write a method which can calculate square value of number"""

def square_value(s):
    """calculate square number of output"""
    return s ** 2

num1 = square_value(10)
print(num1)
num2 = square_value(-10)
print(num2)
num3 = square_value(1.5)
print(num3)
print(square_value.__doc__)