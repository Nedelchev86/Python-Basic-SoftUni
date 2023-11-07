# От конзолата се четат 4 реда:
# 1. Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
# 2. Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
# 3. Сезон – текст, с възможности "Summer" и "Winter"
# 4. Брой дни – цяло число в диапазона [1… 40]

budget = int(input())
location = input()
season = input()
days = int(input())

money = 0
if season == "Summer":
    if location == "Dubai":
        money = 40000 * 0.7
    elif location == "Sofia":
        money = 12500 * 1.25
    else:
        money = 20250
else:
    if location == "Dubai":
        money = 45000 * 0.7
    elif location == "Sofia":
        money = 17000 * 1.25
    else:
        money = 24000
money_need = days * money

if budget > money_need:
    print(F"The budget for the movie is enough! We have {budget - money_need:.2f} leva left!")
else:
    print(F"The director needs {money_need - budget:.2F} leva more!")