# Известно е, че:
# Декорът за филма е на стойност 10% от бюджета.
# При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.


# Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Брой на статистите – цяло число в интервала [1 … 500]
# Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

budget = float(input())
statist = int(input())
price_for_one = float(input())

if statist > 150:
    price_for_one = price_for_one * 0.90

decor = 0.1 * budget
total_for_Statis = statist * price_for_one
grand_total = total_for_Statis + decor

if budget < (decor + total_for_Statis):
    print("Not enough money!")
    print(F"Wingard needs {grand_total - budget:.2F} leva more.")
else:
    print("Action!")
    print(F"Wingard starts filming with {budget - grand_total:.2F} leva left.")
