# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# •	Втори ред –  Сезон – текст "Summer" или "Winter"

budget = float(input())
season = input()

destination = " "
place = " "

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        destination = "Alaska"
        budget *= 0.65
    else:
        destination = "Morocco"
        budget *= 0.45
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        destination = "Alaska"
        budget *= 0.80
    else:
        destination = "Morocco"
        budget *= 0.60
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        budget *= 0.90
    else:
        destination = "Morocco"
        budget *= 0.90

print(F"{destination} - {place} - {budget:.2F}")
