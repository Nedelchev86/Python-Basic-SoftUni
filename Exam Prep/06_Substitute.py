
K = int(input())
L = int(input())
M = int(input())
N = int(input())
count = 0

for a in range(K, 8 + 1):
    for b in range(9, L - 1, -1):
        for c in range(M, 8 +1):
            for d in range(9, N -1, -1):
                if a % 2 == 0 and b % 2 != 0 and c % 2 == 0 and d % 2 != 0:
                    if a == c and b == d:
                        print(F"Cannot change the same player.")
                    else:
                        print(F"{a}{b} - {c}{d}")
                        count += 1
                        if count == 6:
                            exit()