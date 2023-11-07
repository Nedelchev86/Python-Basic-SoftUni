#  Брой козунаци - цяло число в интервала [0 … 99]
#  Брой кори с яйца - цяло число в интервала [0 … 99]
#  Килограми курабии - цяло число в интервала [0 … 99

# input by user

muffin_num = int(input())
eggs_num = int(input())
cookies_num = int(input())

# • Козунак – 3.20 лв.
# • Яйца – 4.35 лв. за кора с 12 яйца
# • Курабии – 5.40 лв. за килограм
# • Боя за яйца - 0.15 лв. за яйце

# available data

muffin_price = 3.20
eggs_price = 4.35
cookies_price = 5.40
egg_paint = 0.15

# let's do it
muffin = muffin_price * muffin_num
eggs = eggs_price * eggs_num
cookies = cookies_price * cookies_num
paint = eggs_num * 12 * egg_paint

total = muffin + eggs + cookies + paint
print(F"{total:.2F}")

