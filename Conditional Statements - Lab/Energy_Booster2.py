fruit = input()
size = input()
quantity = int(input())
total = 0.0
# small

watermelon_price = 2 * 56
mango_price = 2* 36.66
pineapple_price = 2 * 42.10
raspberry_price = 2 * 20

# big

watermelon_price2 = 5 * 28.70
mango_price2 = 5 * 19.60
pineapple_price2 = 5 * 24.80
raspberry_price2 = 5 * 15.20

if fruit == "Watermelon":
    if size == "small":
     total = watermelon_price * quantity
    else:
     total = watermelon_price2 * quantity
if fruit == "Mango":
    if size == "small":
     total = mango_price * quantity
    else:
     total = mango_price2 * quantity
if  fruit == "Pineapple":
    if size == "small":
     total = pineapple_price * quantity
    else:
     total = pineapple_price2 * quantity
if fruit == "Raspberry":
    if size == "small":
     total = raspberry_price * quantity
    else:
     total = raspberry_price2 * quantity
if total >= 400 and total <= 1000:
    total= total - ( total * 0.15)
elif  total > 1000:
    total = total / 2
else:
    total = total
print(F"{total:.2F} lv.")


