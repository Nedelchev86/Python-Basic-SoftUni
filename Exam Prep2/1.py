from math import ceil
speed = float(input())
litters = float(input())
distance = 384400 * 2
total_liters = ((litters * distance) / 100)

time = distance / speed + 3
print(ceil(time))
print(int(total_liters))

