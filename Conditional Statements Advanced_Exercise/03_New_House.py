flowers = input()
count = int(input())
budget = float(input())
price = 0

Roses = 5
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3
Gladiolus = 2.5

if flowers == "Roses":
    if count > 80:
        price = Roses * 0.90
    else:
        price = Roses
elif flowers == "Dahlias":
    if count > 90:
        price = Dahlias * 0.85
    else:
        price = Dahlias
elif flowers == "Tulips":
    if count > 80:
        price = Tulips * 0.85
    else:
        price = Tulips
elif flowers == "Narcissus":
    if count < 120:
        price = Narcissus * 1.15
    else:
        price = Narcissus
elif flowers == "Gladiolus":
    if count < 80:
        price = Gladiolus * 1.20
    else:
        price = Gladiolus
total = count * price
if budget >= total:
    print(F"Hey, you have a great garden with {count} {flowers} and {budget - total:.2F} leva left.")
else:
    print(F"Not enough money, you need {total - budget:.2F} leva more.")
