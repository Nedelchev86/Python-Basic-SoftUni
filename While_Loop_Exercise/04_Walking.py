command = input()
total = 0
while command != "Going home":
    walk = int(command)
    total += walk
    if total >= 10000:
        print("Goal reached! Good job!")
        print(F"{total - 10000} steps over the goal!")
        break
    command = input()
else:
    more = int(input())
    total += more
    if total >= 10000:
     print("Goal reached! Good job!")
     print(F"{total - 10000} steps over the goal!")
    if total < 10000:
     print(F"{10000 - total} more steps to reach goal.")
