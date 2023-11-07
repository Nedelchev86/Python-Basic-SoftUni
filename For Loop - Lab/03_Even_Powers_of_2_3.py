from math import  pow

num = int(input())
result = 1
for i in range(0, num + 1):
    if i % 2 == 0:
        print(result)
    result *= 2