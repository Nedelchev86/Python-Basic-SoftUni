#     • Опаковъчна хартия - 5.80 лв. за ролка
#     • Плат - 7.20 лв. за ролка
#     • Лепило - 1.20 лв. за литър
# Вход:

paper_price = 5.80
fabric_price = 7.20
glue_price = 1.20

paper = int(input())
fabric = int(input())
glue = float(input())
discount = float(input())

sum = (paper * paper_price) + (fabric * fabric_price) + (glue * glue_price)

print(F"{sum -(sum * discount /100):.3F}")
