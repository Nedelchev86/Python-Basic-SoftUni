name = input()

total_points = 301
count = 0
bad_count = 0

while total_points != 0:
    target = input()
    if target == "Retire":
        print(F"{name} retired after {bad_count} unsuccessful shots.")
        break
    poits = int(input())
    if target == "Single":
        poits = poits
    elif target == "Double":
        poits = poits * 2
    elif target == "Triple":
        poits = poits * 3
    total_points -= poits
    if total_points < 0:
        total_points += poits
        bad_count +=1
    else:
        count += 1
else:
    print(F"{name} won the leg with {count} shots.")
