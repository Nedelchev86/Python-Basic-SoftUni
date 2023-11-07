
import math
world_record = float(input())
distance = float(input())
time_for_meter = float(input())

delay = (math.floor(distance / 15 ) * 12.5)
time_for_swiming = (distance * time_for_meter) + delay

if time_for_swiming < world_record:
    print(F"Yes, he succeeded! The new world record is {time_for_swiming:.2F} seconds.")
else:
    print(F"No, he failed! He was {time_for_swiming - world_record:.2F} seconds slower.")

