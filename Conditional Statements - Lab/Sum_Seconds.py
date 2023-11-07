first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time
time_in_minute = total_time // 60
time_in_second = total_time % 60

# мое решение
# if time_in_second < 10:
#     print(str(time_in_minute) +":0" +str(time_in_second))
# else:
#     print(str(time_in_minute) + ":" + str(time_in_second))

# от лекцията
# if time_in_second < 10:
#         print(F"{time_in_minute}:0{time_in_second}")
# else:
#         print(F"{time_in_minute}:{time_in_second}")

# if time_in_second < 10:
#     time_in_second = "0" + str(time_in_second)

time_in_second = "0" + str(time_in_second) if time_in_second < 10 else time_in_second
print(F"{time_in_minute}:{time_in_second}")


