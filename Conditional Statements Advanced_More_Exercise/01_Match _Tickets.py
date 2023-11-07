budget = float(input())
category = input()
number = int(input())
vip_price = 499.99
normal_price = 249.99
transport = 0
cost = 0

if number <= 4:
  transport = budget * 0.75
elif number <= 9:
  transport = budget * 0.60
elif number <= 24:
  transport = budget * 0.50
elif number <= 49:
  transport = budget * 0.40
elif number > 49:
  transport = budget * 0.25

if category == "VIP":
  cost =   number * vip_price + transport
else:
  cost =  number * normal_price + transport

if (budget - cost) >= 0:
  print(F"Yes! You have {budget - cost:.2F} leva left.")
else:
  print(F"Not enough money! You need {cost - budget:.2F} leva.")