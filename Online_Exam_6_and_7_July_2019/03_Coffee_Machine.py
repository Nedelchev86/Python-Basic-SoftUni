drinks = input()
sugar = input()
number = int(input())
price = 0

if drinks == "Espresso":
    if sugar == "Without":
        price = 0.90 * 0.65
    elif sugar == "Normal":
        price = 1
    else:
        price = 1.20
elif drinks == "Cappuccino":
    if sugar == "Without":
        price = 1 * 0.65
    elif sugar == "Normal":
        price = 1.20
    else:
        price = 1.60
elif drinks == "Tea":
    if sugar == "Without":
        price = 0.50 * 0.65
    elif sugar == "Normal":
        price = 0.60
    else:
        price = 0.70

if drinks == "Espresso" and number >=5:
    price = price * 0.75
total = price * number
if total > 15:
    total = total * 0.80
print(F"You bought {number} cups of {drinks} for {total:.2F} lv.")

