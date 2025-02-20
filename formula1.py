import math
from math import sqrt
from math import cos
print("нахождение длины третьей стороны треугольника")
print("введите длину первой стороны треугольника")
a = float(input())
print("введите длину второй стороны треугольника")
b = float(input())
print("введите угол (в градусах) между ними")
x = math.radians(float(input()))
c = sqrt(a**2 + b**2 -2*b*a*(math.cos(x)))
print ("Длина третьей стороны =", c)
