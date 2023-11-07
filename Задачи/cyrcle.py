import math
radius = float(input())

area = 2 * radius * math.pi
girth = math.pi * (radius * radius)
print(f"{girth:.2F}")
print(f"{area:.2F}")
