import math
record = float(input())
distance =float(input())
time_for_1meter = float(input())

time_to_finish = (distance * time_for_1meter)
delay = (math.floor(distance/50) * 30)

time_to_finish_all = (distance * time_for_1meter) + delay
different = time_to_finish_all - record

if time_to_finish_all < record:
    print(F" Yes! The new record is {time_to_finish_all:.2F} seconds.")
elif time_to_finish_all > record:
    print(F"No! He was {different:.2F} seconds slower.")
else:
    print(F"No! He was {different:.2F} seconds slower.")
