from math import sqrt
print("Insert opposite and adjacent sides of triangle:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )