budget = int(input())
season = input()
fishermens = int(input())
rent = 0

if season == "Spring":
    rent = 3000
elif season == "Winter":
    rent = 2600
else:
    rent = 4200

if fishermens <= 6:
    rent *= 0.90

elif 7 <= fishermens <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if fishermens % 2 == 0 and season != "Autumn":
    rent *= 0.95
if budget >= rent:
    print(F"Yes! You have {budget - rent:.2F} leva left.")
else:
    print(F"Not enough money! You need {rent - budget:.2F} leva.")
