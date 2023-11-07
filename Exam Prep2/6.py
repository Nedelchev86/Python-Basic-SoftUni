location = int(input())
total_gold = 0

for i in range (location):
    expected_yield = float(input())
    days = int(input())
    total_gold = 0
    for j in range(days):
        derived_gold = float(input())
        total_gold += derived_gold
    if (total_gold / days) >= expected_yield:
        print(F"Good job! Average gold per day: {total_gold / days:.2F}.")
    else:
        print(F"You need {expected_yield - (total_gold / days):.2F} gold.")