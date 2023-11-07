# •	На първия ред е месецът - May, June, July, August, September или October;
# •	На втория ред е броят на нощувките - цяло число.

month = input()
number = int(input())
studio_price = 0
price_apartment = 0
if month == "May" or month == "October":
      studio_price = 50
      price_apartment = 65
elif month == "June" or month == "September":
      studio_price = 75.20
      price_apartment = 68.70
elif month == "July" or month == "August":
      studio_price = 76
      price_apartment = 77
if type == "Studio" and (month == "May" or month == "October"):
    if number >14:
        studio_price *= 0.95
    elif number > 7:
        studio_price *=0.70
elif type == "Studio" and (month == "June" or month == "September") and number > 14:
        studio_price *=0.80
if type == "Apartment" and number > 14:
    price_apartment *= 0.90

print(number * studio_price)
print(number * price_apartment)