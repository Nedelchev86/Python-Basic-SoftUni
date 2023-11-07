
capacity = float(input())
suitcase = input()
total = 0
count = 0
good = True

while  suitcase != "End":
    more_suitcase = float(suitcase)
    remaining_stace = capacity - total
    if remaining_stace < more_suitcase:
        print("No more space!")
        good = False
        break
    count +=1
    if count % 3 == 0:
        more_suitcase = more_suitcase * 1.1
    total += more_suitcase
    suitcase = input()

if good:
    print("Congratulations! All suitcases are loaded!")
print(F"Statistic: {count} suitcases loaded.")

