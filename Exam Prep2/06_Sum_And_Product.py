n = int(input())

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(9):
            for d in range(9, c, -1):
                if (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(F"{d}{c}{b}{a}")
                    exit()
                if (a * b * c * d) == (a + b + c + d) and n % 5 == 0:
                    print((F"{a}{b}{c}{d}"))
                    exit()
print("Nothing found")
