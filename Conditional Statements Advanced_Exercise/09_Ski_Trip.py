days = int(input())
room = input()
raiting = input()

price = 0
one_person = 18
apartment = 25
president_apartment = 35

if days <10:
    if room == "apartment":
        price = apartment * 0.70
    elif room == "president apartment":
        price = president_apartment * 0.90
    else:
        price = one_person
if days <= 15:
    if room == "apartment":
        price =  apartment * 0.65
    elif room == "president apartment":
        price = president_apartment * 0.85
    else:
        price = one_person
if days > 15:
    if room == "apartment":
        price =  apartment * 0.50
    elif room == "president apartment":
        price = president_apartment * 0.80
    else:
        price = one_person
if raiting == "positive":
    print(F"{(days-1)*price*1.25:.2F}")
else:
    print(F"{(days - 1) * price * 0.90:.2F}")

