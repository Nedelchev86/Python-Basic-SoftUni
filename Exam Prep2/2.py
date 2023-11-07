from math import floor
target = int(input())
workers = int(input())
working_day = int(input())
price_for_one = 110.10

total_time = workers * working_day * 8
processors_done = floor(total_time / 3)

if processors_done < target:
    print(F"Losses: -> {(target - processors_done) * price_for_one:.2F} BGN")
else:
    print(F"Profit: -> {(processors_done - target) * price_for_one:.2F} BGN")
