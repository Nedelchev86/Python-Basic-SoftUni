
game_moves = int(input())
points = 0

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_number =  0
points = 0

for i in range(1, game_moves + 1):
    number = int(input())

    if number >= 0 and number <= 9:
        points += number * 0.2
        from_0_to_9 += 1
    elif number >= 10 and number <= 19:
        points += number * 0.3
        from_10_to_19 += 1
    elif number >= 20 and number <=  29:
        points += number * 0.4
        from_20_to_29 += 1
    elif number >= 30 and number  <= 39:
        points +=   50
        from_30_to_39 += 1
    elif number >= 40 and number <= 50:
        points +=  100
        from_40_to_50 += 1
    else:
        points /= 2
        invalid_number += 1


print(F"{points:.2F}")
print(F"From 0 to 9: { from_0_to_9 / game_moves * 100:.2F}%")
print(F"From 10 to 19: {from_10_to_19 / game_moves * 100:.2F}%")
print(F"From 20 to 29: {from_20_to_29 / game_moves * 100:.2F}%")
print(F"From 30 to 39: {from_30_to_39 / game_moves * 100:.2F}%")
print(F"From 40 to 50: {from_40_to_50 / game_moves * 100:.2F}%")
print(F"Invalid numbers: {invalid_number / game_moves * 100:.2F}%")
