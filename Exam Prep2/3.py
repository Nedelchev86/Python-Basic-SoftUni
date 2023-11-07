month = input()
hours = int(input())
group = int(input())
time_of_days = input()

months = ["march", "april", "may"]

if month in months:
    if time_of_days == "day":
        price = 10.50
    else:
        price = 8.40
else:
    if time_of_days == "day":
        price = 12.60
    else:
        price = 10.20
if group >= 4:
    price = price * 0.90
if hours >= 5:
    price = price / 2
print(F"Price per person for one hour: {price:.2F}")
print(F"Total cost of the visit: {price * group * hours:.2F}")
