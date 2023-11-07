# От конзолата се четат:
# • Бюджет - реално число в интервала [10.0… 100.0]
# • Брой сериали - n - цяло положително число в интервала [1… 10]
# За всеки сериал се четат по два реда:
# o Име на сериал - текст
# o Цена за сериал - реално число в интервала [1.0… 15.0

budget = float(input())
n = int(input())
total_money = 0

for i in range(n):
    name = input()
    price = float(input())
    if name == "Thrones":
        price = price * 0.50
    elif name == "Lucifer":
        price = price * 0.60
    elif name == "Protector":
        price = price * 0.70
    elif name == "TotalDrama":
        price = price * 0.80
    elif name == "Area":
        price = price * 0.90
    total_money += price

if budget < total_money:
    print(F"You need {total_money - budget:.2F} lv. more to buy the series!")
else:
    print(F"You bought all the series and left with {budget - total_money:.2F} lv.")