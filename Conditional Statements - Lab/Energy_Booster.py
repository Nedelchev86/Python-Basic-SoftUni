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

if fruit == "Watermelon" and size == "small":
    total = watermelon_price * quantity
elif fruit == "Watermelon" and size == "big":
    total = watermelon_price2 * quantity
elif fruit == "Mango" and size == "small":
    total = mango_price * quantity
elif fruit == "Mango" and size == "big":
    total = mango_price2 * quantity
elif fruit == "Pineapple" and size == "small":
    total = pineapple_price * quantity
elif fruit == "Pineapple" and size == "big":
    total = pineapple_price2 * quantity
elif fruit == "Raspberry" and size == "small":
    total = raspberry_price * quantity
elif fruit == "Raspberry" and size == "big":
    total = raspberry_price2 * quantity
if total >= 400 and total <= 1000:
    total= total - ( total * 0.15)
elif  total > 1000:
    total = total / 2
else:
    total = total
print(F"{total:.2F} lv.")


