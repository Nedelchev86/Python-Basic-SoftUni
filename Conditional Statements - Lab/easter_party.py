guests = int(input())
price = float(input())
budget = float(input())
cake = budget - (budget * 0.9)

if guests >= 10 and guests <= 15:
    price = price - ( price * 0.15)
elif guests > 15 and guests <= 20:
    price = price - ( price * 0.2)
elif guests > 20:
    price = price - (price * 0.25)
total = (cake + (price * guests))
tip= total - budget
tip= abs(tip)
if total <= budget:
    print(F"It is party time! {tip:.2F} leva left.")
else:
    print(F"No party! {tip:.2F} leva needed.")
