# От конзолата се четат 4 реда:
#     1. Брой танцьори – цяло число в интервала [1 … 10]
#     2. Брой точки – реално число в интервала [1.00 … 10000.00]
#     3. Сезон –  текст със следните възможности - "summer" или "winter"
#     4. Място – текст със следните възможности - "Bulgaria" или "Abroad"
# Изход:

dancer = int(input())
score = float(input())
season = input()
destination = input()
award = 0
money = 0

if destination == "Bulgaria":
    award = score * dancer
    if season =="summer":
        money = award * 0.95
    else:
        money = award * 0.92
else:
    award = (score * dancer) + (score * dancer) * 0.5
    if season =="summer":
        money = award * 0.90
    else:
        money = award * 0.85
donate = money * 0.75
print(F"Charity - {donate:.2F}")
print(F"Money per dancer - {(money * 0.25) / dancer:.2F}")