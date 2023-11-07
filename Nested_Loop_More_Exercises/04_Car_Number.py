first = int(input())
second = int(input())

for i in range(first, second +1):
    for j in range(first, second + 1):
        for k in range(first, second + 1):
            for l in range(first, second + 1):
                if i % 2 == 0 and l % 2 != 0 or i % 2 != 0 and l % 2 == 0:
                    if i > l and (j + k) % 2 == 0:
                        print(F"{i}{j}{k}{l}", end=" ")
