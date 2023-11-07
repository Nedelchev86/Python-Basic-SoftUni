#  Сумата, с която разполагаме - реално число в интервала [10.00…1000.00]
#  Пол - символ ('m' за мъж и 'f' за жена)
#  Възраст - цяло число в интервала [5…105]
#  Спорт - текст (една от възможностите в таблицата)

money = float(input())
gender = input()
age = int(input())
sport = input()
card = 0.00

if gender == "m" and sport == "Gym":
    card = 42
elif gender == "m" and sport == "Boxing":
    card = 41
elif gender == "m" and sport == "Yoga":
    card = 45
elif gender == "m" and sport == "Zumba":
    card = 34
elif gender == "m" and sport == "Dances":
    card = 51
elif gender == "m" and sport == "Pilates":
    card = 39
if gender == "f" and sport == "Gym":
    card = 35
elif gender == "f" and sport == "Boxing":
    card = 37
elif gender == "f" and sport == "Yoga":
    card = 42
elif gender == "f" and sport == "Zumba":
    card = 31
elif gender == "f" and sport == "Dances":
    card = 53
elif gender == "f" and sport == "Pilates":
    card = 37

if age <= 19:
    card = card * 0.80
else:
    card = card
if money >= card:
    print(F"You purchased a 1 month pass for {sport}.")
else:
    print(F"You don't have enough money! You need ${card - money:.2F} more.")
