start = 5364
end = 8848
days = 1

while days < 5:
    rest = input()
    if rest == "END":
        break
    if rest == "Yes":
        days += 1
    climb = int(input())
    start += climb
    if start >= end:
        print(F"Goal reached for {days} days!")
        exit()
print(F"Failed!")
print(start)
print(days)