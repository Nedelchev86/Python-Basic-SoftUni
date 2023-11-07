# hours = int(input())
# minutes = int(input()) + 15
#
# if minutes > 59:
#     hours += 1
#     minutes -= 60
# if hours > 23:
#     hours = 0
#
# print(f'{hours}:{minutes:02d}')

# import math
# hours = int(input())
# minutes = int(input())
#
# total_minutes = hours * 60 + minutes + 15
# new_hours = total_minutes / 60
# new_minutes = total_minutes % 60
#
# new_hours = math.floor(new_hours)
#
# if new_hours > 23:
#     new_hours = 0
#
# if new_minutes < 10:
#     print(f"{new_hours}:0{new_minutes}")
# else:
#     print(f"{new_hours}:{new_minutes}")

# от лекцията

hours = int(input())
minutes = int(input()) + 15
if minutes > 59:
    hours += 1
    minutes -= 60
if hours > 23:
    hours -= 24
if minutes < 10:
    print(F"{hours}:0{minutes}")
else:
    print(F"{hours}:{minutes}")
