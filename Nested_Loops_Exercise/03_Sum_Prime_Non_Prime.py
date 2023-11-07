sum_prime_number = 0
sum_non_prime_number = 0

while True:
    commant = input()

    if commant == "stop":
        break
    current_number = int(commant)
    is_prime = True

    if current_number < 0:
        print("Number is negative.")
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime_number += current_number
    else:
        sum_non_prime_number += current_number

print(F"Sum of all prime numbers is: {sum_prime_number}")
print(F"Sum of all non prime numbers is: {sum_non_prime_number}")