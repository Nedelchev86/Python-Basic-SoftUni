import sys
n = int(input())
max_number = -sys.maxsize
sum_number = sys.maxsize
sum_number = 0

for number in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_number += num
if max_number == sum_number - max_number:
    print(F"Yes \nSum = {max_number}")
else:
    sum_diff = abs(max_number - sum_number)
    print(F"No\nDiff = {abs(max_number - sum_diff)}")