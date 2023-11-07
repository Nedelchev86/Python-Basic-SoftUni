# 1. Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry"
# 2. Размерът на сета - текст с възможности: "small" или "big"
# 3. Брой на поръчаните сетове - цяло число в интервала [1 … 10000]

fruit = input()
size = input()
count = int(input())
price = 0

if size =="small":
    if fruit == "Watermelon":
        price = 2 * 56
    elif fruit == "Mango":
        price =2 * 36.66
    elif fruit == "Pineapple":
        price =2 * 42.10
    elif fruit == "Raspberry":
        price =2 * 20

if size =="big":
    if fruit == "Watermelon":
        price = 5 * 28.70
    elif fruit == "Mango":
        price =5 * 19.60
    elif fruit == "Pineapple":
        price =5 * 24.80
    elif fruit == "Raspberry":
        price =5 * 15.20

total = price * count
if total >= 400 and total <= 1000:
    total *= 0.85
elif total > 1000:
    total /= 2
print(F"{total:.2F} lv.")