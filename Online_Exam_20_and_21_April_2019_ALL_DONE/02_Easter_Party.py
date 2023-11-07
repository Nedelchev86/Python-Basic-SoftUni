
guests = int(input())
price = float(input())
budget = float(input())

if guests > 20:
    price = 0.75 * price
elif guests > 15:
    price = 0.8 * price
elif guests >=10 :
    price = 0.85 * price

cake = 0.1 * budget
total = guests * price + cake

if budget >= total:
    print(F"It is party time! {budget - total:.2F} leva left.")
else:
    print(F"No party! {total - budget:.2F} leva needed.")