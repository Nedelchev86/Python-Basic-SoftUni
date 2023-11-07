food_buy = int(input()) * 1000
total = 0
food_eat = input()

while food_eat != "Adopted":
    food_per_day = int(food_eat)
    total += food_per_day
    food_eat=input()
if food_buy >= total:
    print(F"Food is enough! Leftovers: {food_buy - total} grams.")
else:
    print(F"Food is not enough. You need {total - food_buy} grams more.")
