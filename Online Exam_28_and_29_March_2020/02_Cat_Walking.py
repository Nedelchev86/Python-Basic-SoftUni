# Входът се чете от конзолата и съдържа точно 3 реда:
#  На първия ред - минути разходка на ден - цяло число в интервала [1...50]
#  На втория ред - броят на разходките дневно - цяло число в интервала [1…10]
#  На третия ред - приетите от котката калории на ден – цяло число в интервала [100…400

minute = int(input())
num_walkint = int(input())
calories = int(input())

burn_calories = num_walkint * minute * 5

if burn_calories >= calories / 2:
    print(F"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")
else:
    print(F"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")