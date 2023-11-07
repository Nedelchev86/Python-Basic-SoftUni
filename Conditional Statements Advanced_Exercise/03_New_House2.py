flowers = input()
count = int(input())
budget = int(input())

Roses = 5
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3
Gladiolus = 2.5

total_price = 0

if flowers == "Roses":
    total_price = Roses * count
    if count > 80:
        total_price *=  0.90

elif flowers == "Dahlias":
    total_price = Dahlias * count
    if count > 90:
        total_price *= 0.85

elif flowers == "Tulips":
    total_price = Tulips * count
    if count > 80:
        total_price *= 0.85

elif flowers == "Narcissus":
    total_price = Narcissus * count
    if count < 120:
        total_price *= 1.15

elif flowers == "Gladiolus":
    total_price = Gladiolus * count
    if count < 80:
        total_price *= 1.20

if budget >= total_price:
    print(F"Hey, you have a great garden with {count} {flowers} and {budget - total_price:.2F} leva left.")
else:
    print(F"Not enough money, you need {total_price - budget:.2F} leva more.")
