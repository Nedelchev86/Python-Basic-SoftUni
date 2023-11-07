firs_time = int(input())
secont_time = int(input())
third_time = int(input())
total = firs_time + secont_time + third_time
min = total // 60
seconds = total % 60

if seconds < 10:
    print(F"{min}:0{seconds}")
    # print("str(min) +":0" str(seconds)
else:
    print(F"{min}:{seconds}")
