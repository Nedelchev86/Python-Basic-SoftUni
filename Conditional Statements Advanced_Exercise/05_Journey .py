budget = float(input())
season = input()
money_for_vacation = 0
destination = ""
type_ot_vacantion = ""

if budget > 1000:
    money_for_vacation = budget * 0.9
    destination = "Europe"
    type_ot_vacantion = "Hotel"
elif  budget > 100 and budget <= 1000:
    if season == "summer":
        money_for_vacation = budget * 0.40
        destination = "Balkans"
        type_ot_vacantion = "Camp"
    else:
        money_for_vacation = budget * 0.80
        destination = "Balkans"
        type_ot_vacantion = "Hotel"
elif budget <= 100:
    if season == "summer":
        money_for_vacation = budget * 0.30
        destination = "Bulgaria"
        type_ot_vacantion = "Camp"
    else:
        money_for_vacation = budget * 0.70
        destination = "Bulgaria"
        type_ot_vacantion = "Hotel"

print(F"Somewhere in {destination}")
print(F"{type_ot_vacantion} - {money_for_vacation:.2F}")