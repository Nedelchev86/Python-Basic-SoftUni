# •	На първия ред е месецът - May, June, July, August, September или October;
# •	На втория ред е броят на нощувките - цяло число.

month = input()
number = int(input())
price = 0
price_apartment = 0
if month == "May" or month == "June":
    if type == "Studio":
      price = 50
    else:
      price_apartment = 65
elif month == "July" or month == "August":
    if type == "Studio":
      price = 75.20
    else:
      price_apartment = 68.70
elif month == "September" or month == "October":
    if type == "Studio":
      price = 76
    else:
      price_apartment = 77
if type == "Studio" and (month == "May" or month == "October"):
    if number >7:
        price *= 0.95
    elif number > 14:
        price *=0.70
elif type == "Studio" and (month == "June" or month == "September") and number > 14:
        price *=0.80
if type == "Apartment" and number > 14:
    price_apartment *= 0.90

print(price)
print(price_apartment)