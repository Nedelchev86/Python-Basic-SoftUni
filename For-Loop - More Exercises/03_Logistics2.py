
item_number = int(input())
height = 0
total_heigh = 0
bus = 0
truck = 0
train = 0

for _ in range(item_number):
    height = int(input())
    if height <= 3:
        bus += height
    elif height <= 11:
        truck += height
    else:
        train += height

total_heigh = bus + truck + train
print(F"{(bus * 200 + truck * 175 + train * 120) / total_heigh:.2F}")
print(F"{bus / total_heigh * 100:.2F}%")
print(F"{truck / total_heigh * 100:.2F}%")
print(F"{train / total_heigh * 100:.2F}%")