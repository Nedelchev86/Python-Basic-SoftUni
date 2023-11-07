# Входът се чете от конзолата и се състои от 3 реда:
# •	Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# •	Количество гориво – реално число в интервала [1.00 … 50.00]
# •	Притежание на клубна карта – текст с възможности: "Yes" или "No"

type_of_fuel =input()
fuel = float(input())
card = input()

gasoline_price = 2.22
diese_price = 2.33
gas_price = 0.93
total_price = 0.0

if card == "Yes":
    gasoline_price = gasoline_price - 0.18
    diese_price = diese_price - 0.12
    gas_price = gas_price - 0.08

if type_of_fuel == "Diesel":
    total_price = fuel * diese_price
elif type_of_fuel == "Gasoline":
    total_price = fuel * gasoline_price
elif type_of_fuel == "Gas":
    total_price = fuel * gas_price

if fuel >= 25:
    total_price = total_price - ( total_price * 0.10)
elif fuel > 20:
    total_price = total_price - ( total_price * 0.08)
else:
    total_price = total_price
print(F"{total_price:.2F} lv.")


# Напишете програма, която да изчислява,
# колко ще струва на един шофьор да напълни резервоара на автомобила си,
# като знаете – какъв тип гориво зарежда, каква е цената за литър гориво и дали разполага
# с карта за отстъпки. Цените на горивата са както следва:
