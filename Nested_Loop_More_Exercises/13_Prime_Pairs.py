first_pair = int(input())
second_pair = int(input())
difference_first_pair = int(input())
difference_second_pair = int(input())

for first in range(first_pair, first_pair + difference_first_pair + 1):

    for second in range(second_pair, second_pair + difference_second_pair + 1):

        if first % 2 == 0 or first % 3 == 0 or first % 5 == 0 or first % 7 == 0:
            continue

        if second % 2 == 0 or second % 3 == 0 or second % 5 == 0 or second % 7 == 0:
            continue

        print(f"{first}{second}")