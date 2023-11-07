# МОЕ РЕШЕНИЕ
# number = int(input())
# bonus_score = 0.0
#
# if number <= 100:
#     bonus_score= 5
# elif number > 100 and number < 1000:
#     bonus_score=number *0.2
# else:
#     bonus_score=number * 0.1
# if number % 2 == 0:
#     bonus_score=bonus_score +1
# elif number % 10 == 5:
#     bonus_score =bonus_score +2
# print(bonus_score)
# print(number+bonus_score)

# от лекцията
numbers = int(input())
bonus_poits = 0

if numbers <= 100:
    bonus_poits = 5
elif numbers > 1000:
    bonus_poits = numbers * 0.1
else:
    bonus_poits = numbers * 0.2
if numbers % 2 == 0:
    bonus_poits += 1
elif numbers % 10 == 5:
    bonus_poits +=  2
print(bonus_poits)
print(numbers + bonus_poits)
