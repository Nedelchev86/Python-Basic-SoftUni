
eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max = 0

for i in range (eggs):
    color = input()
    if color == "red":
        red += 1
        if red > max:
            max = red
            max_color = color
    elif color == "orange":
        orange += 1
        if orange > max:
            max = orange
            max_color = color
    elif color == "blue":
        blue += 1
        if blue > max:
            max = blue
            max_color = color
    else:
        green += 1
        if green > max:
            max = green
            max_color = color
print(F"Red eggs: {red}")
print(F"Orange eggs: {orange}")
print(F"Blue eggs: {blue}")
print(F"Green eggs: {green}")
print(F"Max eggs: {max} -> {max_color}")
