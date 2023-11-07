first = int(input())
second = int(input())
max_num = int(input())
count = 0

for A in range(35, 56):
    for B in range(64, 97):
        for x in range(1,first + 1):
            for y in range(1, second + 1):
                count += 1
                print(F"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                if count == max_num:
                    exit()
                if x == first and y == second:
                    exit()
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64
