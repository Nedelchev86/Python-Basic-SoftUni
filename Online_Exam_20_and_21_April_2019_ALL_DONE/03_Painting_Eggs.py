#  Първи ред – размер на яйцата – текст с възможности "Large", "Medium" или "Small"
#  Втори ред – цвят на яйцата – текст с възможности "Red", "Green" или "Yellow"
#  Трети ред – брой партиди – цяло число в интервала [1… 350]

size = input()
color = input()
number = int(input())
price = 0

if size == "Large":
    if color == "Red":
        price = 16
    elif color == "Green":
        price = 12
    else:
        price = 9
elif size == "Medium":
    if color == "Red":
        price = 13
    elif color == "Green":
        price = 9
    else:
        price = 7
else:
    if color == "Red":
        price = 9
    elif color == "Green":
        price = 8
    else:
        price = 5
print(F"{(number * price) * 0.65:.2F} leva.")