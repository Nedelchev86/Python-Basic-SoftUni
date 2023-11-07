# •	Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
# •	Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]

season = input()
kilometers_for_month = float(input())

price_for_kilometers = 0
kilometers_for_season = 4 * kilometers_for_month
if kilometers_for_month <= 5000:
    if season == "Summer":
        price_for_kilometers = 0.90
    elif season == "Winter":
        price_for_kilometers = 1.05
    else:
        price_for_kilometers = 0.75
elif 5000 < kilometers_for_month <= 10000:
    if season == "Summer":
        price_for_kilometers = 1.10
    elif season == "Winter":
        price_for_kilometers = 1.25
    else:
        price_for_kilometers = 0.95
else:
    price_for_kilometers = 1.45
total = (price_for_kilometers * kilometers_for_season) * 0.90
print(F"{total:.2F}")