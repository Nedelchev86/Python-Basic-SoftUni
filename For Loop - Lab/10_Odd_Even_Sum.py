n = int(input())
odd_sum = 0
even_sum = 0

for number in range (0, n):
    input_number = int(input())
    if number % 2 == 0:
        odd_sum += input_number
    else:
        even_sum += input_number
if odd_sum == even_sum:
    print("Yes")
    print(F"Sum = {even_sum}")
else:
    print("No")
    print(F"Diff = {abs(odd_sum - even_sum)}")
