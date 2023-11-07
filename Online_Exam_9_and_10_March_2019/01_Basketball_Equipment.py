tax = int(input())

sneakers = tax * 0.6
clothes = sneakers * 0.8
ball = clothes / 4
other = ball / 5
total = sneakers + clothes + ball + other + tax
print(F"{total:.2F}")
