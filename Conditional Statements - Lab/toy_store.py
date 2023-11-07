puzzle_price = 2.60
doly_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

vacantion = float(input())
puzzle = int(input())
doly = int(input())
bear = int(input())
minions = int(input())
trucks = int(input())

sum_puzzle = puzzle * puzzle_price
sum_doly = doly * doly_price
sum_bear = bear * bear_price
sum_minions = minions * minion_price
sum_trucks = trucks * truck_price

sum = sum_trucks + sum_minions + sum_bear + sum_doly + sum_puzzle
number_of_toys = puzzle + doly + bear + minions + trucks

if number_of_toys >= 50:
    sum = (sum - (sum *0.25))
else:
    sum = sum
total_money = sum - (sum * 0.1)
if total_money >= vacantion:
    print(F"Yes! {total_money-vacantion:.2F} lv left.")
else:
    print(F"Not enough money! {vacantion - total_money:.2F} lv needed.")





