# От конзолата се четат поредица от числа, всяко на отделен ред:
# Капацитетът на стадиона – цяло число в интервала [1 … 10000];
# Броят на всички фенове – цяло число в интервала [1 … 10000].
# За всеки един фен, на отделен ред се прочита:
# Секторът, на който се намира – текст – "A", "B", "V" и "G".

capacity = int(input())
fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(fans):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1
print(F"{sector_a / fans * 100:.2F}%")
print(F"{sector_b / fans * 100:.2F}%")
print(F"{sector_v / fans * 100:.2F}%")
print(F"{sector_g / fans * 100:.2F}%")
print(F"{(sector_g + sector_a + sector_v + sector_b) / capacity * 100:.2F}%")