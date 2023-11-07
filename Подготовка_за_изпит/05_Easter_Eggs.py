egg_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max = 0

for i in range(egg_count):
    color = input()
    if color == "red":
        red_eggs += 1
    elif color == "orange":
        orange_eggs += 1
    elif color == "blue":
        blue_eggs += 1
    else:
        green_eggs += 1

print(F"Red eggs: {red_eggs}")
print(F"Orange eggs: {orange_eggs}")
print(F"Blue eggs: {blue_eggs}")
print(F"Green eggs: {green_eggs}")

if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    print(F"Max eggs: {red_eggs} -> red")
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    print(F"Max eggs: {orange_eggs} -> orange")
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    print(F"Max eggs: {blue_eggs} -> blue")
else:
    print(F"Max eggs: {green_eggs} -> green")