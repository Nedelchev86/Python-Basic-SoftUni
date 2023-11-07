

bottle = int(input()) * 750
plates = 5
pots = 15
count = 0
total = 0
count_plates = 0
count_pots = 0

number = input()

while number != "End":
    command = int(number)
    count += 1
    if  count % 3 == 0:
        total += pots * command
        count_pots += command
    else:
        total += plates * command
        count_plates += command
    if total > bottle:
        print(f"Not enough detergent, {total - bottle} ml. more necessary!")
        break
    number = input()

if bottle >= total:
    print("Detergent was enough!")
    print(F"{count_plates} dishes and {count_pots} pots were washed.")
    print(F"Leftover detergent {bottle - total} ml.")

