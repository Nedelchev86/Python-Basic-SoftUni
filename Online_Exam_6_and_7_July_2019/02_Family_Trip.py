# От конзолата се четат 4 реда:
#  Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
#  Брой нощувки – цяло число в интервала [0 … 1000]
#  Цена за нощувка – реално число в интервала [1.00 … 500.00]
#  Процент за допълнителни разходи – цяло число в интервала [0 … 100]

budget = float(input())
nights = int(input())
price_for_night = float(input())
other = float(input())

all_for_night = nights * price_for_night
other = budget * (other / 100)

if nights > 7:
    all_for_night *= 0.95
total = all_for_night + other

if budget >= total:
    print(F"Ivanovi will be left with {budget - total:.2F} leva after vacation.")
else:
    print(F"{total - budget:.2F} leva needed.")