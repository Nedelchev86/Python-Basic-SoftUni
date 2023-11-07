N = int(input())

sum_right = 0
sum_left = 0
for number in range(0, N*2):
    input_number = int(input())
    if number < N:
        sum_left += input_number
    elif number >= N:
        sum_right += input_number

if sum_left == sum_right:
    print(F"Yes, sum = {sum_left}")
else:
    diff = abs(sum_left - sum_right)
    print(F"No, diff = {diff}")