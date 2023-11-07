# Входът се чете от конзолата и се състои от три реда:
#  Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
#  Втори ред - пакет за филм - текст с възможности "Drink", "Popcorn" или "Menu"
#  Трети ред - брой билети - цяло число в интервала [1… 30]

movie = input()
package = input()
tickets = int(input())

price = 0

if movie == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    else:
        price = 19
elif movie == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    else:
        price = 30
else:
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    else:
        price = 14

total = tickets * price

if movie == "Star Wars" and tickets >= 4:
    total = total * 0.70
if movie == "Jumanji" and tickets == 2:
    total = total * 0.85
print(f"Your bill is {total:.2F} leva.")