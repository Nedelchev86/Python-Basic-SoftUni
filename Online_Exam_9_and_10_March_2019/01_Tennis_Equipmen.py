import math
tenis_rocket_price = float(input())
number_tenis_rocket = int(input())
number_sneakers = int(input())
sneakers_price = tenis_rocket_price / 6

sum = (tenis_rocket_price * number_tenis_rocket) + (number_sneakers * sneakers_price)
other = sum * 0.2

total = sum + other

print(F"Price to be paid by Djokovic {math.floor(total * 0.125)}")
print(F"Price to be paid by sponsors {math.ceil(total * 0.875)}")
