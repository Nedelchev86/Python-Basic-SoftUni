import math
series = input()
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght / 8
leisue_time = break_lenght / 4

time_taken = lunch_time + leisue_time + episode_lenght

time_left = break_lenght - time_taken


if time_left >= 0:
    print(F"You have enough time to watch {series} and left with {math.ceil(time_left)} minutes free time.")
else:
    print(F"You don't have enough time to watch {series}, you need {math.ceil(abs(time_left))} more minutes.")