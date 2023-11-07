import math
record_in_seconds = float(input())
record_in_meters = float(input())
seconds_for_meter = float(input())

water_resistance_second = math.floor(record_in_meters /15) * 12.5
swimmer_seconds = seconds_for_meter * record_in_meters + water_resistance_second

if swimmer_seconds > record_in_seconds:
    print(F"No, he failed! He was {swimmer_seconds - record_in_seconds:.2F} seconds slower.")
else:
    print(F"Yes, he succeeded! The new world record is {swimmer_seconds:.2F} seconds.")