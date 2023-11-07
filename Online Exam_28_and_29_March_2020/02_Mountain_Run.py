
import math

world_record = float(input())
distance = float(input())
time_for_1_m = float(input())


time_late = (math.floor(distance / 50)) * 30
time_for_georgi = distance * time_for_1_m + time_late

if world_record > time_for_georgi:
    print(F" Yes! The new record is {time_for_georgi:.2F} seconds.")
else:
    print(F"No! He was {time_for_georgi - world_record:.2F} seconds slower.")
