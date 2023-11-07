# От конзолата се четат 5 реда:
# 1. Име на филм - текст
# 2. Брой дни - цяло число в диапазона [1… 90]
# 3. Брой билети - цяло число в диапазона [100… 100000]
# 4. Цена на билет - реално число в диапазона [5.0… 25.0]
# 5. Процент за киното - цяло число в диапазона [5... 35]

movie = input()
days = int(input())
tickets = int(input())
price_for_ticket = float(input())
percent = int(input())

profit = (price_for_ticket * tickets * days) - ((price_for_ticket * tickets * days)  * percent / 100)
print(F"The profit from the movie {movie} is {profit:.2F} lv.")