
item_number = int(input())
height = 0
total_heigh = 0
bus = 0
truck = 0
train = 0
bus_height = 0
truck_height = 0
train_height = 0

for _ in range(item_number):
    height = int(input())
    if height <= 3:
        bus += height * 200
        bus_height += height
    elif height <= 11:
        truck += height * 175
        truck_height +=height
    else:
        train += height * 120
        train_height += height
total_heigh = bus_height + train_height + truck_height
print(F"{(bus + truck + train) / total_heigh:.2F}")
print(F"{bus_height / total_heigh * 100:.2F}%")
print(F"{truck_height / total_heigh * 100:.2F}%")
print(F"{train_height / total_heigh * 100:.2F}%")