
excursion_price = float(input())

puzzles_count = int(input())
talking_dolle_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
talking_dolle_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

total_toys_count = puzzles_count + talking_dolle_count + teddy_bears_count + minions_count + trucks_count
total_toys_price = (puzzle_price * puzzles_count) + ( talking_dolle_price * talking_dolle_count) + \
    (teddy_bear_price * teddy_bears_count) + ( minion_price * minions_count) + (truck_price * trucks_count)
if total_toys_count >= 50:
    total_toys_price *= 0.75
total_toys_price *= 0.9
if total_toys_price >= excursion_price:
    print(F"Yes! {total_toys_price - excursion_price:.2F} lv left.")
else:
    print(F"Not enough money! {excursion_price - total_toys_price:.2F} lv needed.")