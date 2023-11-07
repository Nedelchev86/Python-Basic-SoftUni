first = int(input())
second = int(input())
third = int(input())

for a in range(1, first + 1):
    for b in range(1, second + 1):
        for c in range(1, third + 1):
            if a % 2 == 0 and c % 2 == 0:
                if b == 2 or b == 3 or b == 5 or b == 7:
                    print(F"{a} {b} {c}")