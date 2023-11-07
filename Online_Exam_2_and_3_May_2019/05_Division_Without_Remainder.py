n = int(input())
count_2 = 0
count_3 = 0
count_4 = 0

for i in range (n):
    command = int(input())
    if command % 2 == 0:
        count_2 += 1
    if command % 3 == 0:
        count_3 += 1
    if command % 4 == 0:
        count_4 += 1

print(F"{count_2 / n * 100:.2F}%")
print(F"{count_3 / n * 100:.2F}%")
print(F"{count_4 / n * 100:.2F}%")