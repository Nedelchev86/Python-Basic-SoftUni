
budget = float(input())
extras = int(input())
clothing_price = float(input())

decot = budget * 0.1

if extras > 150:
    clothing_price *= 0.90
total_expenses = decot + ( extras * clothing_price)

if total_expenses <= budget:
    print("Action!")
    print(F"Wingard starts filming with {budget - total_expenses:.2F} leva left.")
else:
    print("Not enough money!")
    print(F"Wingard needs {total_expenses - budget:.2F} leva more.")