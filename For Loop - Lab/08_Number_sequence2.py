import sys

n = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for number in range(0, n):
    input_number = int(input())

    if input_number > max_number:
        max_number = input_number
    if input_number < min_number:
        min_number = input_number
print(F"Max number: {max_number}")
print(F"Min number: {min_number}")