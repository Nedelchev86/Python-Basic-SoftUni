minute_walk = int(input())
num_walk = int(input())
calories = int(input())

total_walk = minute_walk * num_walk
spent_calories = total_walk * 5
need_spend_calories = spent_calories
caloris_eat = calories / 2

if caloris_eat <= need_spend_calories:
    print("Yes, the walk for your cat is enough. Burned calories per day: " + str(spent_calories) + ".")
else:
    print("No, the walk for your cat is not enough. Burned calories per day: " + str(spent_calories)+ ".")
