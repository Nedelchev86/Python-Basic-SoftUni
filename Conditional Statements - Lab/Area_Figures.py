import math
figure = input()
area = 0
if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a * side_b)
elif figure == "circle":
    radius = float(input())
    area = (math.pi * radius * radius)
elif figure == "triangle":
    side_a = float(input())
    side_ha = float(input())
    area = (side_ha * side_a) /2
print(F"{area:.3F}")

