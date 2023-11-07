number_of_location = int(input())
total_mining = 0
average_mining_for_day = 0

for location in range(number_of_location):
    average_mining_defolt = float(input())
    number_of_days_mining = int(input())
    total_mining = 0
    for day in range(number_of_days_mining):
        mining_for_day = float(input())
        total_mining += mining_for_day
        average_mining_for_day = total_mining / number_of_days_mining

    if average_mining_for_day >= average_mining_defolt:
        print(f"Good job! Average gold per day: {average_mining_for_day:.2f}.")

    else:
        print(f"You need {average_mining_defolt - average_mining_for_day:.2f} gold.")