happy = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1,10):
            for l in range(1,10):
                if i + j == k + l:
                    if happy % (i+j) == 0:
                        print(F"{i}{j}{k}{l}", end=" ")