
budget = float(input())
statist = int(input())
price_for_1 = float(input())

if statist > 150:
    price_for_1 = price_for_1 - ( price_for_1 * 0.1)
else:
    price_for_1 = price_for_1
total_for_statis = statist * price_for_1
decor = budget * 0.1
all = total_for_statis + decor
if all > budget:
    print("Not enough money!")
    print(F"Wingard needs {all - budget:.2F} leva more.")
else:
    print("Action!")
    print(F"Wingard starts filming with {budget - all:.2F} leva left.")