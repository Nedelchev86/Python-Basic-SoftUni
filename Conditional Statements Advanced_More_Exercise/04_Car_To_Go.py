# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# •	Втори ред –  Сезон – текст "Summer" или "Winter

budget = float(input())
season = input()

car_class = ""
car_type = ""
price = 0

if budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.90
elif budget >= 100 and budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.45
    else:
        car_type = "Jeep"
        price = budget * 0.80
elif budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    else:
        car_type = "Jeep"
        price = budget * 0.65
print(car_class)
print(F"{car_type} - {price:.2F}")
