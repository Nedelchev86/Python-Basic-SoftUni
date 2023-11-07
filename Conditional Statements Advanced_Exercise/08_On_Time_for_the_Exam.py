
exam_hours = int(input())
exam_minute = int(input())
arrive_hours = int(input())
arrive_minutes = int(input())

exam_sum = (exam_hours * 60) + exam_minute
arrive_sum = (arrive_hours * 60) + arrive_minutes

diference = arrive_sum - exam_sum

message_time = "Late"
if diference < -30:
    message_time = "Early"
elif diference <= 0:
    message_time = "On time"

print(message_time)

result = ""

if diference !=0:
    hours = abs(diference) // 60
    minutes = abs(diference) % 60
    if hours > 0:
        result = F"{hours}:{minutes:02} hours"
    else:
        result = F"{minutes} minutes"
    if diference < 0:
        print(F"{result} before the start")
    else:
        print(F"{result} after the start")