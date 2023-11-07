N = int(input())
sum_left = 0
sum_right = 0
current_number = 0

for i in range (0, N):
    current_number = int(input())
    sum_left += current_number
for i in range(0, N):
    current_number = int(input())
    sum_right += current_number

if sum_left == sum_right:
    print(F"Yes, sum = {sum_left} ")
else:
    print(F"No, diff = {abs(sum_left - sum_right)}")