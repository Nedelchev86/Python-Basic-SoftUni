location = int(input())
total_gold = []

for i in range (location):
    expected_yield = float(input())
    days = int(input())
    total_gold = []
    for j in range(days):
        derived_gold = float(input())
        total_gold.append(derived_gold)
        average = sum(total_gold) / days
    if average >= expected_yield:
        print(F"Good job! Average gold per day: {average:.2F}.")
    else:
        print(F"You need {expected_yield - average:.2F} gold.")