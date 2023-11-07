#  при добавен мобилен интернет, към таксата за един месец се добавя:
# o при такса по-малка или равна на 10.00 лв.  5.50 лв.
# o при такса по-малка или равна на 30.00 лв.  4.35 лв.
# o при такса по-голяма от 30.00 лв.  3.85 лв.
#  ако договорът e за две години, общата сума се намалява с 3.75%

# От конзолата се четат 3 реда:
# 1. Срок на договор – текст – "one", или "two"
# 2. Тип на договор – текст – "Small", "Middle", "Large"или "ExtraLarge"
# 3. Добавен мобилен интернет – текст – "yes" или "no"
# 4. Брой месеци за плащане - цяло число в интервала [1 … 24

period = input()
type = input()
internet = input()
months = int(input())
price = 0
total = 0

if period == "one":
    if type == "Small":
        price = 9.98
    elif type == "Middle":
        price = 18.99
    elif type == "Large":
        price = 25.98
    else:
        price = 35.99
else:
    if type == "Small":
        price = 8.58
    elif type == "Middle":
        price = 17.09
    elif type == "Large":
        price = 23.59
    else:
        price = 31.79
if internet == "yes":
    if price <=10:
        price += 5.50
    elif price <=30:
        price +=4.35
    else:
        price +=3.85
if period == "two":
    total =(months * price) * 0.9625
else:
    total = months * price
print(F"{total:.2F} lv.")
