number_joinery = int(input())
type_joinery = input()
delivery = input()

price = 0
price_for_delivery = 60
with_delivery = 0

if type_joinery == "90X130":
    if number_joinery > 60:
     price = (number_joinery * 110) * 0.92
    elif number_joinery > 30:
     price = (number_joinery * 110) * 0.95
    else:
        price = number_joinery * 110

if type_joinery == "100X150":
    if number_joinery > 80:
     price = (number_joinery * 140) * 0.90
    elif number_joinery > 40:
     price = (number_joinery * 140) * 0.94
    else:
        price = number_joinery * 140

if type_joinery == "130X180":
    if number_joinery > 50:
     price = (number_joinery * 190) * 0.88
    elif number_joinery > 20:
     price = (number_joinery * 190) * 0.93
    else:
        price = number_joinery * 190

if type_joinery == "200X300":
    if number_joinery > 50:
     price = (number_joinery * 250) * 0.86
    elif number_joinery > 25:
     price = (number_joinery * 250) * 0.91
    else:
        price = number_joinery * 250

if  delivery == "With delivery":
     price = price + 60


if number_joinery > 99:
    print(F"{price * 0.96:.2F} BGN")
elif number_joinery <= 10:
    print("Invalid order")
else:
    print(F"{price:.2F} BGN")