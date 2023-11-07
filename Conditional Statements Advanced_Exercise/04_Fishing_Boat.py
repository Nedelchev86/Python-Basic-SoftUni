budget = int(input())
season = input()
fishermens = int(input())
rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
# elif season == "Winter":
else:
    rent = 2600
if fishermens <= 7:
    rent *= 0.90
# elif  fishermens > 7 and fishermens <= 11:
elif 7 < fishermens <= 11:
    rent *= 0.85
#elif fishermens > 12:
else:
    rent *= 0.75
if fishermens % 2 == 0 and season != "Autumn":
    rent *= 0.95
if budget >= rent:
    print(F"Yes! You have {budget - rent:.2F} leva left.")
else:
    print(F"Not enough money! You need {rent - budget:.2F} leva.")
