cats = int(input())
small_cat = []
big_cat = []
huge_cat = []
total_foods = []

for i in range(cats):
    foods = float(input())
    total_foods.append(foods)
    if foods < 200:
        small_cat.append(1)
    elif foods < 300:
        big_cat.append(1)
    else:
        huge_cat.append(1)
print(F"Group 1: {len(small_cat)} cats.")
print(F"Group 2: {len(big_cat)} cats.")
print(F"Group 3: {len(huge_cat)} cats.")
print(F"Price for food per day: {(sum(total_foods) / 1000) * 12.45:.2F} lv.")
