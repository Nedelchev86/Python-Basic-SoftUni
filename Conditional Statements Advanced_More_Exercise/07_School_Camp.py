# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].

season = input()
group = input()
number_ot_students = int(input())
number_of_night = int(input())

sport = ""

price = 0

if season == "Winter":
    if group == "mixed":
        price = 10
        sport = "Ski"
    elif group == "boys":
        price = 9.60
        sport = "Judo"
    elif group == "girls":
        price = 9.60
        sport = "Gymnastics"
elif season == "Spring":
    if group == "mixed":
        price = 9.50
        sport = "Cycling"
    elif group == "boys":
        price = 7.20
        sport = "Tennis"
    elif group == "girls":
        price = 7.20
        sport = "Athletics"
elif season == "Summer":
    if group == "mixed":
        price = 20
        sport = "Swimming"
    elif group == "boys":
        price = 15
        sport = "Football"
    elif group == "girls":
        price = 15
        sport = "Volleyball"
if number_ot_students >= 50:
    price *= 0.50
elif 20 <= number_ot_students < 50:
    price *= 0.85
elif 10 <= number_ot_students:
    price *= 0.95
print(F"{sport} {number_of_night * number_ot_students * price:.2F} lv.")
